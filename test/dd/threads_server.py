
import socket
import threading
import json
import time
import random
from datetime import datetime

class ThreadsServer:
    def __init__(self, host='localhost', port=8080):
        self.host = host
        self.port = port
        self.clients = {}  # {username: client_socket}
        self.users = {}    # {username: user_info}
        self.posts = []    # 모든 게시물
        self.running = False

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.running = True

        print(f"Threads 서버가 {self.host}:{self.port}에서 시작되었습니다...")

        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                print(f"새 클라이언트 연결: {address}")

                # 클라이언트 핸들링을 위한 스레드 생성
                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, address)
                )
                client_thread.daemon = True
                client_thread.start()

            except Exception as e:
                if self.running:
                    print(f"서버 오류: {e}")
                break

    def handle_client(self, client_socket, address):
        username = None
        try:
            while True:
                # 클라이언트로부터 메시지 받기
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                try:
                    message = json.loads(data)
                    response = self.process_message(message, client_socket)

                    if message.get('type') == 'login' and response.get('status') == 'success':
                        username = message.get('username')
                        self.clients[username] = client_socket

                    # 응답 보내기
                    if response:
                        client_socket.send(json.dumps(response).encode('utf-8'))

                except json.JSONDecodeError:
                    error_response = {'type': 'error', 'message': '잘못된 JSON 형식'}
                    client_socket.send(json.dumps(error_response).encode('utf-8'))

        except Exception as e:
            print(f"클라이언트 핸들링 오류: {e}")
        finally:
            # 클라이언트 연결 종료 처리
            if username and username in self.clients:
                del self.clients[username]
                print(f"{username} 연결 종료")
            client_socket.close()

    def process_message(self, message, client_socket):
        msg_type = message.get('type')

        if msg_type == 'register':
            return self.handle_register(message)
        elif msg_type == 'login':
            return self.handle_login(message)
        elif msg_type == 'post':
            return self.handle_post(message)
        elif msg_type == 'get_feed':
            return self.handle_get_feed(message)
        elif msg_type == 'get_notifications':
            return self.handle_get_notifications(message)
        elif msg_type == 'like_post':
            return self.handle_like_post(message)
        else:
            return {'type': 'error', 'message': '알 수 없는 메시지 타입'}

    def handle_register(self, message):
        username = message.get('username')
        password = message.get('password')
        email = message.get('email', '')

        if username in self.users:
            return {'type': 'register', 'status': 'error', 'message': '이미 존재하는 사용자명입니다.'}

        # 사용자 등록
        self.users[username] = {
            'password': password,
            'email': email,
            'join_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'followers': [],
            'following': [],
            'posts': []
        }

        return {'type': 'register', 'status': 'success', 'message': '회원가입이 완료되었습니다.'}

    def handle_login(self, message):
        username = message.get('username')
        password = message.get('password')

        if username not in self.users:
            return {'type': 'login', 'status': 'error', 'message': '존재하지 않는 사용자입니다.'}

        if self.users[username]['password'] != password:
            return {'type': 'login', 'status': 'error', 'message': '비밀번호가 틀렸습니다.'}

        return {'type': 'login', 'status': 'success', 'message': '로그인 성공', 'user_info': self.users[username]}

    def handle_post(self, message):
        username = message.get('username')
        content = message.get('content')

        if username not in self.users:
            return {'type': 'post', 'status': 'error', 'message': '인증되지 않은 사용자'}

        # 새 게시물 생성
        post = {
            'id': len(self.posts) + 1,
            'username': username,
            'content': content,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'likes': 0,
            'liked_by': []
        }

        self.posts.append(post)
        self.users[username]['posts'].append(post['id'])

        # 모든 클라이언트에게 새 게시물 알림
        self.broadcast_new_post(post)

        return {'type': 'post', 'status': 'success', 'message': '게시물이 작성되었습니다.'}

    def handle_get_feed(self, message):
        username = message.get('username')

        # 최신 게시물부터 정렬
        sorted_posts = sorted(self.posts, key=lambda x: x['timestamp'], reverse=True)

        return {'type': 'feed', 'posts': sorted_posts}

    def handle_get_notifications(self, message):
        username = message.get('username')

        # 간단한 알림 시뮬레이션
        notifications = [
            {'type': 'like', 'message': f'{random.choice(list(self.users.keys()) if self.users else ["Someone"])}님이 회원님의 게시물을 좋아합니다.', 'time': datetime.now().strftime("%H:%M")},
            {'type': 'follow', 'message': f'{random.choice(list(self.users.keys()) if self.users else ["Someone"])}님이 회원님을 팔로우하기 시작했습니다.', 'time': datetime.now().strftime("%H:%M")},
        ]

        return {'type': 'notifications', 'notifications': notifications}

    def handle_like_post(self, message):
        username = message.get('username')
        post_id = message.get('post_id')

        # 게시물 찾기
        for post in self.posts:
            if post['id'] == post_id:
                if username not in post['liked_by']:
                    post['liked_by'].append(username)
                    post['likes'] += 1
                    return {'type': 'like_post', 'status': 'success', 'message': '좋아요를 눌렀습니다.'}
                else:
                    post['liked_by'].remove(username)
                    post['likes'] -= 1
                    return {'type': 'like_post', 'status': 'success', 'message': '좋아요를 취소했습니다.'}

        return {'type': 'like_post', 'status': 'error', 'message': '게시물을 찾을 수 없습니다.'}

    def broadcast_new_post(self, post):
        """모든 연결된 클라이언트에게 새 게시물 알림"""
        notification = {
            'type': 'new_post_notification',
            'post': post
        }

        for username, client_socket in list(self.clients.items()):
            try:
                client_socket.send(json.dumps(notification).encode('utf-8'))
            except:
                # 연결이 끊어진 클라이언트 제거
                del self.clients[username]

    def stop_server(self):
        self.running = False
        if hasattr(self, 'server_socket'):
            self.server_socket.close()

if __name__ == "__main__":
    server = ThreadsServer()
    try:
        server.start_server()
    except KeyboardInterrupt:
        print("\n서버를 종료합니다...")
        server.stop_server()
