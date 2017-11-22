#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

host = socket.gethostbyname(socket.gethostname())
server = SimpleXMLRPCServer((host, 1235))
print host, "Server conectado a porta 1235..."

def getDadosTeacher():
    print ("passou aqui")
    return 1

server.register_function(getDadosTeacher, "getDadosTeacher")
server.serve_forever()
