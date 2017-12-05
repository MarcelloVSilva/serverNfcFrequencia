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

host = "localhost" # socket.gethostbyname(socket.gethostname())
server = SimpleXMLRPCServer((host, 2000))
print host, "Server conectado a porta 2000..."

def getInfoTeacher(idTeacher):
    print idTeacher
    return jsonTeacher


def sendFreqList(listFreq):
    print listFreq
    return "Frequência realizada"

server.register_function(getInfoTeacher, "getInfoTeacher")
server.register_function(sendFreqList, "sendFreqList")

server.serve_forever()