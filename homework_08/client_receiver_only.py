import json
import logging
from select import select
from socket import *
from datetime import datetime
import argparse
import time
import log.client_log_config
from log_decorator import Log
import sys

from response_codes import server_response_codes
log_client = logging.getLogger("app." + __name__)


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


@Log(log_client)
def parse_parameters(default_host, default_port):
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', nargs='?', default=default_host, help="ip-адрес сервера")
    parser.add_argument('port', nargs='?', default=default_port, type=int, help="tcp-порт на сервере, по умолчанию 7777")
    args = parser.parse_args()
    addr = args.addr
    port = args.port
    log_client.info('Parameters parsed OK')
    return addr, port


if __name__ == "__main__":

    # try:
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(parse_parameters(default_host, default_port))
        print("connected")
        while True:
            print("waiting data")
            time.sleep(2)
            data = s.recv(1000000)

            log_client.info('Server communication OK')

    # except Exception:
    #     log_client.critical('Critical error in communication with server')

            resp_presence = json.loads(data.decode('utf-8'))

            resp_code = str(resp_presence.get("response"))
            resp_time = datetime.utcfromtimestamp(resp_presence.get("time")).strftime('%Y-%m-%d %H:%M:%S')
            resp_alert = resp_presence.get("alert")

            print('Сообщение от сервера: ', resp_presence, ', длиной ', len(data), ' байт')
            print(f'server response:\n code:  {resp_code} - {server_response_codes.get(resp_code)}\n '
                  f'time:  {resp_time} \n alert: {resp_alert}')

