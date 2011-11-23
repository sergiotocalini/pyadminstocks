#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Classes to manage the Databases """
from elixir import *
from DBConfig import DBConf

class Profiles(Entity):
    using_options(tablename = 'Profiles')
    profile = Field(Integer, required = True)
    passwd = Field(Unicode, required = True)
    fullname = Field(Unicode)
    email = Field(Unicode)
    last_access = Field(DateTime)
    stocks = OneToMany('MyStocks')
    following = ManyToMany('FollowStocks')
    history = ManyToMany('HistoryStocks')

class MyStocks(Entity):
    using_options(tablename = 'MyStocks')
    stock = Field(Unicode, required = True)
    amount = Field(Integer)
    commission = Field(Integer)
    date = Field(DateTime)
    gain = Field(Integer)
    half_profit = Field(Integer)
    last_price = Field(Integer)
    price = Field(Integer)
    profile = ManyToOne('Profiles')

class FollowStocks(Entity):
    using_options(tablename = 'FollowStocks')
    stock = Field(Unicode, required = True, unique = True)
    date = Field(DateTime)
    half_profit = Field(Integer)
    maximum = Field(Integer)
    minimum = Field(Integer)
    opening = Field(Integer)
    value = Field(Integer)
    variation = Field(Integer)
    volume = Field(Integer)
    profiles = ManyToMany('Profiles')
    
class HistoryStocks(Entity):
    using_options(tablename = 'HistoryStocks')
    symbol = Field(Unicode, required = True)
    amount = Field(Integer)
    buy_commission = Field(Integer)
    buy_date = Field(DateTime)
    buy_price = Field(Integer)
    shell_commission = Field(Integer)
    shell_date = Field(DateTime)
    shell_price = Field(Integer)
    gain = Field(Integer)
    half_profit = Field(Integer)
    profile = ManyToMany('Profiles')

metadata.bind = DBConf().load()
#metadata.bind.echo  =  True
