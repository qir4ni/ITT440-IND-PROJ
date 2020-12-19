import socket
import sys
import json
import tqdm
import os
import datetime
from datetime import datetime
from os import system

def calcOffset():
	print("Calculating Offset")

def calcDelay():
	print("Calculating Delay")

_ = system('clear')

print(r"""
-----------------------------------------
  _   _ _______ _____         __   ___  
 | \ | |__   __|  __ \       /_ | / _ \ 
 |  \| |  | |  | |__) | __   _| || | | |
 | . ` |  | |  |  ___/  \ \ / / || | | |
 | |\  |  | |  | |       \ V /| || |_| |
 |_| \_|  |_|  |_|        \_/ |_(_)___/ 

	     Client Version
-----------------------------------------
                """)

def main():

	# create client socket
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

	# the ip address of server
	host = '192.168.1.5'

	# the port
	port = 123

	# connect to socket
	print(f"[+] Connecting to {host}:{port}")
	s.connect((host, port))
	print("[+] Connected.")

	# get local sys datetime
	localDT = datetime.now()

	# print local sys datetime
	print("[+] Local System DateTime : ", localDT)

	# convert datetime to string
	localDTStr = localDT.strftime("%Y-%m-%d, %H:%M:%S.%f")

	#msgFromClient = "Hello, this is client"
	#bytesSend = str.encode(msgFromClient)
	bytesSend = str.encode(localDTStr)
	buffer = 1024

	# send msg to server via UDP socket
	s.sendto(bytesSend, (host, port))
	#s.sendto(localDT, (host, port))


	print("[+] Sending Local DateTime to NTP Server")

	T1 = localDT # originate timestamp

	T2, address = s.recvfrom(buffer) # receive timestamp
	T2 = datetime.strptime(T2.decode(), "%Y-%m-%d %H:%M:%S.%f")
	print("[+] T1 :", T1)
	print("[+] T2 :", T2)

	T3, address = s.recvfrom(buffer)  # transmitted timestamp
	T3 = datetime.strptime(T3.decode(), "%Y-%m-%d %H:%M:%S.%f")
	print("[+] T3 :", T3)

	T4 =  datetime.now() #timestamp reference
	T4 = T4.strftime("%Y-%m-%d %H:%M:%S.%f")
	print("[+] T4 :", T4)

	# close the socket
	s.close()

if __name__ == "__main__":
	try:
        	main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
