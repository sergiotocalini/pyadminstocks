#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from decimal import Decimal
from pony.orm import *

db = Database()

class Profile(db.Entity):
    _table_ = "profiles"
    id = PrimaryKey(int, auto=True)
    alias = Required(unicode, unique=True)
    passwd = Required(unicode)
    name = Optional(unicode, nullable=True)
    email = Optional(unicode, unique=True)
    follow_stocks = Set("Stock")
    portfolios = Set("Portfolio")
    
class Stock(db.Entity):
    _table_ = "stocks"
    id = PrimaryKey(int, auto=True)
    symbol = Required(unicode, unique=True)
    volume = Optional(Decimal)
    value = Optional(Decimal)
    value_max = Optional(Decimal)
    value_min = Optional(Decimal)
    value_last = Optional(Decimal)
    variation = Optional(Decimal)
    updated_on = Optional(datetime)
    operation = Optional("Operation")
    profiles = Set(Profile)
    portfolios = Set("Portfolio")
    
class Portfolio(db.Entity):
    _table_ = "portfolios"
    id = PrimaryKey(int, auto=True)
    profile = Required(Profile)
    stock = Required(Stock)
    amount = Required(int)
    operations = Set("Operation")
    gain = Optional(Decimal)
    half_profit = Optional(Decimal)
    
class Operation(db.Entity):
    _table_ = "operations"
    id = PrimaryKey(int, auto=True)
    date = Optional(datetime)
    commission = Optional(Decimal)
    price = Optional(Decimal)
    type = Required(unicode)
    portfolio = Set(Portfolio)
    stock = Required(Stock)
    
