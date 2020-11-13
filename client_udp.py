from socket import socket, AF_INET, SOCK_DGRAM
import time

class ClientUDP:

	def __init__(self, name, server_ip, server_port):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.dest = (server_ip, server_port)
		self.name = name

	def getName(self):
		return self.name

	def send(self, data):
		self.sock.sendto(data.encode(), self.dest)

	def recv(self):
		msg_from_server, server_address = self.sock.recvfrom(1500)
		print(f"Servidor mandou {msg_from_server.decode()}")

def main():
	print("Bem vindo ao Quizz Competitivo!\nPara participar informe alguns dados...")
	name = input("Digite seu nome: ")
	server_ip, server_port = input("Endereço IP do servidor: "), int(input("Porta do servidor: "))
	
	return name, server_ip, server_port

if __name__ == "__main__":
	name, server_ip, server_port = main()
	client = ClientUDP(name, server_ip, server_port)
	menu = input("Deseja iniciar a partida (s/n)? >>> ")