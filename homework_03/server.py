from socket import *
import json
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", default=7777, type=int, help="TCP-порт (по умолчанию 7777)")
parser.add_argument("-a", "--addr", default='',
                    help="IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)")
args = parser.parse_args()
addr = args.addr
port = args.port

s = socket(AF_INET, SOCK_STREAM)
s.bind((addr, port))
s.listen(5)

time_stamp = int(time.time())

resp_presence = {"response": 100,
                 "time": time_stamp,
                 "alert": "presence notification received"
                 }

resp_presence_json = json.dumps(resp_presence)

print("server started")

while True:
    client, addr = s.accept()
    data = client.recv(1000000)
    print('Сообщение: ', data.decode('utf-8'), ', было отправлено клиентом: ', addr)
    client.send(resp_presence_json.encode('utf-8'))
    client.close()
