import requests

url = "https://frc-api.firstinspires.org/v3.0/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
