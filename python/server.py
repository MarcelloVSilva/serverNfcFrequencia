#!/usr/bin/python
# -*- coding: utf-8 -*-

import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("172.16.118.97", 1235))
print "Server conectado a porta 1235..."

def getDadosTeacher():
    print "passou aqui"
    return 1

server.register_function(getDadosTeacher, "getDadosTeacher")
server.serve_forever()
