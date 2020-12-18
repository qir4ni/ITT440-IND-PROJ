import socket
import sys
import json
import tqdm
import os

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

msgFromClient = "Hello, this is client"
bytesSend = str.encode(msgFromClient)
buffer = 1024

# send msg to server via UDP socket
s.sendto(bytesSend, (host, port))

print("[+] Sending message to NTP Server")

# close the socket
s.close()
