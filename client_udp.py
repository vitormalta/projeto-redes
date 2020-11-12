from socket import socket, AF_INET, SOCK_DGRAM

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
		print(f"O servidor enviou: {msg_from_server.decode()}")

def main():
	print("Bem vindo ao Quizz Competitivo!")
	menu = input("Deseja iniciar o jogo? (s/n) >>> ")

	if menu.lower() == "s":
		name = input("Digite seu nome: ")
		server_ip = input("Endereço IP do servidor: ")
		server_port = int(input("Porta do servidor: "))
	
	return name, server_ip, server_port

if __name__ == "__main__":
	name, server_ip, server_port = main()
	sock = ClientUDP(name, server_ip, server_port)