import requests
import config

def get_currentwar():
    url = "https://api.clashofclans.com/v1/clans/" + config.getClanTag() + "/currentwar"

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    return requests.request("GET", url, headers=headers, data=payload)

def get_warleague(_wartag):
    url = "https://api.clashofclans.com/v1/clanwarleagues/wars/" + _wartag

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    return requests.request("GET", url, headers=headers, data=payload)