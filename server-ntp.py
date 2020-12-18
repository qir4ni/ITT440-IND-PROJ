from os import system
import socket
from tqdm import tqdm
import time
import sys
import os
import ntplib  # using ntplib
from time import ctime  # importing time
from datetime import datetime  # for current local time

_ = system('clear')
#print ("\n\t\t\t\t\t Booting Up the Client App ... \n")
#for i in tqdm (range (100),
#               desc="\t\t Loadingâ€¦",
#               ascii=False, ncols=75):
#    time.sleep(0.02)
#
#print(" Complete !!!")

#c = ntplib.NTPClient()  # assigning to variable c
#response = c.request('my.pool.ntp.org', version=3)
#print(response.offset)
#print(response.version)
#print(ctime(response.tx_time))

print(r"""
-----------------------------------------
  _   _ _______ _____         __   ___  
 | \ | |__   __|  __ \       /_ | / _ \ 
 |  \| |  | |  | |__) | __   _| || | | |
 | . ` |  | |  |  ___/  \ \ / / || | | |
 | |\  |  | |  | |       \ V /| || |_| |
 |_| \_|  |_|  |_|        \_/ |_(_)___/ 
                                        
-----------------------------------------
                """)


def main():

	status = '1'
	while(status != '0'):
		print("\n[0] Exit the Program\n[1] Print Latest DateTime Information\n[2] Change DateTime of System to Latest\n[3] Start NTP Server\n")
		option = input("Choose option: ")
		print("Option choosed is", option)

		status = option

		if(option == '1'):
			local = datetime.now()
			print("\nQuerying the NTP Server\n---------------------")
			c = ntplib.NTPClient()  # assigning to variable c
			response = c.request('my.pool.ntp.org', version=3)
			print("Response Offset\t\t: ", response.offset)
			print("Response Version\t: ", response.version)
			print("Response Time\t\t: ", ctime(response.tx_time))
			print("Local DateTime\t\t: ", local)
			print("\n")
		elif(option == '2'):
			print("Changing the System DateTime..")
			# os.system("echo passwd | "sudo date -s \"Thu Aug  9 21:31:26 UTC 2012\")
			# _ = system("echo passwd | "sudo date -s \"\")
		elif(option == '3'):
			print("\nStarting NTP Server..")
			# create server socket(UDP socket)
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
			print(f"[+] Socket successfully created")

			# the server port
			port = 123
			buffer = 1024

			# bind the socket
			s.bind(('', port))
			print(f"[+] Socket binded to " + str(port))

			# listening for incoming datagrams
			while(True):
				print("[+] Server is listening..")
				#bytesRecv = s.recvfrom(buffer)
				#dateRecv = bytesRecv[0]
				#address = bytesRecv[1]

				#clientDate = "DateTime on Client: {}".format(dateRecv)
				#clientIP = "Client IP Address: {}".format(address)

				dateRecv, address = s.recvfrom(buffer)

				T2 = datetime.datetime.now() # receive timestamp
				T2 = T2.strftime("%Y-%m-%d, %H:%M:%S") # T2 timestamp convert to string
				T3 = datetime.datetime.now() # transmitted timestamp
				T3 = T3.strftime("%Y-%m-%d, %H:%M:%S") # T3 timestamp convert to string

				bytesSend = str.encode(T2)
				s.sendto(bytesSend, ('', port))
				bytesSend = str.encode(T3)
				s.sendto(bytesSend, ('', port))

				clientLocalDT = datetime.strptime(dateRecv.decode(), "%Y-%m-%d, %H:%M:%S")
				print(clientLocalDT)

				#DTRecv = bytesRecv.decode()
				#print(DTRecv)
				#clientLocalDT  = datetime.strptime(clientDate,"%Y-%m-%d, %H:%M:%S")
				#print("Local DateTime of Client: ")
				#print(clientLocalDT)

				#print(clientDate)
				#print(clientIP)

			print(f"[+] Socket is listening | Port: {port}")

			# accept connections if there is any
			client_socket, address = s.accept()

			# if below code is executed, that means the sender is connected
			print(f"[+] {address} is connected.")

	print("Exiting..")


if __name__ == "__main__":
    main()
