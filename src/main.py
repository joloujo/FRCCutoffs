import statbotics
from dotenv import load_dotenv
import os
import requests
import pprint
import base64
import json

# Take environment variables from .env
load_dotenv()

# Test the Statbotics API
sb = statbotics.Statbotics()
print(sb.BASE_URL)

# Test the TBA API
TBA_headers = {'X-TBA-Auth-Key': os.environ['X-TBA-Auth-Key']}
TBA_base_URL = "https://www.thebluealliance.com/api/v3"
response = requests.get(TBA_base_URL + '/status', headers=TBA_headers)
print(response.json())

# Get the current districts from the FRC API
FRC_API_credentials = base64.b64encode(bytes(f'{os.environ["FRC-API-Username"]}:{os.environ["FRC-API-Token"]}', 'utf-8')).decode("utf-8")
FRC_API_headers = {'Authorization': f'Basic {FRC_API_credentials}'}
FRC_API_base_URL = "https://frc-api.firstinspires.org/v3.0/"
response = requests.get(FRC_API_base_URL + '2025/districts', headers=FRC_API_headers)
response_json = json.loads(response.text)
pprint.pp(response_json)
