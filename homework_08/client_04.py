from socket import socket, AF_INET, SOCK_STREAM
import json
from threading import Thread

resp_test = {"response": "доставлено"}
resp_test_json = json.dumps(resp_test)


def receiver():
    print("Thread 1 started")
    def listen_messages():
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('', 7781))
        s.listen(5)
        return s

    s = listen_messages()

    while True:
        client, addr = s.accept()
        data = client.recv(1000000)
        data_decoded = json.loads(data.decode('utf-8'))
        print("")
        print('Сообщение: ', data_decoded, ', было отправлено клиентом: ', addr)
        print("Введите сообщение:")
        client.send(resp_test_json.encode('utf-8'))
        client.close()


def sender():
    print("Thread 2 started")
    while True:
        user_message = input("Введите сообщение:\n")
        msg_test = {"message": user_message}
        msg_test_json = json.dumps(msg_test)

        s = socket(AF_INET, SOCK_STREAM)
        s.connect(('localhost', 7780))

        s.send(msg_test_json.encode('utf-8'))
        data = s.recv(1000000)
        s.close()

        resp_test = json.loads(data.decode('utf-8'))

        print('Сообщение от другого клиента: ', resp_test, ', длиной ', len(data), ' байт')


t1 = Thread(target=receiver)
t2 = Thread(target=sender)

t1.start()
t2.start()
