import socket
import sys
import select

try:
    # Create a UDP socket
    server_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Local address to bind to
    host = "127.0.0.1"
    port = 1337
    if len(sys.argv) == 3:
        port = int(sys.argv[2])

    # Bind to the port
    server_soc.bind((host, port))

    # Receive message
    while True:
        readable, _, _ = select.select([server_soc],[],[])
        for sock in readable: 
            data, addr = sock.recvfrom(1400)
            msg = list(data)
            msg[0] = 1
            sock.sendto(bytes(msg), addr)

except OSError as exception:
    print(exception.strerror)
