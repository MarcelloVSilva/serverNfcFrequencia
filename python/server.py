#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
import json

jsonTeacher = json.dumps(
    {
        'idTeacher': 'marcelloId',
        'nameTeacher': 'Marcello Victor',
        'classrooms':[
            {
                'id': 'sistemasDistribuidos2M23',
                'description': 'Sistemas distribuidos terça',
                'polygon': [
                    [-16.705828, -49.297773],
                    [-16.705869, -49.297206],
                    [-16.706805, -49.297450],
                    [-16.706676, -49.297988]
                ]
            },
            {
                'id': 'sistemasDistribuidos6M23',
                'description': 'Sistemas distribuidos sexta',
                'polygon': []
            }
        ]
    
    }, separators=(',',':'))
print jsonTeacher

host = "192.168.15.24" # 192.168.6.72(inf) /192.168.15.24 (trabalho) / 192.168.0.19 (casa)  socket.gethostbyname(socket.gethostname())
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