import socket
import sys
import datetime

try:
    # Create a UDP socket
    client_soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Server address
    server_ip = sys.argv[1]

    server_port = 1337
    data_size = 100
    msg_total = 10
    wait_timeout = 1000.0

    if '-p' in sys.argv:
        server_port = int(sys.argv[(sys.argv).index('-p') + 1])
    if '-s' in sys.argv:
        data_size = int(sys.argv[(sys.argv).index('-s') + 1])
    if '-c' in sys.argv:
        msg_total = int(sys.argv[(sys.argv).index('-c') + 1])
    if '-t' in sys.argv:
        wait_timeout = float(sys.argv[(sys.argv).index('-t') + 1])

    server_add = (server_ip, server_port)
    client_soc.settimeout(wait_timeout/1000)
    msg_count = 0
    for i in range(msg_total):
        # sending msg
        temp = 0
        msg_opcode = temp.to_bytes(1, 'big')
        msg_id = i.to_bytes(4, 'big')
        msg_data = temp.to_bytes(data_size, 'big')
        msg = list(msg_opcode) + list(msg_id) + list(msg_data)
        client_soc.sendto(bytes(msg), server_add)
        # waiting for response till timeout
        try:
            a = datetime.datetime.now()
            data, server = client_soc.recvfrom(data_size + 4 + 1)
            b = datetime.datetime.now()
            c = b - a
            print(f"{len(data)} bytes from {server_ip}: seq={i} rtt={c.seconds / 1000} ms")
            msg_count += 1
        except TimeoutError:
            print("request timeout for icmp_seq", i)
            
    print(f"--- {server_ip} statistics ---")
    print(f"{msg_total} packets transmitted, {msg_count} packets received, {(((1-(msg_count/msg_total)) * 10000) // 1 ) / 100}% packet loss")
    client_soc.close()

except OSError as exception:
    print(exception.strerror)