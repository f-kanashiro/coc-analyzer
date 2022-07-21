from inspect import trace
import requests
import config
import json
import traceback
from models import currentwar_inwar, currentwar_preparation

def getCW_obj(cwjson):
  try:
    cw = json.loads(cwjson)
    
    if cw['state'] == 'preparation':
      return currentwar_preparation.Root.from_dict(cw)
    elif cw['state'] == 'inWar':
      return currentwar_inwar.Root.from_dict(cw)
    else:
      raise Exception("Cannot deserialize JSON into object: Invalid state")
  except Exception as e:
    raise Exception("Cannot deserialize JSON into object: " + str(e))


def get_currentwar():
    try:
        url = "https://api.clashofclans.com/v1/clans/" + config.getClanTag() + "/currentwar"
    
        payload = ""
        headers = {
            'Authorization': config.getBearerToken()
        }
    
        rq = requests.request("GET", url, headers=headers, data=payload)
        if(rq.status_code == 200):
            return getCW_obj(rq.text)
        else:
            raise Exception("Request error\nURL=" + url + "\n" + rq.status_code + " - " + rq.text)
    except Exception as e:
        raise Exception("Request error\nURL=" + url + "\n" + str(e))

def get_warleague(_wartag):
    url = "https://api.clashofclans.com/v1/clanwarleagues/wars/" + _wartag

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    return requests.request("GET", url, headers=headers, data=payload)