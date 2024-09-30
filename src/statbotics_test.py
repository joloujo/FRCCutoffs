from statbotics.main import Statbotics
from pprint import pp

sb = Statbotics()

# teams = sb.get_teams(district='PNW')
# pp(teams[0])

# print("-"*10)
# pp(sb.get_team_events(team=2412, year=2024))
print("-"*10)
# pp(sb.get_team_years(year=2024, district='PNW', fields=['team', 'epa_end', 'rp_1_epa_end', 'rp_2_epa_end']))
pp(sb.get_team_events(event='2024wasno'))
print("-"*10)
