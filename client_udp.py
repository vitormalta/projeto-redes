from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import json
import time

class ClientUDP():

	def __init__(self, name, server_ip, server_port):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.dest = (server_ip, server_port)
		self.name = name
		Thread(target=self.recv_data, args=()).start()

	def get_ip(self):
		self.sock.connect(('8.8.8.8', 80))
		ip = self.sock.getsockname()[0]
		return ip

	def get_name(self):
		return self.name

	def send_data(self, data):
		self.sock.sendto(data.encode(), self.dest)

	def recv_data(self):
		while True:
			try:
				if not data:
					break
				else:
					msg_from_server = self.sock.recvfrom(1500)
					print('Mensagem recebida: {}'.format(msg_from_server[0].decode('utf-8')))
					break
			except:
				pass

def main():
	print('Bem vindo ao Quiz Competitivo!\nPara participar informe alguns dados...')
	name = input('Digite seu nome: ')
	server_ip, server_port = input('Endereço IP do servidor: '), int(input('Porta do servidor: '))
	return name, server_ip, server_port

if __name__ == '__main__':
	name, server_ip, server_port = main()
	client_udp = ClientUDP(name, server_ip, server_port)
	info = dict(name=name, ip=client_udp.get_ip())
	client_udp.send_data(json.dumps(info))
	menu = input('Deseja iniciar a partida (s/n)? >>> ').lower()