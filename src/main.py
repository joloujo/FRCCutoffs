from updateTable import updateTable
from TBA_API import TBA_API_Interface
from random import randint

api = TBA_API_Interface()

status = api.request('/status')
# year = status['current_season']
year = status['max_season']


district_list = api.request(f'/districts/{year}') 

headers: list[str] = ["District", "DCMP 5%", "DCMP 50%", "DCMP 95%", "CMP 5%", "CMP 50%", "CMP 95%",]
data: list[list[str]] = [
    [
        f'{district["display_name"]} ({district["abbreviation"].upper()})', 
        str(randint(40, 60)),
        str(randint(40, 60)),
        str(randint(40, 60)),
        str(randint(40, 60)),
        str(randint(40, 60)),
        str(randint(40, 60)),
    ] 
    for district in district_list
]

updateTable(headers, data)