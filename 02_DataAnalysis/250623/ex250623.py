# import tkinter as tk
# import csv
# from tkinter import filedialog
#
# window = tk.Tk()
# window.geometry("300x300")
#
# def opencsv():
#     file_path = filedialog.askopenfilename(
#         title='CSV파일선택',
#         filetypes=[('CSV files', '*csv')]
#     )
#
#     if file_path:
#         with open(file_path, newline='', encoding='utf-8') as csvfile:
#             reader = csv.reader(csvfile)
#             for row in reader:
#                 print(row)
#
# btn_open = tk.Button(window, text='csv 파일 열기', command=opencsv)
# btn_open.pack()
# window.mainloop()
#
#
# import tkinter as tk
# from tkinter import ttk
# import csv
#
# def opencsv(filename):
#     with open(filename, newline='', encoding='utf-8') as csvfile:
#         reader = csv.reader(csvfile)
#         headers = next(reader)
#         tree['columns'] = headers
#         tree['show'] = 'headings'
#
#         for col in headers:
#             tree.heading(col, text=col)
#             tree.column(col, width=100, anchor='center')
#         for row in reader:
#             tree.insert('', 'end', values=row)  # 부모 구조가 필요 없기 때문에 parent 속성은 비워둔다.
#
# window = tk.Tk()
# window.title('test')
# window.geometry("1500x800")
#
# tree = ttk.Treeview(window)
# tree.pack(fill='both', expand=1)
# opencsv("서울_대기오염_데이터_2025.csv")
# window.mainloop()


import tkinter as tk
import csv
from tkinter import filedialog
from tkinter import ttk

def open_csv():
    file_path = filedialog.askopenfilename(
        title='CSV파일선택',
        filetypes=[('CSV files', '*csv')]
    )

    if file_path:
        load_csv(file_path)

def load_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        tree['columns'] = headers
        tree['show'] = 'headings'

        for col in headers:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')
        for row in reader:
            tree.insert('', 'end', values=row)  # 부모 구조가 필요 없기 때문에 parent 속성은 비워둔다.

window = tk.Tk()
window.title('test')
window.geometry("1500x800")

btn_open = tk.Button(window, text='csv 파일 열기', command=open_csv)
btn_open.pack()

tree = ttk.Treeview(window)
tree.pack(fill='both', expand=1)

window.mainloop()


# filedialog 파일 지정(버튼)
# 내용 출력(버튼)
# 이상치 처리(버튼)
# 결측치 처리(버튼)
# 특정 셀 값 검색(entry, 버튼)
# 파일 데이터의 shape 및 통계 요약 출력 버튼
# 파일 저장 기능(버튼)
