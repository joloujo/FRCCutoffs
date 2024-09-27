import os
from dotenv import load_dotenv
import requests

load_dotenv()

class TBA_API_Interface():
    def __init__(self) -> None:
        pass

    def request(self, endpoint: str = '', headers: dict[str, str] = {}):

        url = "https://www.thebluealliance.com/api/v3" + endpoint
        headers = {'X-TBA-Auth-Key': os.environ['X-TBA-Auth-Key']} | headers

        response = requests.get(url, headers=headers, data={})

        return response.json()
