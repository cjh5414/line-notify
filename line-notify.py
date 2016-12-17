import sys
import requests

ACCESS_TOKEN = sys.argv[1]
MESSAGE = sys.argv[2]

URL = 'https://notify-api.line.me/api/notify'
MESSAGE_FIELD = {'message' : MESSAGE}
LINE_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + ACCESS_TOKEN
}

try:
    response = requests.post(
        url=URL,
        headers=LINE_HEADERS,
        data=MESSAGE_FIELD
    )
    print('Response HTTP Status Code: {status_code}'.format(
        status_code=response.status_code))
except requests.exceptions.RequestException:
    print('HTTP Request failed')

