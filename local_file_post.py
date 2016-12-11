import requests

auth_headers = {
    'app_id': 'your_app_id',
    'app_key': 'your_app_key'
}

url = 'https://api.kairos.com/v2/media'
files = {
    'source': open('media/test.jpg')
}
data = {
    'timeout': 60
}
response = requests.post(url, files=files, data=data, headers=auth_headers)

print response.json()