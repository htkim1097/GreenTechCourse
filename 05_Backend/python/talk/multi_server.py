import socket
import threading

def handle_client(client_socket, address):
    print(f"연결: {address}")
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"{address} 데이터: {data.decode()}")
            client_socket.send(data)
    except:
        print("에러 발생")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.0.62", 8080))

    server.listen()
    print("서버 시작")
    while True:
        client_socket, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

start_server()