#!/usr/bin/env python
#-*- coding: utf-8 -*-
from DBModel import *

setup_all()
create_all()

class Administrator():
    def identify_table(self, wtable):
        if wtable == 'servers':
            table = Servers()
        elif wtable == 'profiles':
            table = Profiles()
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
        if wtable == 'servers':
            return Servers.query.all()
        elif wtable == 'profiles':
            return Profiles.query.all()
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
        if wtable == "server_id":
            return Servers.get_by(id=value)
        elif wtable == "server_addr":
            return Servers.get_by(add=value.decode())
        elif wtable == "server_who":
            return Servers.query.filter_by(profile=value).all()
        elif wtable == "profile":
            return Profiles.get_by(profile=value.decode())
        else:
            return None

    def like_servers(self, user_id, table_filter=None, value=None, asdict=False):
        profile = self.search_table("profile", user_id)
        if not profile:
            print ('Debe especificar un user_id valido.')
            return False
        else:
            if table_filter and value:
                servers = self.like_table(table_filter, value)
                if asdict:
                    return [i.to_dict() for i in servers]
                else:
                    return servers
            else:
                return False

    def get_profile_servers(self, user_id, asdict=True):
        profile = self.search_table("profile", user_id)
        if not profile:
            print ('Debe especificar un user_id valido.')
            return False
        else:
            servers = self.search_table("server_who", profile)
            if asdict:
                return dict((i.id,i.to_dict()) for i in servers)
            else:
                return servers

    def get_server_info(self, server, asdict=True):
        res = self.search_table('server_id', server)
        if asdict:
            return res.to_dict()
        return res
