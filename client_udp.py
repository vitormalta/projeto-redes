from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import json


class ClientUDP:

	def __init__(self, name_input, server_ip, server_port):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.dest = (server_ip, server_port)
		self.name = name_input
		Thread(target=self.recv_data, args=()).start()

	def get_name(self):
		return self.name

	def send_data(self, data):
		self.sock.sendto(data.encode(), self.dest)

	def recv_data(self):
		while True:
			data, server = self.sock.recvfrom(1500)
			if not data:
				break
			else:
				print('Mensagem recebida: {}'.format(data.decode('utf-8')))


def get_ip():
	sock = socket(AF_INET, SOCK_DGRAM)
	local_ip = sock.connect(('8.8.8.8', 80))
	local_ip = sock.getsockname()[0]
	return local_ip


def main():
	print('Bem vindo ao Quiz Competitivo!\nPara participar informe alguns dados...')
	client_name = input('Digite seu nome: ')
	ip, port = input('Endereço IP do servidor: '), int(input('Porta do servidor: '))
	return client_name, ip, port


if __name__ == '__main__':
	name, ip, port = main()
	client_udp = ClientUDP(name, ip, port)
	info = dict(name=name, ip=get_ip())
	client_udp.send_data(json.dumps(info))