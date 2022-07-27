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

      with open(str(pathlib.Path(__file__).parent.resolve()) + '/reports/war_preparation.txt', mode = 'r') as prep_file:
        prep_report = prep_file.read()

      print(prep_report.format(clan = cw.clan.name, remaining_hours = utils.reports.remaining_time_str(start_time)))
    elif isinstance(cw, currentwar_inwar.Root):
      end_time = utils.reports.remaining_local_time(cw.endTime)

      with open(str(pathlib.Path(__file__).parent.resolve()) + '/reports/war_inwar.txt', mode = 'r') as inwar_file:
        inwar_report = inwar_file.read()

      print(inwar_report.format(clan = cw.clan.name, remaining_hours = utils.reports.remaining_time_str(end_time), remaining_attacks = utils.reports.remaining_attacks_bymember_str(cw.clan.members, cw.attacksPerMember)))
  except Exception as e:
    print(str(e))
    exit()

run()