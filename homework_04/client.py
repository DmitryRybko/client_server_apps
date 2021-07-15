import json
from socket import *
from response_codes import server_response_codes
from datetime import datetime
import argparse
import time

time_stamp = int(time.time())
default_port = 7777
default_host = 'localhost'


msg_presence = {
    "action": "presence",
    "time": time_stamp,
    "type": "status",
    "user": {
        "account_name": "client_001",
        "status": "client_001 present"
    }
}


def parse_parameters(default_host, default_port):
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default=default_host, help="ip-адрес сервера")
    parser.add_argument('port', nargs='?', default=default_port, type=int, help="tcp-порт на сервере, по умолчанию 7777")
    args = parser.parse_args()
    addr = args.addr
    port = args.port
    return addr, port


if __name__ == "__main__":

    s = socket(AF_INET, SOCK_STREAM)
    s.connect(parse_parameters(default_host, default_port))

    msg_presence_json = json.dumps(msg_presence)

    s.send(msg_presence_json.encode('utf-8'))
    data = s.recv(1000000)
    s.close()

    resp_presence = json.loads(data.decode('utf-8'))

    resp_code = str(resp_presence.get("response"))
    resp_time = datetime.utcfromtimestamp(resp_presence.get("time")).strftime('%Y-%m-%d %H:%M:%S')
    resp_alert = resp_presence.get("alert")

    print('Сообщение от сервера: ', resp_presence, ', длиной ', len(data), ' байт')
    print(f'server response:\n code:  {resp_code} - {server_response_codes.get(resp_code)}\n '
          f'time:  {resp_time} \n alert: {resp_alert}')

