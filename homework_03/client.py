import json
from socket import *
from response_codes import server_response_codes
from datetime import datetime
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('addr', help="ip-адрес сервера")
parser.add_argument('port', nargs='?', default=7777, type=int, help="tcp-порт на сервере, по умолчанию 7777")
args = parser.parse_args()
addr = args.addr
port = args.port

s = socket(AF_INET, SOCK_STREAM)
s.connect((addr, port))

msg_presence = {
    "action": "presence",
    "time": "<unix timestamp>",
    "type": "status",
    "user": {
        "account_name": "client_001",
        "status": "client_001 present"
    }
}

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

