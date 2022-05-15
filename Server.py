import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        answer=data.decode('utf-8')
        '''print(data.decode('utf-8'))'''
        if answer=='yes':
            str2='im ready'
            connection.send(str2.encode())
            break
        else:
            str3='bye'
            connection.send(str3.encode())
            break
    connection.close()

while True:
    print("====Статистика====")
    Client, address = ServerSocket.accept()
    print('Новое соединение! ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Количество подключенных пользователей: ' + str(ThreadCount))
ServerSocket.close()