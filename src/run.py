import api.supercell.clans as clans
import json
import pytz
import pathlib
from datetime import datetime, timedelta

from models import currentwar_inwar, currentwar_preparation

def localtest():
  return False

def getCW_Obj(_cwjson):
  cw = json.loads(_cwjson)
  
  if cw['state'] == 'preparation':
    return currentwar_preparation.Root.from_dict(cw)
  elif cw['state'] == 'inWar':
    return currentwar_inwar.Root.from_dict(cw)

#currentWL = clans.get_currentwarLeague()

#print(currentWL.text + str(currentWL.status_code))

if localtest():
  file = open(str(pathlib.Path(__file__).parent.resolve()) + '/models/currentwar_preparation.json', 'r')
  _cw = getCW_Obj(file.read())
else:
  currentWar = clans.get_currentwar()

  if currentWar.status_code == 200:
    _cw = getCW_Obj(currentWar.text)
  else:
    print(currentWar.text + str(currentWar.status_code))
    exit()

if isinstance(_cw, currentwar_preparation.Root):
  _starttime = datetime.strptime(_cw.startTime, "%Y%m%dT%H%M%S.%fZ")
  _starttime = _starttime.astimezone(pytz.timezone('America/Sao_Paulo'))

  _endtime = datetime.strptime(_cw.endTime, "%Y%m%dT%H%M%S.%fZ")
  _endtime2 = _endtime.astimezone(pytz.timezone('America/Sao_Paulo'))
elif isinstance(_cw, currentwar_inwar.Root):
  _starttime =  datetime.strptime(_cw.startTime, "%Y%m%dT%H%M%S.%fZ")
  _starttime = _starttime.astimezone(pytz.timezone('America/Sao_Paulo'))

  _endtime = datetime.strptime(_cw.endTime, "%Y%m%dT%H%M%S.%fZ")
  _endtime2 = _endtime.astimezone(pytz.timezone('America/Sao_Paulo'))
else:
  print(currentWar.text + str(currentWar.status_code))

#_remainingTime = datetime.now() - _endtime

_endtime = _endtime - timedelta(hours = 3)

print(_endtime)