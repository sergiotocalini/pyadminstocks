#!/usr/bin/env python
import requests
import csv

class Yahoo():
    def __init__(self):
        self.api = "http://finance.yahoo.com/d/quotes.csv"
        "YPFD.BA",337.00,"6/12/2015","4:59pm",-1.00,340.00,340.00,335.00,22398
    
    def get_stock(self, symbol, *args):
        headers = ['symbol', 'value', 'date', 'time',
                   'variaton', 'open', 'max', 'min', 'volume']
        ws = "%s?f=sl1d1t1c1ohgv&e=.csv&s=%s" %(self.api, symbol)
        res = csv.reader(requests.get(ws))
        output = []
        for line in res:
            parsed = {}
            count = 0
            for x in line:
                parsed[headers[count]] = x
                count+=1
            output.append(parsed)
        return output
        
        
