import requests
import math
from scipy.special import erfinv

def rank_to_district_points(R: int, N: int) -> int:
    a = 1.07
    first = erfinv((N-2*R+2)/(a*N))
    second = 10/erfinv(1/a)
    return math.ceil(first*second+12)

# Modified from statbotics to return a list of lists of ints
def cheesy_schedule(num_teams: int, matches_per_team: int) -> list[list[int]]:
    data = requests.get(
        f"https://raw.githubusercontent.com/Team254/cheesy-arena/main/schedules/{num_teams}_{matches_per_team}.csv"
    )
    lines = data.text.split("\n")
    lines = [[int(x) for x in line.split(",")[::2]] for line in lines[:-1]]
    return lines
