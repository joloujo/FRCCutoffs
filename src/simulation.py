from statbotics.main import Statbotics
from TBA_API import TBA_API_Interface
from pprint import pp
from utils import cheesy_schedule
import random
from scipy.special import expit

sb = Statbotics()
TBA_API = TBA_API_Interface()


def event_simulation(event_code: str, year: int):
    # Get event information
    event_key = f'{year}{event_code.lower()}'
    # tba_teams = TBA_API.request(f'/event/{tba_event_key}/teams/simple')
    # teams = [int(team["team_number"]) for team in tba_teams]

    # Get the teams and their EPAs
    sb_teams = sb.get_team_events(event=event_key, fields=['team', 'epa_end', 'rp_1_epa_end', 'rp_2_epa_end'])

    teams = {
        int(team['team']): {
            'epa': team['epa_end'],
            'rp1': team['rp_1_epa_end'],
            'rp2': team['rp_2_epa_end'],
        }
    for team in sb_teams}

    random_teams = [(int(team['team']), 0) for team in sb_teams]
    random.shuffle(random_teams)

    schedule = cheesy_schedule(len(teams), 12)
    print(schedule)

    year_info = sb.get_year(year=year)

    for match in schedule:
        red_teams = [random_teams[i-1] for i in match[:3]]
        blue_teams = [random_teams[i-1] for i in match[3:]]

        red_team_objs = [teams[team[0]] for team in red_teams]
        blue_team_objs = [teams[team[0]] for team in blue_teams]

        red_epa_sum = sum([team['epa'] for team in red_team_objs])
        blue_epa_sum = sum([team['epa'] for team in blue_team_objs])

        red_win_prob = 1 / (
            1 + 10 ** (-5 / 8 * (red_epa_sum - blue_epa_sum) / year_info['score_sd'])
        )

        red_rp1_prob = expit(sum(team['rp1'] for team in red_team_objs))
        blue_rp1_prob = expit(sum(team['rp1'] for team in blue_team_objs))
        red_rp2_prob = expit(sum(team['rp2'] for team in red_team_objs))
        blue_rp2_prob = expit(sum(team['rp2'] for team in blue_team_objs))

        red_win = random.random() < red_win_prob

        red_rps = (2 if red_win else 0) + (1 if random.random() < red_rp1_prob else 0) + (1 if random.random() < red_rp2_prob else 0)
        blue_rps = (2 if not red_win else 0) + (1 if random.random() < blue_rp1_prob else 0) + (1 if random.random() < blue_rp2_prob else 0)

        print([team[0] for team in red_teams], [team[0] for team in blue_teams])
        print(red_epa_sum, blue_epa_sum)
        print([red_rp1_prob, red_rp2_prob], [blue_rp1_prob, blue_rp2_prob])

        print(red_win)

        print(red_rps, blue_rps)


        for i in match[:3]:
            i -= 1
            random_teams[i] = (random_teams[i][0], random_teams[i][1] + red_rps)

        for i in match[3:]:
            i -= 1
            random_teams[i] = (random_teams[i][0], random_teams[i][1] + blue_rps)

    random_teams.sort(key=lambda team: -team[1])

    pp(random_teams)
    
event_simulation("WASNO", 2024)
