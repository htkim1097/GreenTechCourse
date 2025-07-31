
import socket
import json
import threading
import time

def test_basic_functionality():
    """기본 기능 테스트"""
    print("=== Threads SNS 앱 기본 기능 테스트 ===")

    # 서버 연결
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 8080))
        print("✅ 서버 연결 성공")
    except Exception as e:
        print(f"❌ 서버 연결 실패: {e}")
        print("먼저 threads_server.py를 실행하세요!")
        return

    # 회원가입 테스트
    register_msg = {
        'type': 'register',
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'password123'
    }

    client.send(json.dumps(register_msg).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    register_response = json.loads(response)

    if register_response.get('status') == 'success':
        print("✅ 회원가입 성공")
    else:
        print(f"⚠️ 회원가입: {register_response.get('message')}")

    # 로그인 테스트
    login_msg = {
        'type': 'login',
        'username': 'testuser',
        'password': 'password123'
    }

    client.send(json.dumps(login_msg).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    login_response = json.loads(response)

    if login_response.get('status') == 'success':
        print("✅ 로그인 성공")
    else:
        print(f"❌ 로그인 실패: {login_response.get('message')}")
        client.close()
        return

    # 게시물 작성 테스트
    post_msg = {
        'type': 'post',
        'username': 'testuser',
        'content': '안녕하세요! 첫 번째 테스트 게시물입니다. 🎉'
    }

    client.send(json.dumps(post_msg).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    post_response = json.loads(response)

    if post_response.get('status') == 'success':
        print("✅ 게시물 작성 성공")
    else:
        print(f"❌ 게시물 작성 실패: {post_response.get('message')}")

    # 피드 조회 테스트
    feed_msg = {
        'type': 'get_feed',
        'username': 'testuser'
    }

    client.send(json.dumps(feed_msg).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    feed_response = json.loads(response)

    if feed_response.get('type') == 'feed':
        posts = feed_response.get('posts', [])
        print(f"✅ 피드 조회 성공 - {len(posts)}개의 게시물")
        if posts:
            print(f"   최신 게시물: {posts[0]['content'][:30]}...")
    else:
        print("❌ 피드 조회 실패")

    # 알림 조회 테스트
    notif_msg = {
        'type': 'get_notifications',
        'username': 'testuser'
    }

    client.send(json.dumps(notif_msg).encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    notif_response = json.loads(response)

    if notif_response.get('type') == 'notifications':
        notifications = notif_response.get('notifications', [])
        print(f"✅ 알림 조회 성공 - {len(notifications)}개의 알림")
    else:
        print("❌ 알림 조회 실패")

    client.close()
    print("\n✅ 모든 기본 기능 테스트 완료!")
    print("\n이제 다음 명령으로 GUI 클라이언트를 실행해보세요:")
    print("python threads_client.py")

if __name__ == "__main__":
    test_basic_functionality()
