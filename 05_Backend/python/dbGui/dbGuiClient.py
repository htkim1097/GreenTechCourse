import tkinter as tk
import tkinter.ttk as ttk
import socket

DATA_TYPE_LIST = {
    0: "DB",
    1: "Table",
    2: "Row"
}

ACTION_TYPE_LIST = {
    0: "생성",
    1: "조회",
    2: "삭제"
}

client_socket = None

def connect_db_server(address, port):
    try:
        global client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((address, port))
    except:
        print("connect_db_server() 오류")
        client_socket.close()

def send_query(query):
    try:
        client_socket.send(query.encode())
    except:
        print("send_query() 오류")
        client_socket.close()

def recv_data():
    try:
        data = client_socket.recv(1024)
        print("서버로부터 받은 데이터: ", data.decode())
    except:
        print("recv_data() 오류")
        client_socket.close()

def show_treeview(data):
    try:
        d_data = data.decode()
        tree['columns'] = "abcd"
        tree['show'] = 'headings'

        # for col in headers:
        #     tree.heading(col, text=col)
        #     tree.column(col, width=100, anchor='center')
        for row in d_data:
            tree.insert('', 'end', values=row)
    except:
        print("show_treeview() 오류")

def on_click_btn_apply():
    data_type = cb_data_type.get()
    action_type = cb_action_type.get()

    query_str = "show databases;"

    # # DB
    # if action_type == ACTION_TYPE_LIST[0]:
    #     # 생성
    #     if data_type == DATA_TYPE_LIST[0]:
    #         # create database 이름;
    #         query_str = "create database 이름;"
    #
    #     # 조회
    #     elif data_type == DATA_TYPE_LIST[1]:
    #         # show databases;
    #         query_str = "show databases;"
    #
    #     # 삭제
    #     elif data_type == DATA_TYPE_LIST[2]:
    #         # drop database if exists 이름;
    #         query_str = "drop database if exists 이름;"
    #
    # # Table
    # elif action_type == ACTION_TYPE_LIST[1]:
    #     # 생성
    #     if data_type == DATA_TYPE_LIST[0]:
    #         # create table 이름 (열이름 자료형 속성);
    #         query_str = "create table 이름 (열이름 자료형 속성);"
    #
    #     # 조회
    #     elif data_type == DATA_TYPE_LIST[1]:
    #         # show tables;
    #         query_str = "show tables;"
    #
    #     # 삭제
    #     elif data_type == DATA_TYPE_LIST[2]:
    #         # drop table 이름;
    #         query_str = "drop table 이름;"
    #
    # # Row
    # elif action_type == ACTION_TYPE_LIST[2]:
    #     # 생성
    #     if data_type == DATA_TYPE_LIST[0]:
    #         # insert into 테이블이름 values (열 값들);
    #         query_str = "insert into 테이블이름 values (열 값들);"
    #
    #     # 조회
    #     # 모든 행과 열을 조회 또는 사용자가 쿼리문 작성
    #     elif data_type == DATA_TYPE_LIST[1]:
    #         # select * from 이름;
    #         query_str = "select * from 테이블이름;"
    #
    #     # 삭제
    #     # treeview에서 선택한 행 삭제
    #     elif data_type == DATA_TYPE_LIST[2]:
    #         # delete from 이름 where 조건;
    #         query_str = "delete from 테이블이름 where 조건;"

    send_query(query_str)

win = tk.Tk()
win.title("DB Gui")
win.geometry("800x600")

frame_conn = tk.Frame(win)
frame_conn.pack(fill='x', side="top")

frame_input = tk.Frame(win, padx=10, pady=10)
frame_input.pack(fill='x', pady=(50, 0), padx=(200, 0))

frame_output = tk.Frame(win, padx=10, pady=10)
frame_output.pack(fill='x',side="bottom")

lb_conn_status = tk.Label(frame_conn, text="")
lb_conn_status.pack()

# DB, 테이블, 행 데이터 선택
cb_data_type = ttk.Combobox(frame_input, state="readonly", values=list(DATA_TYPE_LIST.values()), width=7)
cb_data_type.pack(side="left", padx=(5,0))

# 생성, 조회, 삭제 선택
cb_action_type = ttk.Combobox(frame_input, state="readonly", values=list(ACTION_TYPE_LIST.values()), width=7)
cb_action_type.pack(side="left", padx=(5,0))

# 입력 프레임
frame_detail_inputs = tk.Frame(frame_input)
frame_detail_inputs.pack(side="left", padx=(5,0))

en_main = tk.Entry(frame_detail_inputs, width=30)
en_main.pack()

# 확인 버튼
btn_apply = tk.Button(frame_input, text="확인", width=10, height=1, command=on_click_btn_apply)
btn_apply.pack(side="left", padx=(5,0))

# 출력 창
tree = ttk.Treeview(frame_output, height=20, padding=5)
tree.pack(fill="both", expand=True)

win.mainloop()

connect_db_server("localhost", 8080)