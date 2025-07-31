import threading
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import socket

DATA_TYPE_LIST = {
    "DB": 0,
    "Table": 1,
    "Row": 2
}

ACTION_TYPE_LIST = {
    "생성": 0,
    "조회": 1,
    "삭제": 2
}

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
t1 = None
db_list = []
table_list = []
row_list = []

btn_click_info ={
    "who" : -1,
    "action" : -1
}

def connect_to_server():
    host = en_host.get()
    if host == "" or None:
        messagebox.showerror("값 오류", f"서버 주소를 입력해주세요.")
        return

    port = en_port.get()
    if port == "" or None:
        messagebox.showerror("값 오류", f"포트 번호를 입력해주세요.")
        return
    port = int(port)

    try:
        global client_socket
        global connected

        lb_conn_status.configure(text="연결 중...", foreground="blue")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        connected = True

        lb_conn_status.configure(text="연결됨", foreground="green")

        messagebox.showinfo("연결 성공", f"{host}:{port} 서버에 성공적으로 연결되었습니다.")

    except Exception as e:
        connected = False
        lb_conn_status.configure(text="연결 안됨", foreground="red")
        client_socket.close()
        messagebox.showerror("연결 실패", f"서버 연결에 실패했습니다: {str(e)}")

def on_click_btn(data_type, action_type):
    global btn_click_info
    btn_click_info["who"] = -1
    btn_click_info["action"] = -1

    if data_type == DATA_TYPE_LIST["DB"]:
        btn_click_info["who"] = DATA_TYPE_LIST["DB"]

        if action_type == ACTION_TYPE_LIST["생성"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["생성"]

            # create database 이름;
            s = tk.simpledialog.askstring('생성', 'DB 이름 입력')

            if s != "":
                send_query(f"create database {s}")

        # 조회
        elif action_type == ACTION_TYPE_LIST["조회"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["조회"]

            # show databases;
            send_query("show databases;")

        # 삭제
        elif action_type == ACTION_TYPE_LIST["삭제"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["삭제"]

            sel = listbox_db.curselection()
            print("선택한 db", sel)

            # drop database if exists 이름;
            if len(sel) > 0:
                send_query(f"drop database if exists {listbox_db.get(sel[0])};")

    # Table
    elif data_type == DATA_TYPE_LIST["Table"]:
        btn_click_info["who"] = DATA_TYPE_LIST["Table"]

        # 생성
        if action_type == ACTION_TYPE_LIST["생성"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["생성"]

            # create table 이름 (열이름 자료형 속성);
            s = tk.simpledialog.askstring('생성', '테이블 생성 쿼리를 입력해주세요.\n=> create table 이름 (열이름 자료형 속성);')

            if s != "":
                send_query(s)

        # 조회
        elif action_type == ACTION_TYPE_LIST["조회"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["조회"]

            # show tables;
            send_query("show tables;")

        # 삭제
        elif action_type == ACTION_TYPE_LIST["삭제"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["삭제"]

            sel = listbox_table.curselection()
            print("선택한 테이블", sel)

            # drop table 이름;
            if len(sel) > 0:
                send_query(f"drop table if exists {listbox_table.get(sel)};")

    # Row
    elif data_type == DATA_TYPE_LIST["Row"]:
        btn_click_info["who"] = DATA_TYPE_LIST["Row"]

        # 생성
        if action_type == ACTION_TYPE_LIST["생성"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["생성"]

            s = tk.simpledialog.askstring('생성', '데이터 생성 쿼리를 입력해주세요.\ninsert into 테이블이름 values (열_값)                         ')
            # insert into 테이블이름 values (열 값들);
            if s != "":
                send_query(s)

        # 조회
        # 모든 행과 열을 조회 또는 사용자가 쿼리문 작성
        elif action_type == ACTION_TYPE_LIST["조회"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["조회"]

            s = tk.simpledialog.askstring('조회', '데이터 조회 쿼리를 입력해주세요.\n=> select 열_이름 from 테이블_이름 where 조건식                         ')

            # select * from 이름;
            if s != "":
                send_query(s)

        # 삭제
        # treeview에서 선택한 행 삭제
        elif action_type == ACTION_TYPE_LIST["삭제"]:
            btn_click_info["action"] = ACTION_TYPE_LIST["삭제"]

            s = tk.simpledialog.askstring('조회','데이터 삭제 쿼리를 입력해주세요.\n=> drop table 이름                         ')

            # drop table 이름;
            if s != "":
                send_query(s)

def send_query(query):
    try:
        client_socket.send(query.encode())
    except Exception as e:
        print("send_query() 오류", e)

def recv_data():
    while True:
        global connected
        try:
            if connected:
                data = client_socket.recv(1024)
                d_data = data.decode()
                d_data_list = d_data.split('\n')
                print("서버로부터 받은 데이터: ", d_data_list)

                if d_data_list[0] == "complete":
                    pass
                    # messagebox.showinfo("성공", "작업이 완료됐습니다.")
                else:
                    show_list(d_data_list)

        except WindowsError:
            print("소켓 통신 오류")
            connected = False
            lb_conn_status.configure(text="연결 안됨", foreground="red")
            client_socket.close()
            return

        except Exception as e:
            print("recv_data() 오류", e)

def show_list(data=None):
    try:
        who = btn_click_info["who"]

        if who == DATA_TYPE_LIST["DB"]:
            listbox_db.delete(0, "end")

            if data[0] != "complete":
                global db_list
                db_list = data
            else:
                db_list = []
            for i, d in enumerate(db_list):
                if len(db_list) == i + 1:
                    break
                listbox_db.insert(i, d)

        elif who == DATA_TYPE_LIST["Table"]:
            listbox_table.delete(0, "end")

            if data[0] != "complete":
                global table_list
                table_list = data
            else:
                table_list = []

            for i, d in enumerate(data):
                if len(data) == i + 1:
                    break
                listbox_table.insert(i, d)

        elif who == DATA_TYPE_LIST["Row"]:
            listbox_row.delete(0, "end")

            if data[0] != "complete":
                global row_list
                row_list = data
            else:
                row_list = []

            for i, d in enumerate(data):
                if len(data) == i + 1:
                    break
                listbox_row.insert(i, d)

    except Exception as e:
        print("show_list() 오류", e)

def on_selected_db(e):
    s = listbox_db.curselection()
    if len(s) > 0:
        send_query(f"use {listbox_db.get(s)}")
        listbox_table.delete(0, "end")
        listbox_row.delete(0, "end")
        on_click_btn(DATA_TYPE_LIST["Table"], ACTION_TYPE_LIST["조회"])

def on_selected_table(e):
    s = listbox_table.curselection()
    if len(s) > 0:
        listbox_row.delete(0, "end")
        btn_click_info["who"] = DATA_TYPE_LIST["Row"]
        btn_click_info["action"] = ACTION_TYPE_LIST["조회"]
        print(listbox_table.get(s))
        send_query(f"select * from {listbox_table.get(s)}")

win = tk.Tk()
win.title("DB Gui")
win.geometry("1000x600")

frame_conn = tk.Frame(win)
frame_conn.pack(fill='x', side="top")

lb_host = tk.Label(frame_conn, text="서버 주소")
lb_host.pack(side="left", padx=(5, 0))

host_var = tk.StringVar(value="192.168.0.4")  # 테스트용
en_host = tk.Entry(frame_conn, textvariable=host_var)
en_host.pack(side="left", padx=(5, 0))

lb_port = tk.Label(frame_conn, text="포트 번호")
lb_port.pack(side="left", padx=(15, 0))

port_var = tk.StringVar(value="8080")  # 테스트용
en_port = tk.Entry(frame_conn, textvariable=port_var)
en_port.pack(side="left", padx=(5, 0))

btn_conn = tk.Button(frame_conn, text="연결", command= connect_to_server)
btn_conn.pack(side="left", padx=(5, 0))

lb_conn_status = tk.Label(frame_conn, text="연결 안됨", foreground="red")
lb_conn_status.pack(side="left", padx=(5, 0))

frame_input = tk.Frame(win, padx=10, pady=10)
frame_input.pack(fill='x', pady=(50, 0), padx=(200, 0))

# 출력 프레임
frame_output = tk.Frame(win)
frame_output.pack(fill='both', side="bottom", expand=True)

# ---------- db 리스트 박스 
frame_db = tk.Frame(frame_output)
frame_db.pack(side="left", fill="both", expand=1)

frame_db_btns = tk.Frame(frame_db)
frame_db_btns.pack(side="top", fill="x")

lb_db_listbox = tk.Label(frame_db_btns, text="DB")
lb_db_listbox.pack(side="left", padx=(5, 0))

# DB 생성 버튼
btn_create_db = tk.Button(frame_db_btns, text="생성", command=lambda : on_click_btn(DATA_TYPE_LIST["DB"], ACTION_TYPE_LIST["생성"]))
btn_create_db.pack(side="right", padx=(5,0))

# DB 조회 버튼
btn_show_db = tk.Button(frame_db_btns, text="조회", command=lambda : on_click_btn(DATA_TYPE_LIST["DB"], ACTION_TYPE_LIST["조회"]))
btn_show_db.pack(side="right", padx=(5,0))

# DB 삭제 버튼
btn_drop_db = tk.Button(frame_db_btns, text="삭제", command=lambda : on_click_btn(DATA_TYPE_LIST["DB"], ACTION_TYPE_LIST["삭제"]))
btn_drop_db.pack(side="right", padx=(5,0))

# DB 리스트 박스
listbox_db = tk.Listbox(frame_db, bg="lightgray", selectmode="single")
listbox_db.bind("<<ListboxSelect>>", on_selected_db)
listbox_db.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

# ---------- 테이블 리스트 박스 
frame_table = tk.Frame(frame_output)
frame_table.pack(side="left", fill="both", expand=1)

frame_table_btns = tk.Frame(frame_table)
frame_table_btns.pack(side="top", fill="x")

lb_table_listbox = tk.Label(frame_table_btns, text="테이블")
lb_table_listbox.pack(side="left", padx=(5, 0))

# 테이블 생성 버튼
btn_create_table = tk.Button(frame_table_btns, text="생성", command=lambda : on_click_btn(DATA_TYPE_LIST["Table"], ACTION_TYPE_LIST["생성"]))
btn_create_table.pack(side="right", padx=(5,0))

# 테이블 조회 버튼
btn_show_table = tk.Button(frame_table_btns, text="조회", command=lambda : on_click_btn(DATA_TYPE_LIST["Table"], ACTION_TYPE_LIST["조회"]))
btn_show_table.pack(side="right", padx=(5,0))

# 테이블 삭제 버튼
btn_drop_table = tk.Button(frame_table_btns, text="삭제", command=lambda : on_click_btn(DATA_TYPE_LIST["Table"], ACTION_TYPE_LIST["삭제"]))
btn_drop_table.pack(side="right", padx=(5,0))

# 테이블 리스트 박스
listbox_table = tk.Listbox(frame_table, bg="lightgray", selectmode="single")
listbox_table.bind("<<ListboxSelect>>", on_selected_table)
listbox_table.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

# ---------- 행 데이터 리스트 박스 
frame_row = tk.Frame(frame_output)
frame_row.pack(side="left", fill="both", expand=1)

frame_row_btns = tk.Frame(frame_row)
frame_row_btns.pack(side="top", fill="x")

lb_row_listbox = tk.Label(frame_row_btns, text="행 데이터")
lb_row_listbox.pack(side="left", padx=(5, 0))

# 행 생성 버튼
btn_insert_row = tk.Button(frame_row_btns, text="생성", command=lambda : on_click_btn(DATA_TYPE_LIST["Row"], ACTION_TYPE_LIST["생성"]))
btn_insert_row.pack(side="right", padx=(5,0))

# 행 조회 버튼
btn_show_row = tk.Button(frame_row_btns, text="조회", command=lambda : on_click_btn(DATA_TYPE_LIST["Row"], ACTION_TYPE_LIST["조회"]))
btn_show_row.pack(side="right", padx=(5,0))

# 행 삭제 버튼
btn_drop_row = tk.Button(frame_row_btns, text="삭제", command=lambda : on_click_btn(DATA_TYPE_LIST["Row"], ACTION_TYPE_LIST["삭제"]))
btn_drop_row.pack(side="right", padx=(5,0))

# 행 리스트 박스
listbox_row = tk.Listbox(frame_row, bg="lightgray", selectmode="single", height=0)
listbox_row.pack(side="bottom", fill="both", expand=True, padx=5, pady=5)

if __name__ == "__main__":
    t1 = threading.Thread(target=recv_data)
    t1.start()
    win.mainloop()

    if t1.is_alive():
        t1.join()

    if client_socket is not None:
        client_socket.close()
