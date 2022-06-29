import api.supercell.clans as clans
import json
import pytz
from datetime import datetime

from models import currentwar_inwar, currentwar_preparation

def getCW_Obj(_cwjson):
  cw = json.loads(_cwjson)
  
  if cw['state'] == 'preparation':
    return currentwar_preparation.Root.from_dict(cw)
  elif cw['state'] == 'inWar':
    return currentwar_inwar.Root.from_dict(cw)

currentWar = clans.get_currentwar()

if currentWar.status_code == 200:
  _cw = getCW_Obj(currentWar.text)

  if isinstance(_cw, currentwar_preparation.Root):
    _starttime = datetime.strptime(_cw.startTime, "%Y%m%dT%H%M%S.%fZ")

  elif isinstance(_cw, currentwar_inwar.Root):
    _starttime =  datetime.strptime(_cw.startTime, "%Y%m%dT%H%M%S.%fZ")
    _starttime = _starttime.astimezone(pytz.timezone('America/Sao_Paulo'))

    _endtime = datetime.strptime(_cw.endTime, "%Y%m%dT%H%M%S.%fZ")
    _endtime = _endtime.astimezone(pytz.timezone('America/Sao_Paulo'))

    print(_endtime)
else:
  print(currentWar.text + str(currentWar.status_code))