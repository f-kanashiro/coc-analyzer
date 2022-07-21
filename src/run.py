import api.supercell.clans as clans
import utils.reports as reports
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
      remaining_time = (start_time - timedelta(hours = 3)) - datetime.now()
    elif isinstance(cw, currentwar_inwar.Root):
      endtime = datetime.strptime(cw.endTime, "%Y%m%dT%H%M%S.%fZ")
      remaining_time = (endtime - timedelta(hours = 3)) - datetime.now()

    r = open(str(pathlib.Path(__file__).parent.resolve()) + '/reports/war_preparation.txt', 'r').read()
    
    print(r.format(clan = cw.clan.name, remaining_hours = reports.remaining_time_str(remaining_time)))
  except Exception as e:
    print(str(e))
    exit()

run()