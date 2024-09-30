from simulation import get_event_info, event_simulation
from interfaces import EventInfo
from pprint import pp
from time import time
from statbotics.main import Statbotics

N = 10000
EVENT_CODE = 'WASNO'
YEAR = 2024

sb = Statbotics()

start: float = time()
eventInfo: EventInfo = get_event_info('PNCMP', YEAR)

done_fetching: float = time()
print(f'Fetched in {done_fetching - start} seconds')

score_sd = sb.get_year(year=YEAR)['score_sd']

rp_lists: dict[int, list[int]] = {team: [] for team in eventInfo.teams}

for i in range(0, N):
    event_results: dict[int, int] = event_simulation(eventInfo, score_sd)
    for team in event_results:
        rp_lists[team].append(event_results[team])

done_simulating: float = time()
print(f'Simulated in {done_simulating - done_fetching} seconds ({(done_simulating - done_fetching) / N} seconds average)')

average_rps: dict[int, float] = {team: 0.0 for team in eventInfo.teams}
for team in rp_lists:
    average_rps[team] = sum(rp_lists[team]) / N

pairs = [(team, average_rps[team]) for team in average_rps]
pairs.sort(key=lambda pair: -pair[1])

for i, pair in enumerate(pairs):
    print('| {:>2} | {:>5} | {:>5.2f} '.format(i+1, pair[0], pair[1]))