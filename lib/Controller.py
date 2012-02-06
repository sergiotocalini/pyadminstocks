#!/usr/bin/env python
#-*- coding: utf-8 -*-
from DBAdmin import Querys, Administrator

class Profiles():
    def make(self, profile_dict={}):
        if profile_dict.has_key('profile'):
            profile = Querys().search_table("profiles", profile_dict['profile'])
            if profile:
                print ('El usuario ya existe en el sistema.')
                return False
            else:
                return Administrator().insert_dict("profiles", [profile_dict])
        else:
            return None

    def delete(self, id=None):
        if (not id):
            print ('Debe especificar el id.')
            return None
        else:
            profile = Querys().search_table("profiles", id)
            if profile:
                servers = Querys().search_table("server_who", profile)
                Administrator().delete(servers)
                Administrator().delete([profile])
                return True
            else:
                return False

    def modify(self, profile_dict={}):
        if profile_dict.has_key('profile'):
            profile = Querys().search_table("profiles", profile_dict['profile'])
            if profile:
                Administrator().update([profile], profile_dict)
                return True
            else:
                return False
        else:
            return None

class Stocks():
    def buy(self, profile, stocks=[]):
        print (profile, stocks)

    def shell(self, profile, stocks=[]):
        print (profile, stocks)
