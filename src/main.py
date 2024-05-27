import statbotics
from dotenv import load_dotenv
import os
import requests

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
