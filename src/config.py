import os
import configparser
from pathlib import Path

def getConfigValue(_section, _key):
    config = configparser.ConfigParser()
    dir = os.path.dirname(__file__)
    config.read(str(Path(dir).parent) + '/config.ini')
    return config[_section][_key]

def getBearerToken():    
    return 'Bearer ' + getConfigValue('coc-api', 'BearerToken')

def getClanTag():
    return getConfigValue('coc-api', 'ClanTag').replace('#', '%23')