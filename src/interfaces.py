class Team():
    number: int
    total_epa: float
    rp1_epa: float
    rp2_epa: float

    def __init__(self, team: int, total_epa: float = 0, rp1_epa: float = 0, rp2_epa: float = 0) -> None:
        self.number = team
        self.total_epa = total_epa
        self.rp1_epa = rp1_epa
        self.rp2_epa = rp2_epa

    def __str__(self) -> str:
        return 'Team {}: {:.2f}, {:.2f}, {:.2f}'.format(self.number, self.total_epa, self.rp1_epa, self.rp2_epa)

class EventInfo():
    teams: dict[int, Team]
    schedule: list[list[int]]

    def __init__(self, teams: list[Team], schedule: list[list[int]]) -> None:
        self.teams = {}
        for team in teams:
            self.teams[team.number] = team

        self.schedule = schedule
    
    def __str__(self) -> str:
        return (' ' * 4 + '\n').join([str(team) for team in self.teams])
