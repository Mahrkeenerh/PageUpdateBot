import winsound, webbrowser, json, os
from time import sleep


try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

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

    if new_request.content != old_request.content:
        webbrowser.open(url)
        winsound.Beep(750, 750)
        sleep(0.1)
        winsound.Beep(750, 750)
        old_request = new_request
