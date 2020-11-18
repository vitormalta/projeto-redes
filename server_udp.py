from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread
import random
import json
import os


class ServerUDP:

    def __init__(self, host, port):
        self.server = socket(AF_INET, SOCK_DGRAM)
        self.server.bind((host, port))
        self.clients_list, self.num_of_clients = [], 0
        self.chosen_numbers = []
        Thread(target=self.recv_data, args=()).start()

    def get_clients_list(self):
        return self.clients_list

    def player_manager(self, info, address=None):
        if self.num_of_clients < 5:
            self.clients_list.append(json.loads(info))
            self.num_of_clients += 1
        else:
            self.send_data('1 - Limite máximo de jogadores atigindo! Deseja iniciar a partida?', address)

    @staticmethod
    def file_reader(index):
        path = os.getcwd()
        with open(path + '/tuplas.txt', 'r', encoding='utf-8') as file:
            question = file.readlines()
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
                    self.send_data(self.file_reader(n), client_address)
                    print(f'Pergunta enviada ao jogador: {self.file_reader(n)}')
                    break

    def recv_data(self):
        while True:
            print('Aguardando requisições...')
            data, client = self.server.recvfrom(1500)
            if not data:
                break
            else:
                if isinstance(json.loads(data.decode()), list) and self.num_of_clients <= 5:
                    print("O cliente {} enviou: {}".format(client, data.decode()))
                    self.player_manager(data.decode(), client)
                else:
                    if data.decode() == '1':
                        print('Start()')
                    elif data.decode() == '2':
                        self.send_data(json.dumps(self.get_clients_list()), client)

    def send_data(self, data, address):
        self.server.sendto(data.encode(), address)


if __name__ == '__main__':
    server_udp = ServerUDP('localhost', 8080)
