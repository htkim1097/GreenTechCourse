import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd

import csv
import numpy as np
from prompt_toolkit.clipboard import pyperclip
import pyperclip        # pyperclip 패키지 설치 필요


# GUI 생성
window = tk.Tk()
window.geometry("1300x600")
window.title("CSV 분석 도구")

data = pd.DataFrame()         # 원본 데이터 프레임 저장 변수
data_copy = None              # 원본 데이터 복사본 저장 변수
file_path = None              # 파일 경로 저장 변수
copy_button_created = False   # '복사하기' 버튼 실행 확인용 변수

save_data = pd.DataFrame()    # 버튼 실행 시 갱신되는 데이터 프레임 저장 변수
history = []                  # '이전으로' 버튼 실행 시 되돌릴 데이터 저장 변수


# CSV 파일 열기
def opencsv():
   global data
   global data_copy
   global data_outlier
   global file_path

   file_path = filedialog.askopenfilename(
       title="CSV 파일 선택",
       filetypes=[("CSV files", "*.csv")]
   )

   if file_path:
       try:
           data = pd.read_csv(file_path, encoding='utf-8')
           data_copy = data.copy()
           data_outlier = data.copy()   # 원본 백업
           messagebox.showinfo("성공", f"{file_path} 파일을 성공적으로 불러왔습니다.")
       except Exception as e:
           messagebox.showerror("오류", f"파일을 열 수 없습니다:\n{e}")



# 파일 내용 출력
def show_file():
    global file_path

    # 현재 트리에 있는 모든 자식 노드 삭제
    tree.delete(*tree.get_children())

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)  # CSV 파일을 읽는 reader 객체
        headers = next(reader)        # CSV 파일을 통해 생성된 reader 객체의 첫 줄을 헤더로 설정
        tree['columns'] = headers     # 테이블의 헤더(열 이름)를, 위에서 얻은 headers로 설정
        tree['show'] = 'headings'     # tree 위젯을 테이블 형태로 설정

        for col in headers:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')  # 열의 폭 100, 중앙 정렬
        for row in reader:
            tree.insert('', 'end', values=row)


# 이전으로
def reset_data():
    global history

    if len(history) > 1:
        treeview_update(history[-1])
        del(history[-1])

    else:
        show_file()


# 수정된 결과 tree 출력
def treeview_update(data):

  # 기존 TreeView 내용 삭제
  tree.delete(*tree.get_children())

  # 컬럼 설정
  tree['columns'] = list(data.columns)
  tree['show'] = 'headings'

  for col in data.columns:
      tree.heading(col, text=col)
      tree.column(col, width=100, anchor='center')
  for i in data.index:
      tree.insert('', 'end', values=list(data.loc[i]))


# 선택한 행 값 가져오기
def get_selected_cell():
   selected = tree.focus()

   if not selected:
       result_label.config(text="행을 선택하세요.")
       return

   values = tree.item(selected, 'values')
   result_label.config(text=f"{values}")

   global copy_button_created
   if copy_button_created == False:
       copy_button = tk.Button(button_frame, text="복사하기", command=copy_text, fg='green')
       copy_button.pack()
       copy_button_created = True

# 선택한 행 값 가져오기 -> 복사하기
# 사용 시 pyperclip 패키지 추가 필요
def copy_text():
    text_to_copy = result_label.cget("text")
    pyperclip.copy(text_to_copy)
    messagebox.showinfo("복사 완료", "복사가 완료되었습니다.")


# 이상치 처리 기능
def outlier_replace():
    global data
    global data_outlier
    global save_data

    # 데이터 프레임에서 숫자만 추출
    target_cols = list(data.select_dtypes(include='number').columns)

    # 이상치 값 처리
    pct25 = data[target_cols].quantile(0.25)
    pct75 = data[target_cols].quantile(0.75)
    iqr = pct75 - pct25
    lower = pct25 - 1.5 * iqr
    upper = pct75 + 1.5 * iqr

    # 이상치에 Nan 부여
    data[target_cols] = np.where( (data[target_cols] < lower) | (data[target_cols] > upper), np.nan, data[target_cols] )

    # 이상치 처리 출력용 data_outlier
    target_cols_copy = list(data_outlier.select_dtypes(include='number').columns)
    pct25_copy = data_outlier[target_cols_copy].quantile(0.25)
    pct75_copy = data_outlier[target_cols_copy].quantile(0.75)
    iqr_copy = pct75_copy - pct25_copy
    lower_copy = pct25_copy - 1.5 * iqr_copy
    upper_copy = pct75_copy + 1.5 * iqr_copy
    data_outlier[target_cols_copy] = np.where( (data_outlier[target_cols_copy] < lower_copy) | (data_outlier[target_cols_copy] > upper_copy), np.nan, data_outlier[target_cols_copy] )

    treeview_update(data_outlier)
    save_data = data_outlier.copy()
    history.append(save_data)



# 결측치 처리 기능
def missing_replace():
  global data
  global save_data

  data = data.dropna()        # 결측치 행 제거
  treeview_update(data)

  save_data = data.copy()
  history.append(save_data)


