from API import API
import requests
import random

class Cheesy_API(API):
    @classmethod
    def dir(cls, endpoint: str) -> str:
        return "./cache/cheesy_schedules/" + endpoint
    
    @classmethod
    def url(cls, endpoint: str) -> str:
        return "https://raw.githubusercontent.com/Team254/cheesy-arena/main/schedules/" + endpoint
        
    @classmethod
    def get(cls, endpoint: str | tuple[int, int]) -> list[list[int]]:

        if isinstance(endpoint, tuple):
            endpoint = cls.endpoint(endpoint[0], endpoint[1])

        schedule = cls.load(endpoint)

        if schedule != None:
            return schedule

        data = requests.get(
            cls.url(endpoint)
        )
        schedule = [[int(x)-1 for x in line.split(",")[::2]] for line in data.text.split("\n")[:-1]]

        cls.cahce(endpoint, schedule)

        return schedule
    
    @classmethod
    def endpoint(cls, teams: int, mpt: int) -> str:
        return f'{teams}_{mpt}.csv'
    
    @classmethod
    def shuffled(cls, teams: int, mpt: int) -> list[list[int]]:
        unshuffled = cls.get(cls.endpoint(teams, mpt))

        shuffle = list(range(teams))
        random.shuffle(shuffle)

        return [[shuffle[team] for team in match] for match in unshuffled]



