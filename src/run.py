import api.supercell.clans as clans
import api.telegram.telegram_messages as telegram_messages
import json
import pytz
import pathlib
from datetime import datetime, timedelta
from utils import formatting, reports

from models import currentwar_inwar, currentwar_preparation

def localtest():
  return True

def run():
  try:
    if localtest():
      with open(str(pathlib.Path(__file__).parent.resolve()) + '/examples/currentwar_inwar.json', mode = 'r') as f:
        cw = clans.getCW_obj(f.read())
    else:
      #First 9 days of month may occurs CWL
      if 1 <= datetime.now().day <= 9:
        lg = clans.get_leaguegroup()
        print(lg)
        exit()
      else:
        cw = clans.get_currentwar()

    if isinstance(cw, currentwar_preparation.Root):    
      start_time = formatting.remaining_local_time(cw.startTime)

      with open(str(pathlib.Path(__file__).parent.resolve()) + '/reports/war_preparation.txt', mode = 'r') as prep_file:
        prep_report = prep_file.read()

      telegram_messages.war_status(prep_report.format(clan = cw.clan.name, remaining_hours = formatting.remaining_time_str(start_time)))
    elif isinstance(cw, currentwar_inwar.Root):
      end_time = formatting.remaining_local_time(cw.endTime)
      reports.inwar(
          report_file = str(pathlib.Path(__file__).parent.resolve()) + '/reports/war_inwar.txt'
        , clan = cw.clan.name
        , remaining_hours = formatting.remaining_time_str(end_time)
        , remaining_attacks = formatting.remaining_attacks_bymember_str(cw.clan.members, cw.attacksPerMember)
      ).send()
  except Exception as e:
    print(str(e))
    exit()

run()