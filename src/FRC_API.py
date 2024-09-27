import base64
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class FRC_API_Interface():
    def __init__(self) -> None:
        token = f'{os.environ["FRC-API-Username"]}:{os.environ["FRC-API-Auth-Key"]}'
        self.credentials = base64.b64encode(bytes(token, 'utf-8')).decode("utf-8")

    def request(self, endpoint: str = '', headers: dict[str, str] = {}):

        url = "https://frc-api.firstinspires.org/v3.0/" + endpoint
        headers = {'Authorization': f'Basic {self.credentials}'} | headers

        response = requests.get(url, headers=headers, data={})

        return response
