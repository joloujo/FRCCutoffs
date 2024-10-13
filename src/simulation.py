from typing import Any, Dict, List
from statbotics.main import Statbotics # type: ignore 
from TBA_API import TBA_API_Interface
import random
from scipy.special import expit # type: ignore 
from interfaces import Team, EventInfo
from Cheesy_API import Cheesy_API

sb = Statbotics()
TBA_API = TBA_API_Interface()

def get_event_info(event: str, year: int) -> EventInfo:
    event_key: str = f'{year}{event.lower()}'
    sb_teams: List[Dict[str, Any]] = sb.get_team_events(event=event_key, fields=['team', 'epa_end', 'rp_1_epa_end', 'rp_2_epa_end'])

    teams = [
        Team(team=team['team'], total_epa=team['epa_end'], rp1_epa=team['rp_1_epa_end'], rp2_epa=team['rp_2_epa_end'])
        for team in sb_teams]

    return EventInfo(teams, Cheesy_API.shuffled(len(teams), 12))

def event_simulation(eventInfo: EventInfo, score_sd: float) -> dict[int, int]:
    team_numbers = list(eventInfo.teams.keys())

    rps: list[int] = [0] * len(team_numbers)

    schedule: list[list[int]] = eventInfo.schedule

    for match in schedule:
        # Get team indexes and objects for the match
        red_team_indexes: list[int] = match[:3]
        blue_team_indexes: list[int] = match[3:]

        red_teams: list[Team] = [eventInfo.teams[team_numbers[team_index]] for team_index in red_team_indexes]
        blue_teams: list[Team] = [eventInfo.teams[team_numbers[team_index]] for team_index in blue_team_indexes]

        # Find the total EPA of each team to calculate the win percentage
        red_epa: float = sum([team.total_epa for team in red_teams])
        blue_epa: float = sum([team.total_epa for team in blue_teams])

        red_win_prob: float = 1 / (
            1 + 10 ** (-5 / 8 * (red_epa - blue_epa) / score_sd)
        )

        # Calculate RP probabilities for each team
        red_rp1_prob = expit(sum(team.rp1_epa for team in red_teams))
        blue_rp1_prob = expit(sum(team.rp1_epa for team in blue_teams))
        red_rp2_prob = expit(sum(team.rp2_epa for team in red_teams))
        blue_rp2_prob = expit(sum(team.rp2_epa for team in blue_teams))

        # Calculate winner and each team's ranking points
        red_win: bool = random.random() < red_win_prob

        red_rps: int = (2 if red_win else 0) + (1 if random.random() < red_rp1_prob else 0) + (1 if random.random() < red_rp2_prob else 0)
        blue_rps: int = (2 if not red_win else 0) + (1 if random.random() < blue_rp1_prob else 0) + (1 if random.random() < blue_rp2_prob else 0)

        # Assign ranking points
        for team_index in red_team_indexes:
            rps[team_index] += red_rps 

        for team_index in blue_team_indexes:
            rps[team_index] += blue_rps 

    return {pair[0]: pair[1] for pair in zip(team_numbers, rps)}