# 통계 요약 출력
def show_summary():
   global save_data

   if data is not None:
       # transpose() = 행, 열 바꿈
       summary_df = data.describe().transpose().reset_index()
       summary_df.rename(columns={'index': '열 이름'}, inplace=True)
       treeview_update(summary_df)
       save_data = summary_df.copy()
       history.append(save_data)
   else:
       messagebox.showwarning("경고", "먼저 CSV 파일을 열어주세요.")


# CSV 데이터 출력
def reshow_file():
   if data is not None:
       treeview_update(data)
   else:
       messagebox.showwarning("경고", "먼저 CSV 파일을 열어주세요.")


# 검색 기능
def search_treeview():
   global data, data_copy

   if data is None:
       messagebox.showwarning("경고", "먼저 CSV 파일을 열어주세요.")
       return

   # nan 값 검색할 때
   query = search_entry.get().lower().strip()

   if not query:                    # 검색창이 비어있다면
       treeview_update(data_copy)   # 원본 출력
       return

   matched_rows = []
   columns = list(data.columns)

   for i in range(len(data)):
       row = data.iloc[i]
       for col in columns:
           cell_value = row[col]
           # 결측치 NaN이면 str(cell_value) = 'nan'이지만 그대로 처리
           if query in str(cell_value).lower():
               matched_rows.append(list(row))
               break

   data_copy = pd.DataFrame(matched_rows, columns=columns)
   treeview_update(data_copy)


# csv 파일 저장
def save_csv():
    global save_data

    if save_data is not None:
        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="CSV 파일 저장"
        )
        if save_path:
            try:
                save_data.to_csv(save_path, index=False, encoding='utf-8')
                messagebox.showinfo("성공", f"{save_path} 파일로 저장되었습니다.")
            except Exception as e:
                messagebox.showerror("오류", f"파일 저장 중 오류 발생:\n{e}")
    else:
        messagebox.showwarning("경고", "저장할 데이터가 없습니다. 먼저 CSV 파일을 열어주세요.")



# 선택된 행 삭제
def delete_selected_row():
    selected_item = tree.selection()  # 현재 선택된 행의 ID (튜플)
    if selected_item:
        confirm = messagebox.askyesno("확인", "선택한 행을 삭제하시겠습니까?")
        if confirm:
            for item in selected_item:
                tree.delete(item)




# 월별 통계
def open_new_window():
    global data, save_data
    date_df = data.copy()

    date_df['날짜'] = pd.to_datetime(date_df['날짜']) # 날짜 데이터로 변경
    date_df['월'] = date_df['날짜'].dt.month.astype(str)

    date_df = date_df.groupby('월', as_index = False).agg(['mean'])

    #열을 삭제할 수준을 지정
    date_df = date_df.drop(columns='날짜', axis=1, level=0)

    treeview_update(date_df)
    save_data = date_df.copy()
    history.append(save_data)




# ---- GUI 설정 ----

button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP, fill='x', pady=10)

delete_frame = tk.Frame(window)
delete_frame.pack(side=tk.TOP, fill='x')

#파일 열기
open_button = tk.Button(button_frame, text="CSV 파일 열기", command=opencsv)
open_button.pack(side=tk.LEFT, padx=5)

#파일 출력
print_button = tk.Button(button_frame, text="CSV 파일 출력", command=show_file)
print_button.pack(side=tk.LEFT, padx=5)

# 이상치 처리 버튼
outlier_button = tk.Button(button_frame, text="이상치 처리", command=outlier_replace)
outlier_button.pack(side=tk.LEFT, padx=5)

# 결측치 처리 버튼
missing_button = tk.Button(button_frame, text="결측치 처리", command=missing_replace)
missing_button.pack(side=tk.LEFT, padx=5)

#통계 요약
summary_button = tk.Button(button_frame, text="통계 요약 보기", command=show_summary)
summary_button.pack(side=tk.LEFT, padx=5)

#파일 저장
save_button = tk.Button(button_frame, text="CSV 파일 저장", command=save_csv)
save_button.pack(side=tk.LEFT, padx=5)

#선택한 셀 값 가져오기
get_cell_button = tk.Button(button_frame, text="선택 행의 전체값 가져오기", command=get_selected_cell)
get_cell_button.pack(side=tk.LEFT, padx=5)

# 월별 통계 출력 윈도우 창
month_button = tk.Button(button_frame, text="월별 통계 확인", command=open_new_window)
month_button.pack(side=tk.LEFT, padx=5)

# 결과 표시용 레이블
result_label = tk.Label(window, text="", fg="green")
result_label.pack(pady=5)

# 행 삭제 버튼
delete_button = tk.Button(delete_frame, text="선택한 행 삭제", command=delete_selected_row)
delete_button.pack(side=tk.RIGHT, padx=5)

# 이전으로 버튼
back_button = tk.Button(button_frame, text="이전으로", command=reset_data)
back_button.pack(side=tk.LEFT, padx=5)

# 검색 입력창 및 버튼
search_button = tk.Button(button_frame, text="검색", command=lambda: search_treeview())
search_button.pack(side=tk.RIGHT ,padx=5)

search_var = tk.StringVar()
search_entry = tk.Entry(button_frame, textvariable=search_var, width=30)
search_entry.pack(side=tk.RIGHT, padx=5)
search_entry.bind("<Return>", lambda event: search_treeview(search_var.get()))

# Treeview
tree = ttk.Treeview(window)
tree.pack(fill='both', expand=True, padx=10, pady=5)

# GUI 실행
window.mainloop()
