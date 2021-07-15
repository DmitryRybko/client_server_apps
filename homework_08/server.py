import select
from socket import *
import json
import time
import argparse
import logging
import logging.handlers
import log.server_log_config
from log_decorator import Log


handler = logging.handlers.TimedRotatingFileHandler("log/server.log", when="d", interval=1, backupCount=10)
log_server = logging.getLogger("app." + __name__)
log_server.addHandler(handler)

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


@Log(log_server)
def parse_params(default_port, default_addr):

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default=default_port, type=int, help="TCP-порт (по умолчанию 7777)")
    parser.add_argument("-a", "--addr", default=default_addr,
                        help="IP-адрес для прослушивания (по умолчанию слушает все доступные адреса)")
    args = parser.parse_args()
    addr = args.addr
    port = args.port

    log_server.info("Parameters parsed OK")
    return addr, port


@Log(log_server)
def form_response(request_dict):

    request_type = request_dict.get("action")
    select_response = responses.get(request_type, responses.get("incorrect"))
    resp_presence_json_encoded = json.dumps(select_response).encode('utf-8')

    return resp_presence_json_encoded


def read_requests(r_clients, all_clients):
    """ Чтение запросов из списка клиентов
    """
    responses = {}

    for sock in r_clients:
        try:
            data = sock.recv(1000000).decode('utf-8')
            responses[sock] = data
        except:
            print('Клиент {} {} отключился (reading requests)'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)

    return responses


def write_responses(requests, w_clients, all_clients):
    """ Эхо-ответ сервера клиентам, от которых были запросы
    """
    print(f'все запросы: {requests}')
    print(f'все клиенты для записи: {w_clients}')
    for sock in w_clients:
        try:
            server_response = json.dumps(resp_presence).encode('utf-8')
            sock.send(server_response)
            print("Ответ сервера")
            print(server_response)
        except:
            print('Клиент {} {} отключился (writing requests)'.format(sock.fileno(), sock.getpeername()))
            sock.close()
            all_clients.remove(sock)


@Log(log_server)
def start_server():

    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(parse_params(default_port_settings, default_addr_settings))
        s.listen(5)
        s.settimeout(0.2)
        print("server started")
        log_server.info("Server started OK")
        return s

    except Exception:
        log_server.critical("Server failed to start")


if __name__ == "__main__":

    clients = []

    s = start_server()

    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            wait = 1
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass

            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)




