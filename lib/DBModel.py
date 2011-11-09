#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Classes to manage the Databases """

from elixir import *

#metadata.bind = "postgres://postgres:carpan@localhost:5432/pyadminstocks"
metadata.bind = "sqlite:///database/pyAdminStocks_database.sqlite"
#metadata.bind.echo = True

class my_stocks(Entity):
    using_options(tablename="my_stocks")
    stock_id=Field(Integer,autoincrement=True,primary_key=True)
    stock_symbol=Field(Unicode,required=True)
    stock_date=Field(DateTime)
    stock_amount=Field(Integer)
    stock_price=Field(Integer)
    stock_last_price=Field(Integer)
    stock_commission=Field(Integer)
    stock_gain=Field(Integer)
    stock_half_profit=Field(Integer)
    stock_who=ManyToOne('profiles')
    stock_follow=ManyToOne('follow_stocks')

class follow_stocks(Entity):
    using_options(tablename="follow_stocks")
    stock_symbol=Field(Unicode,required=True)
    stock_open=Field(Integer)
    stock_datetime=Field(DateTime)
    stock_max=Field(Integer)
    stock_min=Field(Integer)
    stock_value=Field(Integer)
    stock_var=Field(Integer)
    stock_vol=Field(Integer)
    stock_half_profit=Field(Integer)
    stock_my=OneToMany('my_stocks')
    
class profiles(Entity):
    using_options(tablename="profiles")
    profile_id=Field(Integer,required=True)
    profile_name=Field(Unicode,required=True)
    profile_email=Field(Unicode)
    profile_passwd=Field(Unicode,required=True)
    profile_last_access=Field(DateTime)
    profile_login=Field(Integer)
    stocks=OneToMany('my_stocks')

class shells_stocks(Entity):
    using_options(tablename="shells_stocks")
    id=Field(Integer,autoincrement=True,primary_key=True)
    symbol=Field(Unicode,required=True)
    date=Field(DateTime)
    buy_price=Field(Integer)
    amount=Field(Integer)
    price_per_stock=Field(Integer)
    price_per_all=Field(Integer)
    buy_commission=Field(Integer)
    shell_commission=Field(Integer)
    gain=Field(Integer)
    half_profit=Field(Integer)
    who=ManyToOne('profiles')
