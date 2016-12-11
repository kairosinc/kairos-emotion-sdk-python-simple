import requests

auth_headers = {
    'app_id': 'your_app_id',
    'app_key': 'your_app_key'
}

url = 'https://api.kairos.com/v2/media/5964b4443a32b319f98f6ce3'

response = requests.get(url, headers=auth_headers)

print response.json()