import requests
import json

headers = {"TRN-Api-Key" : "6959575d-9a4a-438b-b9cd-185f579967bf"}
response = requests.get("https://api.fortnitetracker.com/v1/profile/pc/xlco", headers=headers)

print(response.content)

data = response.json()

for item in data:
    print(item)


print(data['epicUserHandle'])