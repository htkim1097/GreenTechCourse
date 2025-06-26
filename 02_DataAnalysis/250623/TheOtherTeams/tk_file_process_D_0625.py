

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.font_manager as fm
import platform

# 한글 폰트 설정
if platform.system() == 'Windows':
   plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
   plt.rcParams['font.family'] = 'AppleGothic'
else:
   plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

file_path = None
df = None
canvas = None

num_cols = ['PM10', 'PM2.5', 'O3', 'NO2', 'SO2', 'CO', '기온(°C)', '습도(%)']

def open_csv():  #todo csv파일열기
    global file_path
    file_path = filedialog.askopenfilename(
        filetypes=[("CSV files", "*.csv")]
    )
    label.config(text=file_path)  # 선택한 파일 경로를 화면에 표시

def load_csv():  #todo 파일읽기
    global file_path, df
    if not file_path:
        return
    df_new = pd.read_csv(file_path)  # 파일에서 데이터를 읽어옴
    df = df_new.copy()               # 읽어온 데이터를 df에 복사해서 저장
    display_data()                   # 표로 화면에 보여줌
    clear_graph()                    # 그래프가 있으면 지움

def display_data():  #todo GUI에 출력
    global df
    if df is None:
        return
    tree.delete(*tree.get_children())  # 기존 표 내용(행들) 모두 지우기
    tree["columns"] = list(df.columns)  # 표의 열 이름을 데이터프레임 열 이름과 똑같이 맞춤
    tree["show"] = "headings"           # 표의 첫 줄에 열 제목만 보이게 함
    for col in df.columns:  # 데이터의 모든 열 이름에 대해 반복 (for문: 열 제목/너비 설정)
        tree.heading(col, text=col)     # 표의 각 열에 제목(열 이름) 붙이기
        tree.column(col, width=100, anchor='center')  # 각 열의 너비를 100, 가운데 정렬
    for _, row in df.iterrows():  # 데이터의 각 행(row)에 대해 반복 (for문: 표에 한 줄씩 추가)
        tree.insert("", "end", values=list(row))  # 데이터 한 줄씩 표에 추가

def outlier_check():  #todo 이상치 개수 확인 창 띄우기
    global df
    if df is None:
        return
    num_df = df[num_cols]
    Q1 = num_df.quantile(0.25)
    Q3 = num_df.quantile(0.75)
    IQR = Q3 - Q1
    # 아래는 "평범한 값의 범위"에서 너무 벗어난 값(이상치)을 True로 표시
    cond = ((num_df < (Q1 - 1.5 * IQR)) | (num_df > (Q3 + 1.5 * IQR)))
    # cond는 값이 이상치면 True, 아니면 False가 들어있는 표
    outlier_count = cond.sum().sum()  # True(이상치)인 값의 개수를 모두 더함
    messagebox.showinfo("이상치 개수", f"이상치: {str(outlier_count)}개")

def outlier_handle():  #todo 이상치 버튼크릭 Nan으로 처리
    global df
    if df is None:
        return
    num_df = df[num_cols]
    Q1 = num_df.quantile(0.25)
    Q3 = num_df.quantile(0.75)
    IQR = Q3 - Q1
    cond = ((num_df < (Q1 - 1.5 * IQR)) | (num_df > (Q3 + 1.5 * IQR)))
    df[num_cols] = num_df.mask(cond)
    display_data()
    clear_graph()

def missing_check():  #todo 결측치 조회하여 갯수를 메시지 박스에 띄움
    global df
    if df is None:
        return
    missing_count = df.isna().sum().sum()  # 빈칸(NaN)인 값만 True로 만들고, 전체 빈칸 개수 세기
    messagebox.showinfo("결측치 개수", f"결측치: {str(missing_count)}개")  # 결과를 창으로 알려줌

def missing_handle():  #todo 결측치 처리
    global df
    if df is None:
        return
    for col in df.columns:  # 데이터의 모든 열에 대해 반복 (for문: 각 열별로 결측치 처리)
        if col in num_cols:  # 숫자 데이터 열이면 (조건문: 숫자/글자 구분)
            df[col] = df[col].fillna(df[col].mean())  # 빈칸(NaN)을 그 열의 평균값으로 채움
        else:  # 글자 데이터 열이면
            df[col] = df[col].fillna('결측')           # 빈칸(NaN)을 '결측'이라는 글씨로 채움
    display_data()  # 표 다시 보여주기
    clear_graph()   # 그래프 지우기

def summary_info():  #todo 통계요약
    global df
    if df is None:  # 데이터를 아직 안 불러왔으면 (조건문: 안전장치)
        return
    # 데이터의 행/열 개수, 통계 요약을 info에 저장
    info = f"행/열 개수: {df.shape}\n\n{df.describe(include='all')}"
    stat_win = tk.Toplevel(root)  # 새로운 창 만들기
    stat_win.title("통계 요약 전체 보기")  # 창 제목
    stat_win.geometry("700x500")  # 창 크기(가로 700, 세로 500)
    #todo Consolas영문가독성 좋지만, 한글가독성 떨어질 한글영문 함께 사용 경우, D2Coding
    text = tk.Text(stat_win, wrap="none", font=("D2Coding", 12))  # 텍스트 창(폰트 크기 12)
    text.pack(side="left", fill="both", expand=True)  # 왼쪽에 붙이고, 창 크기에 맞게 늘림
    text.insert("1.0", info)  # 텍스트 창에 info 내용 넣기
    yscroll = tk.Scrollbar(stat_win, orient="vertical", command=text.yview)  # 세로 스크롤바
    yscroll.pack(side="right", fill="y")
    text.config(yscrollcommand=yscroll.set)
    xscroll = tk.Scrollbar(stat_win, orient="horizontal", command=text.xview)  # 가로 스크롤바
    xscroll.pack(side="bottom", fill="x")
    text.config(xscrollcommand=xscroll.set)

