#!/usr/bin/env python

import urllib2

url = "http://ar.finance.yahoo.com/d/quotes.csv?s=TS.BA&f=sl1d1t1c1ohgv&e=.csv"
file_url = urllib2.urlopen(url)

