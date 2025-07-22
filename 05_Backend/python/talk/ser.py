import socket

# AF_INET : IPv4 체계
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 2323))
server_socket.listen()

print("서버 부팅")

comm, addr = server_socket.accept()
print(f"{addr}에서 연결")

while True:
    data = comm.recv(1024)
    if not data:
        break

    print(f"클라이언트에게 받은 데이터: {data.decode()}")
    comm.sendall(data)

comm.close()
server_socket.close()