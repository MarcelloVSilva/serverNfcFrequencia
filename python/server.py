#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    host = socket.gethostbyname(socket.gethostname())
    port = int(os.environ.get("PORT", 2000))
    app.run(host=host, port=port)

#
#import socket
#import xmlrpclib
#from SimpleXMLRPCServer import SimpleXMLRPCServer
#
#host = socket.gethostbyname(socket.gethostname())
#server = SimpleXMLRPCServer((host, 2000))
#print host, "Server conectado a porta 2000..."
#
#def getDadosTeacher():
#    print ("passou aqui")
#    return 1
#
#server.register_function(getDadosTeacher, "getDadosTeacher")
#server.serve_forever()
#