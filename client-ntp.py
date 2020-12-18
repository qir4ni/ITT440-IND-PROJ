import socket
import sys
import json
import tqdm
import os

# create client socket
s = socket.socket()

# the ip address of server
host = '192.168.1.7'

# the port
port = 123

# connect to socket
print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")


# close the socket
s.close()
