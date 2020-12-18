import socket
import sys
import json
import tqdm
import os
import datetime

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
localDT = datetime.datetime.now()

# print local sys datetime
print("[+] Local System DateTime : ", localDT)

# convert datetime to string
localDTStr = localDT.strftime("%Y-%m-%d, %H:%M:%S")

#msgFromClient = "Hello, this is client"
#bytesSend = str.encode(msgFromClient)
bytesSend = str.encode(localDTStr)
buffer = 1024

# send msg to server via UDP socket
s.sendto(bytesSend, (host, port))


print("[+] Sending Local DateTime to NTP Server")

# close the socket
s.close()
