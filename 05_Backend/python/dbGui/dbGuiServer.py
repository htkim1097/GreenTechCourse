import pymysql
import socket
import threading

def send_query(query):
    try:
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="0000",
            charset="utf8",
            database=None
        )

        cur = conn.cursor()

        # 테이블 데이터 조회
        cur.execute(query)
        db_data = cur.fetchall()
        conn.commit()
        conn.close()

        data = ""
        for d in db_data:
            data += f"{d[0]},"

        return data
    except:
        print("send_query() 오류")
        return None

def handle_client(client_socket, address):
    print(f"연결: {address}")
    try:
        while True:
            cli_data = client_socket.recv(1024).decode()
            if not cli_data:
                break
            print(cli_data)
            db_data = send_query(cli_data)
            print(db_data)

            client_socket.sendall(db_data.encode())
    except Exception as e:
        print("에러 발생", e)
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8080))

    server.listen()
    print("서버 시작")
    while True:
        client_socket, address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

start_server()