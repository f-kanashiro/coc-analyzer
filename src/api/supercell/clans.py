import requests
import config

def get_currentwar():
    url = "https://api.clashofclans.com/v1/clans/" + config.getClanTag() + "/currentwar"

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    return requests.request("GET", url, headers=headers, data=payload)

def get_currentwarLeague():
    url = "https://api.clashofclans.com/v1/clanwarleagues/wars/%232U2UR8920"

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    return requests.request("GET", url, headers=headers, data=payload)