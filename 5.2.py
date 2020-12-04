import socket

s = socket.socket()
host = '192.168.56.101'
port= 8889

print("Waiting for connection...")
try:
	s.connect((host,port))
except socket.error as e:
	print(str(e))

Response = s.recv(1024)
print(Response)
while True:
	Input =input("Say something: ")
	s.send(str.encode(Input))
	Response = s.recv(1024)
	print(Response.decode('utf-8'))
s.close()
