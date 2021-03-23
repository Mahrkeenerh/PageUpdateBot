import requests, winsound, webbrowser, json
from time import sleep

with open('config.txt') as file:
    json_data = json.load(file)
    url = json_data['url']
    frequency = json_data['update_frequency']

old_request = requests.get(url=url)
new_request = old_request

# while old_request.content == new_request.content:
while True:
    sleep(frequency)
    new_request = requests.get(url=url)
    if new_request.status_code != 200:
        print(new_request.status_code)

webbrowser.open(url)

while True:
    winsound.Beep(750, 750)
    sleep(0.1)
