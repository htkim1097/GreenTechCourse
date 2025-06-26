import tkinter as tk
import pandas as pd
from tkinter import ttk, filedialog ,messagebox
import numpy as np

window = tk.Tk()
window.title("CSV 분석")
window.geometry("1500x800")
frame = tk.Frame(window)
frame.pack(side='top')

tree = None
file_data = pd.DataFrame()
current_data = pd.DataFrame()
round_data = pd.DataFrame()
stats_data = pd.DataFrame()
history=[]



#뒤로가기용 저장함수
def before_history():
    global current_data
    history.append(current_data.copy())


#뒤로가기
def undo():
    global file_data
    if len(history) > 0:
        file_data = history[-1]
        del history[-1]
        treeview(file_data)


#데이터로드
def load_data(filename):
    global file_data
    file_data = pd.read_csv(filename)

#csv오픈함수
def open_csv():
    file_path = filedialog.askopenfilename(
        title="CSV 파일 선택",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        load_data(file_path)
        filename_label.config(text=f"현재 파일: {file_path}")

# CSV로 파일 저장 기능(저장 버튼)
def save_to_csv():
    global file_data,round_data,stats_data

    file_path = filedialog.asksaveasfilename(
        defaultextension='*.csv',
        title="CSV 파일로 저장",
        filetypes=[("CSV files", "*.csv")]
    )
    if file_path:
        if round_data is not None:
            round_data.to_csv(file_path, index=False, encoding='utf-8-sig')
        elif stats_data is not None:
            stats_data.to_csv(file_path, index=False, encoding='utf-8-sig')
        else:
            file_data.to_csv(file_path, index=False, encoding='utf-8-sig')



def show_data():
    global file_data
    treeview(file_data)

#트리뷰 변환함수
def treeview(df):
    global tree,current_data
    current_data = df
    if tree is not None:
        tree.destroy()

    tree = ttk.Treeview(window)
    tree['columns'] = list(df.columns)
    tree['show'] = 'headings'

    for col in df.columns: #df.columns는 열값
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')
    for row in df.values.tolist(): #df.values.tolist() 행데이터 2차원 리스트화
        tree.insert('', 'end', values=row)

    tree.pack(fill='both', expand=1)



#결측치 함수
def missing_data():
    global file_data
    if file_data is None:
        return
    ok_cancel = messagebox.askokcancel("확인 질문", "변경 사항을 저장하시겠습니까?")
    if not ok_cancel:
        return
    else:
        before_history()
        file_data = file_data.dropna()
        treeview(file_data)

#이상치 함수
def outlier():
    global file_data
    if file_data is None:
        return
    ok_cancel = messagebox.askokcancel("확인 질문", "변경 사항을 저장하시겠습니까?")
    if not ok_cancel: #취소 누를 시 되돌아가기.
        return
    else:
        before_history()
        for col in list(file_data):
           try:
                pct25 = file_data[col].quantile(0.25)
                pct75 = file_data[col].quantile(0.75)
                iqr = pct75 - pct25
                lower = pct25 - 1.5 * iqr
                higher = pct75 + 1.5 * iqr
                file_data[col] = np.where((file_data[col]>higher)|(file_data[col]<lower),np.nan,file_data[col])
           except:
               continue


    treeview(file_data)

def search_text():
    global file_data

    before_history()
    keyword = entry.get()

    if keyword == "": #검색어 없을 시
        result_label.config(text="검색어를 입력하세요.")
        return

    result_rows = []
    arr = file_data.values #넘파이 배열, 2차원리스트

    for i in range(len(arr)):
        row = arr[i]
        for t in row:
            if keyword in str(t):
                result_rows.append(list(row))  # 리스트 변환
                break

    # 검색 결과 없을시
    if len(result_rows) == 0:
        result_label.config(text="검색 결과 없음")

        empty_df = pd.DataFrame(columns=file_data.columns)
        file_data = empty_df
        treeview(file_data)

    else:
        result_label.config(text="검색 결과: " + str(len(result_rows)) + "개")
        filtered_df = pd.DataFrame(result_rows, columns=file_data.columns)
        file_data = filtered_df
        treeview(file_data)


def show_stats():
    global file_data,stats_data
    if file_data is None:
        return

    before_history() #뒤로가기용 저장함수

    stats_df = file_data.describe().transpose() # describe통계요약, transpose행열도치

    if 'count' in stats_df.columns: # count열이 들어있으면 count열 제거.
        stats_df.pop('count')
    cols = file_data.columns # 파일데이터 열

    stats_df['대기오염물질'] = cols[1:] # cols의 맨앞줄빼고가져오기(이데이터에선 날짜)

    stats_df.insert(0, '대기오염물질', stats_df.pop('대기오염물질')) # 원래의 대기오염물질 열 삭제-> 0번자리에 대기오염물질 열 insert

    stats_data=stats_df

    treeview(stats_data)


# 소수점 제한 기능 (제한 버튼)

def rounded():
    global file_data,round_data
    selected = decimal_combo.get()
    decimals = int(selected[0])
    before_history()


    round_data  = current_data.round(decimals)
    treeview(round_data)


#조건,분기문 통해서
#1번, 근사치->통계를 눌렀을때 통계값이 바뀐근사치에 영향을 받지 않게.
#2번, 근사치->다른 버튼 눌렀을 때 근사치로 처음 표현했던 숫자 형태가 그대로 유지되게.


#raised ridge solid groove sunken flat
button_relief="raised"
button_width=15
button_height=4
#버튼
filename_label = tk.Label(window, text="현재 파일:",fg="red",relief="groove")
filename_label.pack(pady=5)

open_button = tk.Button(frame, text="파일 열기", command=open_csv ,width=button_width,height=button_height,relief=button_relief)
open_button.pack(side='left',fill=tk.X, padx=5)

print_button = tk.Button(frame, text="파일 출력", command=show_data,width=button_width,height=button_height,relief=button_relief)
print_button.pack(side='left',fill=tk.X, padx=5)

save_to_csv_button = tk.Button(frame, text="파일 저장", command=save_to_csv,width=button_width,height=button_height,relief=button_relief)
save_to_csv_button.pack(side='left',fill=tk.X, padx=5)

outlier_button = tk.Button(frame, text="이상치 제거", command=outlier,width=button_width,height=button_height,relief=button_relief)
outlier_button.pack(side='left',fill=tk.X, padx=5)

missing_data_button = tk.Button(frame, text="결측치 제거", command=missing_data,width=button_width,height=button_height,relief=button_relief)
missing_data_button.pack(side='left',fill=tk.X, padx=5)

stats_button = tk.Button(frame, text="통계", command=show_stats,width=button_width,height=button_height,relief=button_relief)
stats_button.pack(side='left',fill=tk.X, padx=5)

undo_button = tk.Button(frame, text="뒤로가기", command=undo,width=button_width,height=button_height,relief=button_relief)
undo_button.pack(side='left',fill=tk.X, padx=5)

entry = tk.Entry(frame,relief="solid")
entry.pack(side='left', padx=5)

search_button = tk.Button(frame, text="검색", command=search_text,width=button_width,height=button_height,relief=button_relief)
search_button.pack(side='left', padx=5)

decimal_combo=tk.ttk.Combobox(frame, values=['1자리','2자리','3자리','4자리','5자리'],state='readonly')
decimal_combo.pack(side='left',padx=5)
decimal_combo.set("소숫점 자릿수 선택")

limit_button = tk.Button(frame, text="선택", command=rounded, width=button_width, height=button_height, relief=button_relief)
limit_button.pack(side='left', padx=5)

result_label = tk.Label(window, text="")
result_label.pack(pady=5)

window.mainloop()



