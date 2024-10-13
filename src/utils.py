import math
from scipy.special import erfinv # type: ignore

def rank_to_district_points(R: int, N: int) -> int:
    a = 1.07
    first = erfinv((N-2*R+2)/(a*N))
    second = 10/erfinv(1/a)
    return math.ceil(first*second+12)
