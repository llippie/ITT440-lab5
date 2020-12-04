import socket

#commented was for UDP
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 8888
#ip = "192.168.56.101"
s.connect(('192.168.56.101',port))
#s.bind(('',port))
#while True:
data = s.recvfrom(1024)
s.send(b'Hi, saya client.ty.')
print(data)
s.close()
