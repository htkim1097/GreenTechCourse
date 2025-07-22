import pymysql
import socket
import threading

def send_query(query):
    conn = pymysql.connect(
        host="192.168.0.41",
        port=8080,
        user="root",
        password="0000",
        charset="utf8"
    )

    cur = conn.cursor()

    # 테이블 데이터 조회
    cur.execute(query)
    data = cur.fetchall()
    conn.close()

    return data

def handle_client(client_socket, address):
    print(f"연결: {address}")
    try:
        while True:
            cli_data = client_socket.recv(1024)
            if not cli_data:
                break

            db_data = send_query(cli_data)

            client_socket.send(db_data)
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