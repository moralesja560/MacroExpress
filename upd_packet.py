import socket
import sys

#your own public IP
UDP_IP = "10.65.72.5"
#choose UDP port. PLC does not have a port selector
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print("received message: %s" % data)
	if "break_port" in str(data):
		print("command received: Exiting")
		sys.exit()
