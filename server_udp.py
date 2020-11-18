from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import random
import json
import time
import os

class ServerUDP():

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.server = socket(AF_INET, SOCK_DGRAM) 
		self.server.bind((self.host, self.port))
		self.clients_list, self.num_of_clients = [], 0 
		self.chosen_numbers = []
		#self.server.listen()
		Thread(target=self.recv_msg, args=()).start()

	def get_clients_list(self):
		return self.clients_list

	def player_manager(self, info):
		if self.num_of_clients < 5:
			self.clients_list.append(json.loads(info))
			self.num_of_clients += 1
			print(self.clients_list)
		else:
			print('Limite máximo de participantes atingido!')
		
	def file_reader(self, index):
		path = os.getcwd()
		with open(path + '/tuplas.txt', 'r', encoding='utf-8') as file:
			question = file.readlines()
		print(question[index])
		return question[index]

	def question_manager(self, client_address):
		n = random.randint(0, 20)
		while True:
			if n in self.chosen_numbers:
				n = random.randint(0, 20)
			else:
				if len(self.chosen_numbers) == 20:
					print('Todas as perguntas foram enviadas aos clientes')
					break
				else:
					self.chosen_numbers.append(n)
					self.send(self.file_reader(n), client_address)
					print(f'Pergunta enviada ao jogador: {self.file_reader(n)}')
					break

	def recv_msg(self):
		while True:
			print('Aguardando requisições...')
			data, client = self.server.recvfrom(2048)
			if not data:
				break
			else:
				if data.decode() == 's':
					self.send("Bem vindo", client)
					#self.question_manager(client)
				else:
					for i in json.loads(data.decode()):
						if 'name' in i:
							self.player_manager(data)


	def send(self, data, address):
		if type(data) == type(list()):
			self.server.sendto(json.dumps(data).encode(), address)
		else:
			self.server.sendto(data.encode(), address)

if __name__ == '__main__':
	server = ServerUDP('localhost', 8080)