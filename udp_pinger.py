import socket
import sys

# Creat a UDP socket
client_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server addres
server_ip = sys.argv[0]

server_port = 1337
data_size = 100
msg_count = 10
wait_timeout = 1000

if '-p' in sys.argv:
    server_port = sys.argv[(sys.argv).index('-p') + 1]
if '-s' in sys.argv:
    data_size = sys.argv[(sys.argv).index('-s') + 1]
if '-c' in sys.argv:
    msg_count = sys.argv[(sys.argv).index('-c') + 1]
if '-t' in sys.argv:
    wait_timeout = sys.argv[(sys.argv).index('-t') + 1]

server_add = (server_ip, server_port)

for i in range(msg_count):
    msg_opcode = my_byte = bytes([0])
    msg_id = i
    msg_data = ""

    message = msg_opcode+msg_id+msg_data

    client_soc.sendto(message, server_add)
    data, server = client_soc.recvfrom(1024)

    print("64 bytes from ", server_ip ," : seq= ", i ," rtt= ", tim)

client_soc.close()