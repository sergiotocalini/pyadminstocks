#!/usr/bin/env python
import os
import platform
import sys
from configobj import ConfigObj

APP_NAME = 'pyAdminStocks'
APP_VERSION = '9999'

def create_configFile(filename):
    config = ConfigObj()
    config.filename = filename
    config['themes'] = 'tango'
    config['fscreen'] = 'no'
    config['tabpos'] = 'POS_RIGHT'
    config.write()

def create_pluginFile(filename):
    config = ConfigObj()
    config.filename = filename
    config['SYSTEM_TRAY'] = {}
    config['NOTIFY'] = {}
    config['INFORMATION'] = {}
    config['OTHERS'] = {}
    config.write()

def _get_configFile(filename):
    if os.path.isfile(filename):
        config = ConfigObj(filename)
    else:
        create_configFile(filename)
        config = ConfigObj(filename)
    return config

def _get_pluginFile(filename):
    if os.path.isfile(filename):
        config = ConfigObj(filename)
    else:
        create_pluginFile(filename)
        config = ConfigObj(filename)
    return config

if platform.system() == 'Linux':
    APP_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
    if not (APP_PATH in sys.path):
        sys.path.insert(0, APP_PATH)

    USERNAME = os.environ['LOGNAME']

    HOME_PATH = os.environ['HOME']

    CONF_PATH = os.path.join(HOME_PATH, '.config/pyAdminStocks')
    if not (os.path.isdir(CONF_PATH)):
        os.system('mkdir -p %s' %(CONF_PATH))
        
    CONF_FILE = os.path.join(CONF_PATH, 'pyAeJokuaa.conf')

    PLUG_FILE = os.path.join(CONF_PATH, 'plugins.conf')

    PLUG_PATH_SYS = os.path.join(APP_PATH, 'plugins')
    PLUG_PATH_USER = os.path.join(HOME_PATH, '.local/share/pyAdminStocks/plugins')
    if not (os.path.isdir(PLUG_PATH_USER)):
        os.system('mkdir -p %s' %(PLUG_PATH_USER))
    PLUG_PATH = [PLUG_PATH_SYS, PLUG_PATH_USER]

    DB_CONFIG = os.path.join(CONF_PATH, 'database.conf')
    DB_FILE = os.path.join(CONF_PATH, 'database.sqlite')

    configFile = _get_configFile(CONF_FILE)
    THEME_PATH = os.path.join(APP_PATH, 'themes', configFile['themes'])
