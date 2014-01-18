'''
    Base

    Curr reference:
    http://docs.python.org/release/2.5.2/lib/socket-example.html
'''

import socket

HOST = 'protos.homenet.org' 
PORT = 50007 # arbitrary port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