def save_csv():
    global df
    if df is None:  # 데이터를 아직 안 불러왔으면 (조건문: 안전장치)
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".csv")  # 저장할 파일 이름 입력창 띄우기
    if save_path:  # 사용자가 저장 버튼을 눌렀다면 (조건문)
        df.to_csv(save_path, index=False)  # 현재 df를 csv로 저장

def clear_graph():
    global canvas
    if canvas is not None:  # 그래프가 이미 그려져 있다면 (조건문)
        canvas.get_tk_widget().destroy()  # 그래프를 창에서 지움
        canvas = None

def plot_graph():
    global df, canvas
    if df is None:  # 데이터를 아직 안 불러왔으면 (조건문: 안전장치)
        return
    num_df = df[num_cols]  # 숫자 데이터만 뽑기
    if num_df.empty:  # 숫자 데이터가 하나도 없으면 (조건문)
        return
    clear_graph()
    fig, ax = plt.subplots(figsize=(min(1+len(num_df.columns)*2, 12), 4))  # 그래프 크기 조절
    num_df.plot(kind='box', ax=ax)  # 박스플롯(상자그림) 그리기
    ax.set_title("수치형 데이터 박스플롯")  # 그래프 제목
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)  # 그래프를 tkinter 창에 붙임
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)  # 그래프를 프레임에 가득 채움
    plt.close(fig)
    plt.rc('font', family='NanumGothic')

def search():
    # 문자열로 변환된 float64 열만 필터 대상으로 사용 / float_cols의 모든 값을 문자열로 바꿉
    filter_cols = df.select_dtypes(include='float64').astype(str)
    # 셀 값에 입력 문자열이 포함되어 있는지 검사 (Boolean DataFrame)
    mask = filter_cols.applymap(lambda x: search_entry.get() in x)

    row_match = mask.any(axis=1)  # 조건을 만족하는 행(가로줄)이 하나라도 있는 경우
    data = df[row_match] # 원래 DataFrame에서 해당 행만 선택 (전체 열 포함)
    print(data)
    for i in tree.get_children():
        tree.delete(i)
    # for i in range(len(data)):
    #     tree.insert('', 'end', values=data.to_string(index=False, header=False))
    for _, row in data.iterrows():
        tree.insert('', 'end', values=list(row))



root = tk.Tk()  # tkinter로 창 만들기
root.title("CSV 데이터 처리기")  # 창 제목

label = tk.Label(root, text="파일을 선택하세요")  # 파일 경로 보여주는 라벨
label.pack()  # 라벨을 창 위에 배치 (pack: 위에서 아래로 쌓음)

btn_frame = tk.Frame(root)  # 버튼들을 한 줄에 모으는 프레임
btn_frame.pack()            # 프레임을 창에 배치 (pack: 위에서 아래로 쌓음)

# 각 버튼을 한 줄(row=0)에 차례로 배치, column=0부터 오른쪽으로 1씩 증가
tk.Button(btn_frame, text="파일 열기", command=open_csv).grid(row=0, column=0)      # 첫 번째 버튼(파일 열기), 맨 왼쪽
tk.Button(btn_frame, text="출력", command=load_csv).grid(row=0, column=1)           # 두 번째 버튼(출력), 두 번째 칸
tk.Button(btn_frame, text="이상치 조회", command=outlier_check).grid(row=0, column=2)  # 세 번째 버튼(이상치 조회), 세 번째 칸
tk.Button(btn_frame, text="이상치 처리", command=outlier_handle).grid(row=0, column=3) # 네 번째 버튼(이상치 처리), 네 번째 칸
tk.Button(btn_frame, text="결측치 조회", command=missing_check).grid(row=0, column=4)  # 다섯 번째 버튼(결측치 조회), 다섯 번째 칸
tk.Button(btn_frame, text="결측치 처리", command=missing_handle).grid(row=0, column=5) # 여섯 번째 버튼(결측치 처리), 여섯 번째 칸
tk.Button(btn_frame, text="통계요약", command=summary_info).grid(row=0, column=6)      # 일곱 번째 버튼(통계요약), 일곱 번째 칸
tk.Button(btn_frame, text="저장", command=save_csv).grid(row=0, column=7)              # 여덟 번째 버튼(저장), 여덟 번째 칸
tk.Button(btn_frame, text="그래프", command=plot_graph).grid(row=0, column=8)          # 아홉 번째 버튼(그래프), 아홉 번째 칸

search_entry = tk.Entry(root)
search_entry.pack()
search_btn = tk.Button(root, text="검색", command=search)
search_btn.pack()

tree = ttk.Treeview(root, height=15)  # 표(트리뷰), 15줄 보여줌
tree.pack(fill="both", expand=True)   # 창을 꽉 채우도록 배치 (pack: 위에서 아래로 쌓음)

graph_frame = tk.Frame(root)  # 그래프를 보여줄 프레임
graph_frame.pack(fill="both", expand=True)  # 프레임을 창에 꽉 채움 (pack: 위에서 아래로 쌓음)

root.mainloop()  # 창 실행(프로그램 시작)