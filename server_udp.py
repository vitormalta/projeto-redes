from socket import socket, AF_INET, SOCK_DGRAM

class ServerUDP():

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.server = socket(AF_INET, SOCK_DGRAM) 
		#É um socket que recebe como parâmetro a pilha de protocolo e qual o protocolo da camada de transporte irá ser utilizada
		self.server.bind(self.host, self.port)
		#Vinculamos o socket a algum endereço IP e porta, o método recebe uma tupla onde o primeiro índice representa o endereço IP e o segundo índice é a porta
		self.clients_list = []

	def recv(self):

		msg, client = self.__server.recvfrom(1500)
		#Retorna uma tupla contendo o objeto em bytes lidos de um socket UDP e o endereço do cliente socket
		print(f"{cliente} enviou: {msg.decode()}...")


	def send(self, data, address):

		self.server.sendto(data.encode(), address)