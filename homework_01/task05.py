"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com 
и преобразовать результаты из байтовового в строковый тип на кириллице."""

import subprocess

ping_param_1 = ['ping', 'yandex.ru']
ping_subprocess_1 = subprocess.Popen(ping_param_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in ping_subprocess_1.stdout:
    print(line)

"""
b'\r\n'
b'Pinging YANDEX.ru [77.88.55.66] with 32 bytes of data:\r\n'
b'Reply from 77.88.55.66: bytes=32 time=43ms TTL=242\r\n'
b'Reply from 77.88.55.66: bytes=32 time=34ms TTL=242\r\n'
b'Reply from 77.88.55.66: bytes=32 time=30ms TTL=242\r\n'
b'Reply from 77.88.55.66: bytes=32 time=35ms TTL=242\r\n'
b'\r\n'
b'Ping statistics for 77.88.55.66:\r\n'
b'    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\r\n'
b'Approximate round trip times in milli-seconds:\r\n'
b'    Minimum = 30ms, Maximum = 43ms, Average = 35ms\r\n'
"""

ping_param_1 = ['ping', 'youtube.com']
ping_subprocess_1 = subprocess.Popen(ping_param_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
for line in ping_subprocess_1.stdout:
    print(line)

"""
b'\r\n'
b'Pinging youtube.com [216.58.210.174] with 32 bytes of data:\r\n'
b'Reply from 216.58.210.174: bytes=32 time=37ms TTL=110\r\n'
b'Reply from 216.58.210.174: bytes=32 time=40ms TTL=110\r\n'
b'Reply from 216.58.210.174: bytes=32 time=40ms TTL=110\r\n'
b'Reply from 216.58.210.174: bytes=32 time=50ms TTL=110\r\n'
b'\r\n'
b'Ping statistics for 216.58.210.174:\r\n'
b'    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),\r\n'
b'Approximate round trip times in milli-seconds:\r\n'
b'    Minimum = 37ms, Maximum = 50ms, Average = 41ms\r\n'
"""