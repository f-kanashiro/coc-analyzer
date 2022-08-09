from inspect import trace
import requests
import config
import json
import traceback
from models import currentwar_inwar, currentwar_preparation, leaguegroup

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
      raise Exception("Request error\nURL=" + url + "\n" + str(rq.status_code) + " - " + rq.text)
  except Exception as e:
      raise Exception("Request error\nURL=" + url + "\n" + str(e))

def getCW_obj(cwjson):
  try:
    cw = json.loads(cwjson)
    
    if cw['state'] == 'preparation':
      return currentwar_preparation.Root.from_dict(cw)
    elif cw['state'] == 'inWar':
      return currentwar_inwar.Root.from_dict(cw)
      #TODO create warEnded model
    elif cw['state'] == 'warEnded': #'warEnded' state have the same data type of 'inWar' state
      return currentwar_inwar.Root.from_dict(cw)
    elif cw['state'] == 'notInWar':
      raise Exception("Not in War")
    else:
      raise Exception("Invalid state")
  except Exception as e:
    raise Exception("getCW_obj(cwjson): " + str(e))      

def get_warleague(_wartag):
  url = "https://api.clashofclans.com/v1/clanwarleagues/wars/" + _wartag

  payload = ""
  headers = {
      'Authorization': config.getBearerToken()
  }

  return requests.request("GET", url, headers=headers, data=payload)

def get_leaguegroup():
  try:
    url = "https://api.clashofclans.com/v1/clans/" + config.getClanTag() + "/currentwar/leaguegroup"

    payload = ""
    headers = {
        'Authorization': config.getBearerToken()
    }

    rq = requests.request("GET", url, headers=headers, data=payload)
    
    if(rq.status_code == 200):
      return get_groupleague_obj(rq.text)
    else:
      raise Exception("Request error\nURL=" + url + "\n" + str(rq.status_code) + " - " + rq.text)
  except Exception as e:
      raise Exception(str(e))

def get_groupleague_obj(cljson):
  try:
    cl = json.loads(cljson)

    return leaguegroup.Root.from_dict(cl)
  except:
    raise Exception(traceback.print_exc())      