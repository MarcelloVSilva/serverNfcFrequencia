#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import json

jsonTeacher = json.dumps(
    {
        'teacher':{
            'idTeacher': 'marcelloId',
            'nameTeacher': 'Marcello Victor',
            'classrooms':[
                {
                    'id': 'sistemasDistribuidos2M23',
                    'description': 'Sistemas distribuidos',
                    'polygon': {}
                }
            ]
        }
    }, separators=(',',':'))
print jsonTeacher

host = "172.16.118.97" # socket.gethostbyname(socket.gethostname())
server = SimpleXMLRPCServer((host, 2000))
print host, "Server conectado a porta 2000..."

def getInfoTeacher(idTeacher):
    print idTeacher
    return jsonTeacher

server.register_function(getInfoTeacher, "getInfoTeacher")
server.serve_forever()




                # ['-16.604074', '-49.264518'],
                # ['-16.604206', '-49.264484'],
                # ['-16.604320', '-49.264900'],
                # ['-16.604183', '-49.264949'],