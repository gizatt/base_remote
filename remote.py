'''
    Remote

    Curr reference:
    http://docs.python.org/release/2.5.2/lib/socket-example.html
'''

import socket

HOST = ''  # localhost since this functions as server
PORT = 50007 # arbitrary port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print "Conencted by", addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.send(data)
conn.close()
