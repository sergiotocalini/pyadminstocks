#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from configobj import ConfigObj
from lib.Path import HOME_PATH, DB_CONFIG, DB_FILE

class DBConf():
    def _get_configFile(self):
        if os.path.isfile(DB_CONFIG):
            config = ConfigObj(DB_CONFIG)
        else:
            self.write()
            config = ConfigObj(DB_CONFIG)
        return config

    def write(self, engine='sqlite', host='',
              port=5432, db='', user='', passwd=''):
        config = ConfigObj()
        config.filename = DB_CONFIG
        config['DAEMON'] = {}
        config['DAEMON']['engine'] = engine
        config['SERVER'] = {}
        config['SERVER']['host'] = host
        config['SERVER']['port'] = port
        config['SERVER']['db'] = db
        config['AUTH'] = {}
        config['AUTH']['user'] = user
        config['AUTH']['password'] = passwd
        config.write()

    def modify(self, fields=None):
        config = self._get_configFile()
        for i in fields:
            for x in fields[i]:
                config[i][x] = fields[i][x]
        config.write()

    def read(self):
        config = self._get_configFile()
        database = {'daemon':config['DAEMON']['engine'],
                    'host':config['SERVER']['host'],
                    'port':config['SERVER']['port'],
                    'db':config['SERVER']['db'],
                    'user':config['AUTH']['user'],
                    'password':config['AUTH']['password']}        
        return database

    def load(self):
        config = self._get_configFile()
        if config['DAEMON']['engine'] == 'sqlite':
            db_config = 'sqlite:///%s' %(DB_FILE)
        elif config['DAEMON']['engine'] == 'postgresql':
            db_config = 'postgres://'
            db_config += '%(user)s:%(password)s@' %(config['AUTH'])
            db_config += '%(host)s:%(port)s/%(db)s' %(config['SERVER'])
        elif config['DAEMON']['engine'] == 'mysql':
            db_config = 'mysql://'
            db_config += '%(user)s:%(password)s@' %(config['AUTH'])
            db_config += '%(host)s:%(port)s/%(db)s' %(config['SERVER'])
        return db_config
