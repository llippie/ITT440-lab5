import socket
import sys
import json

s = socket.socket()
ip = '192.168.56.101'
port = 8080
fileName = input("File to store: ")
file = open(fileName,"r")
sendData = json.dumps(fileName+"\n"+file.read())

s.connect((ip, port))
s.sendall(bytes(sendData,encoding="utf-8"))

data = s.recv(1024)
print(data)

s.close()
file.close()
