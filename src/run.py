import api.supercell.clans as clans
import json
import pytz
import pathlib
from datetime import datetime, timedelta

from models import currentwar_inwar, currentwar_preparation

def localtest():
  return False

def run():
  try:
    if localtest():
      file = open(str(pathlib.Path(__file__).parent.resolve()) + '/examples/currentwar_preparation.json', 'r')
      cw = clans.getCW_obj(file.read())
    else:
      cw = clans.get_currentwar()

    if isinstance(cw, currentwar_preparation.Root):
      start_time = datetime.strptime(cw.startTime, "%Y%m%dT%H%M%S.%fZ")
      #_starttime = _starttime.astimezone(pytz.timezone('America/Sao_Paulo'))    

      remaining_time = (start_time - timedelta(hours = 3)) - datetime.now()
    elif isinstance(cw, currentwar_inwar.Root):
      endtime = datetime.strptime(cw.endTime, "%Y%m%dT%H%M%S.%fZ")
      #_endtime = _starttime.astimezone(pytz.timezone('America/Sao_Paulo'))

      remaining_time = (endtime - timedelta(hours = 3)) - datetime.now()    

    print(remaining_time)
  except Exception as e:
    print(str(e))
    exit()

run()