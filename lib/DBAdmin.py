#!/usr/bin/env python
#-*- coding: utf-8 -*-
from DBModel import *

setup_all()
create_all()

class Administrator():
    def identify_table(self, wtable):
        if wtable == 'Profiles':
            table = Profiles()
        elif wtable == 'MyStocks':
            table = MyStocks()
        elif wtable == 'FollowStocks':
            table = FollowStocks()
        elif wtable == 'HistoryStocks':
            table = HistoryStocks()
        else:
            print ('La tabla donde desea insertar no existe.')
            table = None
        return table

    def insert_dict(self, wtable, listdict):
        table = self.identify_table(wtable)
        if table:
            result = [table.from_dict(i) for i in listdict]
            session.commit()
            return result
        else:
            return False

    def delete(self, listquery):
        result = [i.delete() for i in listquery]
        session.commit()
        return result
    
    def update(self, listquery, dic):
        result = [i.from_dict(dic) for i in listquery]
        session.commit()
        return result

class Querys():
    def identify_table(self, wtable):
        if wtable == 'Profiles':
            return Profiles.query.all()
        elif wtable == 'MyStocks':
            return MyStocks.query.all()
        elif wtable == 'FollowStocks':
            return FollowStocks.query.all()
        elif wtable == 'HistoryStocks':
            return HistoryStocks.query.all()
        else:
            print ('La tabla donde obtener la consulta no existe.')
            return False

    def all_table(self, wtable, flag=False):
        table = self.identify_table(wtable)
        if flag:
            dic = {}
            counter = 0
            for i in table:
                dic[counter] = i.to_dict()
                counter += 1
            return dic
        else:
            return table

    def like_table(self, wtable, value):
        value = "%" + value + "%"
        if wtable == "host":
            query_filter = Servers.host.like(value.decode())
            return Servers.query.filter(query_filter).all()
        elif wtable == "addr":
            query_filter = Servers.addr.like(value.decode())
            return Servers.query.filter(query_filter).all()
        elif wtable == "system":
            query_filter = Servers.system.like(value.decode())
            return Servers.query.filter(query_filter).all()
        elif wtable == "comment":
            query_filter = Servers.comment.like(value.decode())
            return Servers.query.filter(query_filter).all()
        else:
            return None

    def search_table(self, wtable, value):
        if wtable == 'Profiles':
            return Profiles.get_by(profile=value.decode())
        elif wtable == 'MyStocks':
            return MyStocks.query.filter_by(profile=value).all()
        elif wtable == 'MyFollowStocks':
            query_filter = Profiles.profile.like(value.profile)
            return FollowStocks.query.filter(query_filter).all()
        elif wtable == 'MyHistoryStocks':
            query_filter = Profiles.profile.like(value.profile)
            return HistoryStocks.query.filter(query_filter).all()
        else:
            return None

    def get_profile(self, user_id, relationship=[], asdict=True):
        profile = self.search_table("Profiles", user_id)
        if not profile:
            print ('Debe especificar un user_id valido.')
            return False
        else:
            attr = dict((i, self.search_table(i, profile)) for i in relationship)
            if asdict:
                for i in attr:
                    attr[i] = [x.to_dict() for x in attr[i] if x != None]
            print attr

