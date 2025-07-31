
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import socket
import json
import threading
import time
from datetime import datetime

class ThreadsClient:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Threads - 실시간 SNS")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # 네트워크 설정
        self.host = 'localhost'
        self.port = 8080
        self.socket = None
        self.connected = False
        self.username = None

        # GUI 상태
        self.current_screen = "login"

        # 스타일 설정
        self.setup_styles()

        # 화면 초기화
        self.create_login_screen()

        # 업데이트 스레드들
        self.update_threads_running = False

    def setup_styles(self):
        """GUI 스타일 설정"""
        style = ttk.Style()

        # Threads 스타일 색상
        self.bg_color = "#000000"  # 검은색 배경
        self.text_color = "#FFFFFF"  # 흰색 텍스트
        self.accent_color = "#1DA1F2"  # 파란색 액센트

        self.root.configure(bg=self.bg_color)

    def create_login_screen(self):
        """로그인 화면 생성"""
        self.clear_screen()

        # 메인 프레임
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # 로고/타이틀
        title_label = tk.Label(main_frame, text="Threads", 
                              font=("Arial", 24, "bold"), 
                              fg=self.text_color, bg=self.bg_color)
        title_label.pack(pady=(50, 30))

        # 로그인 폼
        login_frame = tk.Frame(main_frame, bg=self.bg_color)
        login_frame.pack(pady=20)

        # 사용자 이름
        tk.Label(login_frame, text="사용자 이름", 
                fg=self.text_color, bg=self.bg_color, font=("Arial", 12)).pack(anchor='w')
        self.username_entry = tk.Entry(login_frame, font=("Arial", 12), width=25)
        self.username_entry.pack(pady=(5, 15))

        # 비밀번호
        tk.Label(login_frame, text="비밀번호", 
                fg=self.text_color, bg=self.bg_color, font=("Arial", 12)).pack(anchor='w')
        self.password_entry = tk.Entry(login_frame, font=("Arial", 12), width=25, show="*")
        self.password_entry.pack(pady=(5, 20))

        # 버튼들
        button_frame = tk.Frame(login_frame, bg=self.bg_color)
        button_frame.pack()

        login_btn = tk.Button(button_frame, text="로그인", 
                             font=("Arial", 12), width=15,
                             bg=self.accent_color, fg="white",
                             command=self.login)
        login_btn.pack(pady=5)

        register_btn = tk.Button(button_frame, text="회원가입", 
                               font=("Arial", 12), width=15,
                               bg="#333333", fg=self.text_color,
                               command=self.create_register_screen)
        register_btn.pack(pady=5)

        # 엔터키 바인딩
        self.password_entry.bind('<Return>', lambda e: self.login())

    def create_register_screen(self):
        """회원가입 화면 생성"""
        self.clear_screen()

        # 메인 프레임
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)

        # 타이틀
        title_label = tk.Label(main_frame, text="회원가입", 
                              font=("Arial", 20, "bold"), 
                              fg=self.text_color, bg=self.bg_color)
        title_label.pack(pady=(30, 20))

        # 회원가입 폼
        register_frame = tk.Frame(main_frame, bg=self.bg_color)
        register_frame.pack(pady=20)

        # 사용자 이름
        tk.Label(register_frame, text="사용자 이름", 
                fg=self.text_color, bg=self.bg_color, font=("Arial", 12)).pack(anchor='w')
        self.reg_username_entry = tk.Entry(register_frame, font=("Arial", 12), width=25)
        self.reg_username_entry.pack(pady=(5, 15))

        # 이메일
        tk.Label(register_frame, text="이메일", 
                fg=self.text_color, bg=self.bg_color, font=("Arial", 12)).pack(anchor='w')
        self.reg_email_entry = tk.Entry(register_frame, font=("Arial", 12), width=25)
        self.reg_email_entry.pack(pady=(5, 15))

        # 비밀번호
        tk.Label(register_frame, text="비밀번호", 
                fg=self.text_color, bg=self.bg_color, font=("Arial", 12)).pack(anchor='w')
        self.reg_password_entry = tk.Entry(register_frame, font=("Arial", 12), width=25, show="*")
        self.reg_password_entry.pack(pady=(5, 20))

        # 버튼들
        button_frame = tk.Frame(register_frame, bg=self.bg_color)
        button_frame.pack()

        register_btn = tk.Button(button_frame, text="가입하기", 
                               font=("Arial", 12), width=15,
                               bg=self.accent_color, fg="white",
                               command=self.register)
        register_btn.pack(pady=5)

        back_btn = tk.Button(button_frame, text="뒤로가기", 
                           font=("Arial", 12), width=15,
                           bg="#333333", fg=self.text_color,
                           command=self.create_login_screen)
        back_btn.pack(pady=5)

    def create_main_screen(self):
        """메인 화면 생성"""
        self.clear_screen()
        self.current_screen = "main"

        # 메인 프레임
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill='both', expand=True)

        # 상단 헤더
        header_frame = tk.Frame(main_frame, bg=self.bg_color, height=60)
        header_frame.pack(fill='x', padx=10, pady=5)
        header_frame.pack_propagate(False)

        # 로고
        logo_label = tk.Label(header_frame, text="Threads", 
                             font=("Arial", 16, "bold"), 
                             fg=self.text_color, bg=self.bg_color)
        logo_label.pack(side='left', pady=15)

        # 사용자 정보
        user_label = tk.Label(header_frame, text=f"@{self.username}", 
                             font=("Arial", 12), 
                             fg=self.accent_color, bg=self.bg_color)
        user_label.pack(side='right', pady=15)

        # 탭 프레임
        tab_frame = tk.Frame(main_frame, bg=self.bg_color)
        tab_frame.pack(fill='x', padx=10)

        # 탭 버튼들
        self.feed_btn = tk.Button(tab_frame, text="피드", 
                                 font=("Arial", 12), width=10,
                                 bg=self.accent_color, fg="white",
                                 command=self.show_feed_tab)
        self.feed_btn.pack(side='left', padx=5)

        self.notifications_btn = tk.Button(tab_frame, text="알림", 
                                         font=("Arial", 12), width=10,
                                         bg="#333333", fg=self.text_color,
                                         command=self.show_notifications_tab)
        self.notifications_btn.pack(side='left', padx=5)

        self.profile_btn = tk.Button(tab_frame, text="프로필", 
                                   font=("Arial", 12), width=10,
                                   bg="#333333", fg=self.text_color,
                                   command=self.show_profile_tab)
        self.profile_btn.pack(side='left', padx=5)

        # 컨텐츠 영역
        self.content_frame = tk.Frame(main_frame, bg=self.bg_color)
        self.content_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # 기본적으로 피드 탭 표시
        self.show_feed_tab()

        # 업데이트 스레드 시작
        self.start_update_threads()

    def show_feed_tab(self):
        """피드 탭 표시"""
        self.clear_content_frame()
        self.update_tab_buttons("feed")

        # 게시물 작성 영역
        post_frame = tk.Frame(self.content_frame, bg="#111111", relief='solid', bd=1)
        post_frame.pack(fill='x', pady=(0, 10))

        tk.Label(post_frame, text="무슨 일이 일어나고 있나요?", 
                font=("Arial", 12), fg=self.text_color, bg="#111111").pack(anchor='w', padx=10, pady=5)

        self.post_text = tk.Text(post_frame, height=3, font=("Arial", 11), 
                                bg="#222222", fg=self.text_color, insertbackground=self.text_color)
        self.post_text.pack(fill='x', padx=10, pady=5)

        post_btn = tk.Button(post_frame, text="게시", 
                           font=("Arial", 11), width=8,
                           bg=self.accent_color, fg="white",
                           command=self.post_message)
        post_btn.pack(anchor='e', padx=10, pady=5)

        # 피드 영역
        feed_label = tk.Label(self.content_frame, text="피드", 
                             font=("Arial", 14, "bold"), 
                             fg=self.text_color, bg=self.bg_color)
        feed_label.pack(anchor='w', pady=(10, 5))

        # 스크롤 가능한 피드
        self.feed_frame = scrolledtext.ScrolledText(self.content_frame, 
                                                   bg="#111111", fg=self.text_color,
                                                   font=("Arial", 10),
                                                   state='disabled')
        self.feed_frame.pack(fill='both', expand=True)

        # 피드 로드
        self.load_feed()

    def show_notifications_tab(self):
        """알림 탭 표시"""
        self.clear_content_frame()
        self.update_tab_buttons("notifications")

        # 알림 제목
        notif_label = tk.Label(self.content_frame, text="알림", 
                              font=("Arial", 14, "bold"), 
                              fg=self.text_color, bg=self.bg_color)
        notif_label.pack(anchor='w', pady=(0, 10))

        # 알림 리스트
        self.notifications_frame = scrolledtext.ScrolledText(self.content_frame, 
                                                           bg="#111111", fg=self.text_color,
                                                           font=("Arial", 10),
                                                           state='disabled')
        self.notifications_frame.pack(fill='both', expand=True)

        # 알림 로드
        self.load_notifications()

    def show_profile_tab(self):
        """프로필 탭 표시"""
        self.clear_content_frame()
        self.update_tab_buttons("profile")

        # 프로필 정보
        profile_label = tk.Label(self.content_frame, text=f"@{self.username}", 
                                font=("Arial", 18, "bold"), 
                                fg=self.text_color, bg=self.bg_color)
        profile_label.pack(pady=20)

        # 로그아웃 버튼
        logout_btn = tk.Button(self.content_frame, text="로그아웃", 
                             font=("Arial", 12), width=15,
                             bg="#333333", fg=self.text_color,
                             command=self.logout)
        logout_btn.pack(pady=10)

    def update_tab_buttons(self, active_tab):
        """탭 버튼 상태 업데이트"""
        buttons = {
            "feed": self.feed_btn,
            "notifications": self.notifications_btn,
            "profile": self.profile_btn
        }

        for tab, btn in buttons.items():
            if tab == active_tab:
                btn.configure(bg=self.accent_color, fg="white")
            else:
                btn.configure(bg="#333333", fg=self.text_color)

    def clear_screen(self):
        """화면 초기화"""
        for widget in self.root.winfo_children():
            widget.destroy()

    def clear_content_frame(self):
        """컨텐츠 프레임 초기화"""
        if hasattr(self, 'content_frame'):
            for widget in self.content_frame.winfo_children():
                widget.destroy()

    def connect_to_server(self):
        """서버에 연결"""
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            self.connected = True

            # 서버 메시지 수신 스레드 시작
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True
            receive_thread.start()

            return True
        except Exception as e:
            messagebox.showerror("연결 오류", f"서버에 연결할 수 없습니다: {e}")
            return False

    def receive_messages(self):
        """서버로부터 메시지 수신"""
        while self.connected:
            try:
                data = self.socket.recv(1024).decode('utf-8')
                if data:
                    message = json.loads(data)
                    self.handle_server_message(message)
            except Exception as e:
                if self.connected:
                    print(f"메시지 수신 오류: {e}")
                break

    def handle_server_message(self, message):
        """서버 메시지 처리"""
        msg_type = message.get('type')

        if msg_type == 'new_post_notification':
            # 새 게시물 알림 - 피드 새로고침
            if self.current_screen == "main" and hasattr(self, 'feed_frame'):
                self.root.after(0, self.load_feed)

    def send_message(self, message):
        """서버에 메시지 전송"""
        try:
            if self.connected and self.socket:
                self.socket.send(json.dumps(message).encode('utf-8'))
                return True
        except Exception as e:
            print(f"메시지 전송 오류: {e}")
            return False

    def register(self):
        """회원가입"""
        username = self.reg_username_entry.get().strip()
        email = self.reg_email_entry.get().strip()
        password = self.reg_password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("오류", "사용자 이름과 비밀번호를 입력하세요.")
            return

        if not self.connect_to_server():
            return

        message = {
            'type': 'register',
            'username': username,
            'email': email,
            'password': password
        }

        if self.send_message(message):
            # 응답 대기
            try:
                response_data = self.socket.recv(1024).decode('utf-8')
                response = json.loads(response_data)

                if response.get('status') == 'success':
                    messagebox.showinfo("성공", response.get('message'))
                    self.create_login_screen()
                else:
                    messagebox.showerror("오류", response.get('message'))
            except Exception as e:
                messagebox.showerror("오류", f"서버 응답 오류: {e}")

    def login(self):
        """로그인"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("오류", "사용자 이름과 비밀번호를 입력하세요.")
            return

        if not self.connect_to_server():
            return

        message = {
            'type': 'login',
            'username': username,
            'password': password
        }

        if self.send_message(message):
            # 응답 대기
            try:
                response_data = self.socket.recv(1024).decode('utf-8')
                response = json.loads(response_data)

                if response.get('status') == 'success':
                    self.username = username
                    self.create_main_screen()
                else:
                    messagebox.showerror("오류", response.get('message'))
                    self.disconnect()
            except Exception as e:
                messagebox.showerror("오류", f"서버 응답 오류: {e}")
                self.disconnect()

    def post_message(self):
        """게시물 작성"""
        content = self.post_text.get('1.0', tk.END).strip()
        if not content:
            messagebox.showwarning("경고", "내용을 입력하세요.")
            return

        message = {
            'type': 'post',
            'username': self.username,
            'content': content
        }

        if self.send_message(message):
            self.post_text.delete('1.0', tk.END)
            # 피드 새로고침
            self.load_feed()

    def load_feed(self):
        """피드 로드"""
        message = {
            'type': 'get_feed',
            'username': self.username
        }

        if self.send_message(message):
            try:
                response_data = self.socket.recv(1024).decode('utf-8')
                response = json.loads(response_data)

                if response.get('type') == 'feed':
                    self.display_feed(response.get('posts', []))
            except Exception as e:
                print(f"피드 로드 오류: {e}")

    def display_feed(self, posts):
        """피드 표시"""
        if hasattr(self, 'feed_frame'):
            self.feed_frame.config(state='normal')
            self.feed_frame.delete('1.0', tk.END)

            if not posts:
                self.feed_frame.insert(tk.END, "아직 게시물이 없습니다.\n")
            else:
                for post in posts:
                    post_text = f"@{post['username']}\n"
                    post_text += f"{post['content']}\n"
                    post_text += f"💕 {post['likes']} · {post['timestamp']}\n"
                    post_text += "-" * 40 + "\n\n"
                    self.feed_frame.insert(tk.END, post_text)

            self.feed_frame.config(state='disabled')

    def load_notifications(self):
        """알림 로드"""
        message = {
            'type': 'get_notifications',
            'username': self.username
        }

        if self.send_message(message):
            try:
                response_data = self.socket.recv(1024).decode('utf-8')
                response = json.loads(response_data)

                if response.get('type') == 'notifications':
                    self.display_notifications(response.get('notifications', []))
            except Exception as e:
                print(f"알림 로드 오류: {e}")

    def display_notifications(self, notifications):
        """알림 표시"""
        if hasattr(self, 'notifications_frame'):
            self.notifications_frame.config(state='normal')
            self.notifications_frame.delete('1.0', tk.END)

            if not notifications:
                self.notifications_frame.insert(tk.END, "새로운 알림이 없습니다.\n")
            else:
                for notif in notifications:
                    notif_text = f"🔔 {notif['message']}\n"
                    notif_text += f"   {notif['time']}\n\n"
                    self.notifications_frame.insert(tk.END, notif_text)

            self.notifications_frame.config(state='disabled')

    def start_update_threads(self):
        """업데이트 스레드들 시작"""
        self.update_threads_running = True

        # 피드 업데이트 스레드
        feed_thread = threading.Thread(target=self.feed_update_worker)
        feed_thread.daemon = True
        feed_thread.start()

        # 알림 업데이트 스레드
        notification_thread = threading.Thread(target=self.notification_update_worker)
        notification_thread.daemon = True
        notification_thread.start()

    def feed_update_worker(self):
        """피드 업데이트 워커"""
        while self.update_threads_running:
            time.sleep(10)  # 10초마다 업데이트
            if self.current_screen == "main" and hasattr(self, 'feed_frame'):
                self.root.after(0, self.load_feed)

    def notification_update_worker(self):
        """알림 업데이트 워커"""
        while self.update_threads_running:
            time.sleep(15)  # 15초마다 업데이트
            if self.current_screen == "main" and hasattr(self, 'notifications_frame'):
                self.root.after(0, self.load_notifications)

    def logout(self):
        """로그아웃"""
        self.disconnect()
        self.username = None
        self.current_screen = "login"
        self.update_threads_running = False
        self.create_login_screen()

    def disconnect(self):
        """서버 연결 해제"""
        self.connected = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            self.socket = None

    def run(self):
        """앱 실행"""
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        """앱 종료 처리"""
        self.update_threads_running = False
        self.disconnect()
        self.root.destroy()

if __name__ == "__main__":
    app = ThreadsClient()
    app.run()
