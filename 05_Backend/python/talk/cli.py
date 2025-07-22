import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("192.168.0.41", 8080))

try:
    while True:
        msg = input("서버에 보낼 메시지: ")
        if msg.lower() == "exit":
            break

        client_socket.send(msg.encode())

        data = client_socket.recv(1024)  # 보레이트 : 1kb 씩 송수신
        print("서버로부터 받은 데이터: ", data.decode())
finally:
    client_socket.close()