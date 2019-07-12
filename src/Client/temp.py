import sys
sys.path.append('..\\')
import lib.socket_wrapper as sw
import socket
import time

client = sw.Client()
client.s.settimeout(2)
print(client.s.connect(('192.168.1.118', 8000)))
# print(client.set_client_connection('192.168.1.118', 8000))
time.sleep(10)

print('john')
print(client.set_client_connection('192.168.1.118', 8001))
client.close()
time.sleep(2)

gg = sw.Client()
print(client.set_client_connection('192.168.1.118', 8000))
time.sleep(2)
client.close()
