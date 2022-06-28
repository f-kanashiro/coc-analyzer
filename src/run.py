import config
import requests
import json
from models import currentwar_inwar, currentwar_preparation

def getCurrentWar(_cwjson):
  cw = json.loads(_cwjson)
  
  if cw['state'] == 'preparation':
    return currentwar_preparation.Root.from_dict(cw)
  elif cw['state'] == 'inWar':
    return currentwar_inwar.Root.from_dict(cw)

url = "https://api.clashofclans.com/v1/clans/" + config.getClanTag() + "/currentwar"

payload = ""
headers = {
  'Authorization': config.getBearerToken()
}

currentWarRq = requests.request("GET", url, headers=headers, data=payload)

if currentWarRq.status_code == 200:  
  cw = getCurrentWar(currentWarRq.text)
  print(cw)
else:
  print(currentWarRq.text + str(currentWarRq.status_code))