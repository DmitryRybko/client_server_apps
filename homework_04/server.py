from socket import *
import json
import time
import argparse

time_stamp = int(time.time())

default_port_settings = 7777
default_addr_settings = ''

resp_presence = {"response": 100,
                 "time": time_stamp,
                 "alert": "presence notification received"
                 }

resp_incorrect_request = {"response": 400,
                          "time": time_stamp,
                          "alert": "incorrect request / JSON Object"
                          }

responses = {"presence": resp_presence, "incorrect": resp_incorrect_request}


def parse_params(default_port, default_addr):

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=default_port, type=int, help="TCP-порт (по умолчанию 7777)")
    parser.add_argument("-a", "--addr", default=default_addr,
                        help="IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)")
    args = parser.parse_args()
    addr = args.addr
    port = args.port

    return addr, port


def form_response(request_dict):

    request_type = request_dict.get("action")
    select_response = responses.get(request_type, responses.get("incorrect"))
    resp_presence_json_encoded = json.dumps(select_response).encode('utf-8')

    return resp_presence_json_encoded


def start_server():

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(parse_params(default_port_settings, default_addr_settings))
    s.listen(5)
    print("server started")

    return s


if __name__ == "__main__":

    socket_server = start_server()

    while True:
        client, addr_client = socket_server.accept()
        data = client.recv(1000000)
        data_decoded = data.decode('utf-8')
        print('Сообщение: ', data_decoded, ', было отправлено клиентом: ', addr_client)
        request_dict = json.loads(data_decoded)
        response = form_response(request_dict)
        client.send(response)
        client.close()
