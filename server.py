import socket
import threading
#to handle multiple connection requests at once
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET -> to use IPv4 over IPv6
#socket.SOCK_STREAM -> to use TCP/IP connection
#socket.SOCK_DGRAM -> to use UDP connection
sock.bind(('0.0.0.0',10000))
#choosen port 10000 ans whatever ip configured by the system
sock.listen(0)

connections = []

def connection_handler(c ,a):
	global connections

	while True:
		
		data = c.recv(1024)
		#recieve data packets of size 1024
		for connection in connections:
			connection.send(bytes(data))
			if not data:
				connections.remove(c)
				c.close()
				break	

while True:
	c,a=sock.accept()
	cThreads = threading.thread(target=connection_handler)
	#function that handles our connections
	cThreads.daemon=True
	#user will be able to exit programs regardless of open threads in the system
	cThread.start()
	connections.append(c)
	print(connections)