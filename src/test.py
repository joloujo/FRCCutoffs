import requests
import os
import base64
from dotenv import load_dotenv
import json

load_dotenv()

url = "https://frc-api.firstinspires.org/v3.0/2024"
token = f'{os.environ["FRC-API-Username"]}:{os.environ["FRC-API-Auth-Key"]}'
credentials = base64.b64encode(bytes(token, 'utf-8')).decode("utf-8")
headers = {'Authorization': f'Basic {credentials}'}

response = requests.request("GET", url, headers=headers)

print(response)
print(json.loads(response.text))
