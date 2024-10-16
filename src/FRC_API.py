import os
import base64
import requests
from typing import Any
from API import API
from dotenv import load_dotenv

load_dotenv()

class FRC_API_Interface():
    def __init__(self) -> None:
        token = f'{os.environ['FRC-API-Username']}:{os.environ['FRC-API-Auth-Key']}'
        self.credentials = base64.b64encode(bytes(token, 'utf-8')).decode("utf-8")

    def request(self, endpoint: str) -> Any:

        url: str = 'https://frc-api.firstinspires.org/v3.0/' + endpoint
        headers = {'Authorization': f'Basic {self.credentials}'}

        response: requests.Response = requests.get(url, headers=headers, data={})

        return response.json()

class FRC_API(API):
    @classmethod
    def dir(cls, endpoint: str) -> str:
        return './cache/FRC/' + endpoint + '.json'

    @classmethod
    def url(cls, endpoint: str) -> str:
        return 'https://frc-api.firstinspires.org/v3.0/' + endpoint

    @classmethod
    def get(cls, endpoint: str) -> dict[Any, Any]:
        return {}