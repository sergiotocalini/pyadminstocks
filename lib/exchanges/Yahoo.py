#!/usr/bin/env python
import re
import urllib2
from DateTime import DateTime
from datetime import datetime

class YahooAdmin():
    def get_stock(self, stock='@^merv', country='ar', delimiter=','):
        url = 'http://%s.finance.yahoo.com' %(country)
        url += '/d/quotes.csv?s=%s&f=sl1d1t1c1ohgv&e=.csv' %(stock)
        
        results = {}
        
        response = urllib2.urlopen(url)
        for line in response.readlines():
            line = re.sub(r'^\s+$|\n', '', line)
            if line <> '':
                line = line.strip()
                line = line.replace('"', '')
                values = line.split(delimiter)

                dict_stock = {'stock':values[0], 'value':values[1],
                              'datetime':' '.join(values[2:4]), 'var':values[4],
                              'open':values[5], 'max':values[6],
                              'min':values[7], 'vol':values[8]}
                results[values[0]] = dict_stock
        return results

    def get_exchange(self, exchange='ARSUSD', country='ar', delimiter=','):
        url = 'http://%s.finance.yahoo.com/' %(country)
        url += 'd/quotes.csv?s=%s=X&f=sl1d1t1c1ohgv&e=.csv' %(exchange)

        results = {}

        response = urllib2.urlopen(url)
        for line in response.readlines():
            line = re.sub(r'^\s+$|\n', '', line)
            if line <> "":
                line = line.strip()
                line = line.replace('"', '')
                values = line.split(delimiter)
                
                dict_file={'currency':values[0][3:6],
                           'processing':values[0][0:3],
                           'price':values[1], 'value':1,
                           'datetime':' '.join(values[2:4])}
                results[values[0][0:6]] = dict_file
        return results

