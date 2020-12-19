from os import system
import socket
from tqdm import tqdm
import time
import sys
#import datetime
import os
import ntplib  # using ntplib
from time import ctime  # importing time
from datetime import datetime  # for current local time
from _thread import *


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

def threaded_client(s, dateRecv, host, port):

	while True:
		#dateRecv, address = s.recvfrom(buffer)
		#host, port = address

		if not dateRecv:
			break

		print("[+] Client IP Address :", host)
		clientLocalDT = datetime.strptime(dateRecv.decode(), "%Y-%m-%d, %H:%M:%S.%f")
		print("[+] T1 :",clientLocalDT)

		T2 = datetime.now() # receive timestamp
		T2 = T2.strftime("%Y-%m-%d %H:%M:%S.%f") # T2 timestamp convert to string
		print("[+] T2 :", T2)
		bytesSend = str.encode(T2)
		s.sendto(bytesSend, (host, port))
		print("[+] Sending T2 to Client")

		T3 = datetime.now() # transmitted timestamp
		T3 = T3.strftime("%Y-%m-%d %H:%M:%S.%f") # T3 timestamp convert to string
		print("[+] T3 :", T3)
		bytesSend = str.encode(T3)
		s.sendto(bytesSend, (host, port))
		print("[+] Sending T3 to Client")
		print("[+] Process Completed\n")

		# server is listening
		print(f"[+] Server is listening.. | Port: 123")


		#s.sendall(str.encode("Bye"))
		break

	# close connection
	#s.close()


def main():

	status = '1'
	while(status != '0'):
		print("\n[0] Exit the Program\n[1] Print Latest DateTime Information\n[2] Start NTP Server\n")
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
			print("Response Time\t\t: ", datetime.fromtimestamp(response.tx_time))
			print("Local DateTime\t\t: ", local)
			print("\n")
		elif(option == '2'):
			print("\nStarting NTP Server..")
			# create server socket(UDP socket)
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
			print(f"[+] Socket successfully created")

			# the server port
			port = 123
			buffer = 1024
			ThreadCount = 0

			# bind the socket
			s.bind(('', port))
			print(f"[+] Socket binded to " + str(port))

			# server is listening
			print(f"[+] Server is listening.. | Port: {port}")

			# listening for incoming datagrams
			while(True):

				dateRecv, address = s.recvfrom(buffer)
				host, port = address

				# accept connections if there is any
				#client_socket, address = s.accept()

				# if below code is executed, that means the sender is connected
				print(f"[+] {address} is connected.")

				#new thread for client
				start_new_thread(threaded_client, (s, dateRecv, host, port))

				ThreadCount += 1
				print("\n[+] Thread Number :" + str(ThreadCount))

			# close socket
			s.close()


			#print(f"[+] Socket is listening | Port: {port}")


	print("Exiting..")


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print('Interrupted')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
