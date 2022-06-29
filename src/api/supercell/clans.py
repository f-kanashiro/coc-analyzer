import requests
import config

def get_currentwar():
    url = "https://api.clashofclans.com/v1/clans/" + config.getClanTag() + "/currentwar"

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    return requests.request("GET", url, headers=headers, data=payload)