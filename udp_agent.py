import socket
import sys



# Creat a UDP socket
server_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Local addres to bind to
host = "127.0.0.1"
port = 1337
if sys.argc == 3:
    port = sys.argv[2]

# Bind to the port
server_soc.bind((host, port))

# Receive message
data, addr = server_soc.recvfrom(1024)
