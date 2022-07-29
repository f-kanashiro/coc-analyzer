from datetime import datetime, timedelta
from math import floor

# Receives datetime from json and returns de remaining time at local timezone
def remaining_local_time(t):
    rt = datetime.strptime(t, "%Y%m%dT%H%M%S.%fZ")
    return (rt - timedelta(hours = 3)) - datetime.now()

def remaining_time_str(rt):
    minutes = floor((rt.total_seconds() // 60) % 60)
    hours = floor(rt.total_seconds() / 60 / 60)

    if hours == 0:
        return str(minutes) + " minutos"
    else:
        if hours == 1:
            return str(hours) + " hora e " + str(minutes) + " minutos"
        else:
            return str(hours) + " horas e " + str(minutes) + " minutos"

def remaining_attacks_bymember_str(members, attacksPerMember):
    #get members with remaining attacks to do
    members = [m for m in members if len(m.attacks) < attacksPerMember]

    attacks_str = ""

    for m in members:
        attacks_str += m.name + " - " + str(attacksPerMember - len(m.attacks)) + " ataques restantes\n"

    return attacks_str[:-1]