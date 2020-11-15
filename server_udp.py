from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import json
import time

class ServerUDP():

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.server = socket(AF_INET, SOCK_DGRAM) 
		self.server.bind((self.host, self.port))
		self.clients_list, self.num_of_clients = list(), 0 
		Thread(target=self.recv, args=()).start()

	def get_clients_list(self):
		return self.clients_list

	def player_manager(self, info):
		if self.num_of_clients < 5:
			self.clients_list.append(json.loads(info))
			self.num_of_clients += 1
			print(self.clients_list)
		else:
			print("Limite máximo de participantes atingido!")

	def recv(self):
		while True:
			print("Aguardando requisições...")
			data, client = self.server.recvfrom(1500)
			if not data:
				break
			else:
				for i in json.loads(data.decode()):
					if "name" in i:
						self.player_manager(data)

	def send(self, data, address):
		self.server.sendto(data.encode(), address)

if __name__ == "__main__":
	server = ServerUDP('localhost', 8080)