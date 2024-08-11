import requests

def check_user(username):
    url = 'https://decapi.me/twitch/uptime/' + username
    r = requests.get(url)
    
    if ("offline" in requests.get(url).text):
        return False
    else: 
        return True