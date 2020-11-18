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
                print('Mensagem do servidor {}: {}'.format(server, data.decode('utf-8')))


def get_ip():
    sock = socket(AF_INET, SOCK_DGRAM)
    local_ip = sock.connect(('8.8.8.8', 80))
    local_ip = sock.getsockname()[0]
    return local_ip


def main():
    print('Bem vindo(a) ao Quiz competitivo!')
    client_name = input("Digite seu nome: ")
    ip = input('Endereço do servidor: ')
    port = int(input('Porta do servidor: '))
    return client_name, ip, port


def menu():
    print('\nSelecione o número da opção desejada: \n')
    opt = input('1 - Iniciar partida\n2 - Lista de jogadores\n3 - Ajuda\n>> ')
    if opt == '1':
        client_udp.send_data(opt)
    elif opt == '2':
        client_udp.send_data(opt)
        return menu()
    elif opt == '3':
        print('Ao iniciar a partida cada jogador iniciará com 100 pontos\n'
              'Resposta correta: + 25 pontos\n'
              'Resposta incorreta: -5 pontos\n'
              'Sem resposta: -1 ponto\n'
              'As respostas são compostas por uma única palavra, com caracteres minúsculos\n'
              'Além disso cada jogador terá 10 segundos para responder.')
        return menu()


if __name__ == '__main__':
    name, ip, port = main()
    client_udp = ClientUDP(name, ip, port)
    info = [name, get_ip()]
    client_udp.send_data(json.dumps(info))
    menu()
