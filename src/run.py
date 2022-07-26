import api.supercell.clans as clans
import utils.reports
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
      with open(str(pathlib.Path(__file__).parent.resolve()) + '/examples/currentwar_preparation.json', mode = 'r') as f:        
        cw = clans.getCW_obj(f.read())
    else:
      cw = clans.get_currentwar()

    if isinstance(cw, currentwar_preparation.Root):    
      start_time = utils.reports.remaining_local_time(cw.startTime)

      with open(str(pathlib.Path(__file__).parent.resolve()) + '/reports/war_preparation.txt', mode = 'r') as f:
        report = f.read()

      print(report.format(clan = cw.clan.name, remaining_hours = utils.reports.remaining_time_str(start_time)))
    elif isinstance(cw, currentwar_inwar.Root):
      end_time = utils.reports.get_remaining_local_time(cw.endTime)      
    
  except Exception as e:
    print(str(e))
    exit()

run()