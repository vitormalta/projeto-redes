from socket import socket, AF_INET, SOCK_DGRAM
import json
import time

class ClientUDP:

	def __init__(self, name, server_ip, server_port):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.dest = (server_ip, server_port)
		self.name = name

	def get_ip(self):
		self.sock.connect(('8.8.8.8', 80))
		ip = self.sock.getsockname()[0]
		return ip

	def send(self, data):
		self.sock.sendto(data.encode(), self.dest)

	def recv_msg(self):
		msg_from_server, server_address = self.sock.recvfrom(2048)
		print(f'Mensagem recebida: {msg_from_server.decode()}')

def main():
	print('Bem vindo ao Quiz Competitivo!\nPara participar informe alguns dados...')
	name = input('Digite seu nome: ')
	server_ip, server_port = input('Endereço IP do servidor: '), int(input('Porta do servidor: '))
	return name, server_ip, server_port

if __name__ == '__main__':
	name, server_ip, server_port = main()
	client = ClientUDP(name, server_ip, server_port)
	info = dict(name=name, ip=client.get_ip())
	client.send(json.dumps(info))
	menu = input('Deseja iniciar a partida (s/n)? >>> ').lower()
	client.send(menu)