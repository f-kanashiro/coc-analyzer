from datetime import datetime, timedelta
from math import floor

def remaining_time_str(rt):
    minutes = floor(rt.total_seconds() / 60)
    hours = (floor(rt.total_seconds() / 60 / 60))

    if (hours == 0):
        return str(minutes) + " minutos"
    else:
        return str(hours) + " horas e " + str(minutes) + " minutos"