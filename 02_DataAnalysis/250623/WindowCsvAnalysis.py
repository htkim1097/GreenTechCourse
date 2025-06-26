import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import platform

# 한글 폰트 설정
if platform.system() == 'Windows':
   plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
   plt.rcParams['font.family'] = 'AppleGothic'
else:
   plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

file_path = ''
df_origin = pd.DataFrame()
df_data = pd.DataFrame()
search_modes = {0 : '일치', 1 : '근사값', 2 : '이상', 3 : '이하'}
search_cols = {}

def set_ctrl_state(is_enable):
    """
    컨트롤들의 조작 여부를 설정
    :param is_enable: 가능 여부
    """
    if is_enable:
        btn_save.config(state='normal')
        btn_print.config(state='normal')
        btn_search.config(state='normal')
        btn_describe.config(state='normal')
        btn_solve_missing.config(state='normal')
        btn_solve_outlier.config(state='normal')
        entry_search.config(state='normal')
        combo_search_mode.config(state='readonly')
        btn_reset_search.config(state='normal')
        combo_search_col.config(state='readonly')
    else:
        btn_save.config(state='disabled')
        btn_print.config(state='disabled')
        btn_search.config(state='disabled')
        btn_describe.config(state='disabled')
        btn_solve_missing.config(state='disabled')
        btn_solve_outlier.config(state='disabled')
        entry_search.config(state='disabled')
        combo_search_mode.config(state='disabled')
        btn_reset_search.config(state='disabled')
        combo_search_col.config(state='disabled')

def clear_selected():
    """
    현재 선택된 파일 경로 초기화
    """
    global file_path
    file_path = ''
    label_selected.config(text='')

def open_csv():
    """
    csv 파일 불러오기
    """
    global file_path

    try:
        path = filedialog.askopenfilename(
            title='CSV파일선택',
            filetypes=[('CSV files', '*csv')]
        )

        if path:
            file_path = path
            label_selected.config(text=file_path)

            global df_origin
            df_origin = pd.read_csv(file_path)

            global df_data
            df_data = df_origin.copy()

            text_result.delete('1.0', 'end')
            set_ctrl_state(True)

    except:
        pass

    set_data_cols_dict()
    clear_treeview()

def set_data_cols_dict():
    """
    불러온 데이터의 속성들을 딕셔너리에 저장한다.
    """
    search_cols[0] = '전체'
    for col in df_origin.columns:
        search_cols[len(search_cols)] = col

    combo_search_col.config(values=list(search_cols.values()))
    combo_search_col.current(0)

def clear_treeview():
    """
    treeview에 도시된 데이터를 삭제한다.
    """
    # treeview의 모든 객체를 삭제
    for item in tree.get_children():
        tree.delete(item)

    # treeview 컬럼(속성) 초기화
    tree.config(columns=list(), show='')

def search():
    """
    데이터 프레임 값 검색 기능
    """
    target = entry_search.get()

    if target == "":
        return

    target_col = combo_search_col.get()
    mode = combo_search_mode.get()
    global df_data

    tmp_df = pd.DataFrame()

    # entry 입력 값이 숫자이면 변환
    # isnumeric()은 실수 자료형을 False로 반환
    if target.isnumeric():
        target = int(target)
    else:
        try:
            # 'nan' 문자열을 float으로 처리해서 막아놓음 
            if target != 'nan':
                target = float(target)
        except:
            pass

    # 일치
    if mode == list(search_modes.values())[0]:
        # nan 값 검색
        if (type(target) is str) and target == 'nan':
            for col in df_data.columns:
                try:
                    tmp_df = tmp_df._append(df_data[df_data[col].isna()])
                except:
                    continue

        # 입력값이 문자열일 때
        elif type(target) is str:
            # 전체 검색
            if target_col == list(search_cols.values())[0]:
                for col in df_data.columns:
                    try:
                        tmp_df = tmp_df._append(df_data[df_data[col].str.contains(target, case=False)])
                    except:
                        tmp_df = tmp_df._append(df_data[df_data[col] == target])
            else:
                try:
                    tmp_df = df_data[df_data[target_col].str.contains(target, case=False)]
                except:
                    tmp_df = df_data[df_data[target_col] == target]

        else:
            # 전체 검색
            if target_col == list(search_cols.values())[0]:
                for col in df_data.columns:
                    tmp_df = tmp_df._append(df_data[df_data[col] == target])
            else:
                try:
                    tmp_df = df_data[df_data[target_col] == target]
                except: pass

    # 근사값
    elif mode == list(search_modes.values())[1]:
        # nan 값 검색
        if (type(target) is str) and target == 'nan':
            for col in df_data.columns:
                try:
                    tmp_df = tmp_df._append(df_data[df_data[col].isna()])
                except:
                    continue

        # 입력값이 문자열일 때
        elif type(target) is str:
            # 전체 검색
            if target_col == list(search_cols.values())[0]:
                for col in df_data.columns:
                    try:
                        tmp_df = tmp_df._append(df_data[df_data[col].str.contains(target, case=False)])
                    except:
                        tmp_df = tmp_df._append(df_data[df_data[col] == target])
            else:
                try:
                    tmp_df = df_data[df_data[target_col].str.contains(target, case=False)]
                except:
                    tmp_df = df_data[df_data[target_col] == target]
        else:
            # 전체 검색
            if target_col == list(search_cols.values())[0]:
                for col in df_data.columns:
                    try:
                        if str(target).find('.') != -1:
                            val_len = len(str(target).split('.')[1])
                            print(val_len)
                            tmp_df = tmp_df._append(df_data[df_data[col].round(val_len) == target])
                        else:
                            tmp_df = tmp_df._append(df_data[df_data[col].round(0) == target])
                    except:
                        continue
            else:

                tmp_df = df_data[df_data[target_col].round(0) == target]

        # if target_col == list(search_cols.values())[0]:
        #     for col in df_data.columns:
        #         try:
        #             tmp_df = tmp_df._append(df_data[round(df_data[col], 1) == target])
        #         except:
        #             continue
        # else:
        #     try:
        #         tmp_df = df_data[round(df_data[target_col]) == target]
        #     except:
        #         pass

    # 이상
    elif mode == list(search_modes.values())[2]:
        if type(target) is str:
            print_messages("문자열은 해당 검색 옵션을 지원하지 않습니다.")

        if target_col == list(search_cols.values())[0]:
            for col in df_data.columns:
                try:
                    tmp_df = tmp_df._append(df_data[df_data[col] >= target])
                except:
                    continue
        else:
            try:
                tmp_df = df_data[df_data[target_col] >= target]
            except:
                pass

    # 이하
    elif mode == list(search_modes.values())[3]:
        if type(target) is str:
            print_messages("문자열은 해당 검색 옵션을 지원하지 않습니다.")

        if target_col == list(search_cols.values())[0]:
            for col in df_data.columns:
                try:
                    tmp_df = tmp_df._append(df_data[df_data[col] <= target])
                except:
                    continue
        else:
            try:
                tmp_df = df_data[df_data[target_col] <= target]
            except:
                pass

    tmp_df = tmp_df.drop_duplicates()

    refresh_treeview(tmp_df)

def solve_missing():
    """
    결측치를 해당 열의 중앙값으로 채우기
    """
    res_message = "[결측치 처리]\n"
    for col in df_data.columns:
        try:
            changed = np.where(df_data[col].isna())

            med = df_data[col].median()

            if len(changed[0]) > 0:
                res_message += f"{col}--------------------\n"

                for i in changed[0]:
                    res_message += f"  {i} 행 : {df_data[col][i]} -> {med}\n"
                res_message += '\n'

            df_data[col] = df_data[col].fillna(med)
        except:
            continue

    print_messages(res_message)
    refresh_treeview(df_data)

def solve_outlier():
    """
    boxplot의 iqr을 이용한 이상치 처리
    이상치를 결측치로 변환
    """
    res_message = "[이상치 처리]\n"
    replace_val = np.nan

    for col in df_data.columns:
        try:
            # 수치형일 경우만 처리
            q1 = df_data[col].quantile(0.25)
            q3 = df_data[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - 1.5 * iqr
            upper = q3 + 1.5 * iqr

            changed = np.where((df_data[col] < lower) | (df_data[col] > upper))

            if len(changed[0]) > 0:
                res_message += f"{col}--------------------\n"

                for i in changed[0]:
                    res_message += f"  {i} 행 : {df_data[col][i]} -> {replace_val}\n"
                res_message += '\n'

            df_data[col] = np.where((df_data[col] < lower) | (df_data[col] > upper), replace_val, df_data[col])
        except:
            # 숫자형이 아닌 열은 무시
            continue

    print_messages(res_message)
    refresh_treeview(df_data)

def show_describe():
    """
    새로운 창에 처음 불러온 데이터와 수정된 데이터의 그래프를 도시합니다.
    """
    # 새로운 창 생성
    desc_win = tk.Tk()
    desc_win.title("Before & After Boxplot + Describe")  # 창 제목 설정
    desc_win.geometry("1400x750")  # 창 크기 설정

    # matplotlib으로 박스플롯 2개 그리기
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1행 2열 subplot 생성

    # 왼쪽 그래프. 정제 전 데이터 박스플롯
    sns.boxplot(data=df_origin, ax=axes[0])  # seaborn으로 박스플롯
    axes[0].set_title("Before")  # 제목 설정
    axes[0].tick_params(axis='x', rotation=45)  # X축 라벨 회전

    # 오른쪽 그래프. 정제 후 데이터 박스플롯
    sns.boxplot(data=df_data, ax=axes[1])
    axes[1].set_title("After")
    axes[1].tick_params(axis='x', rotation=45)

    fig.tight_layout()  # 그래프 간격 자동 정리

    canvas = FigureCanvasTkAgg(fig, master=desc_win)  # tkinter 위에 matplotlib 그래프 올리기
    canvas.draw()  # 그래프 그리기
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)  # 창 상단에 붙이기

    frame_descwin_bottom = tk.Frame(desc_win)
    frame_descwin_bottom.pack(side='bottom', fill='both', expand=True)

    # shape 표시
    text_shape = tk.Text(frame_descwin_bottom, height=2, relief='flat')
    text_shape.pack(side='top', anchor='w')

    # describe를 표시할 컨트롤
    canvas_descwin_desc1 = tk.Canvas(frame_descwin_bottom)
    canvas_descwin_desc1.pack(side='left', fill='both', expand=True)
    canvas_descwin_desc2 = tk.Canvas(frame_descwin_bottom)
    canvas_descwin_desc2.pack(side='right', fill='both', expand=True)

    text_desc1 = tk.Text(canvas_descwin_desc1, wrap='none', height=15)
    text_desc1.pack(side='top', fill='both')
    text_desc2 = tk.Text(canvas_descwin_desc2, wrap='none', height=15)
    text_desc2.pack(side='top', fill='both')

    # describe 표시 컨트롤의 스크롤바
    scrbar_desc1 = ttk.Scrollbar(canvas_descwin_desc1, orient="horizontal", command=text_desc1.xview)
    scrbar_desc1.pack(side="bottom", fill="x")
    text_desc1.configure(xscrollcommand=scrbar_desc1.set)

    scrbar_desc2 = ttk.Scrollbar(canvas_descwin_desc2, orient="horizontal", command=text_desc2.xview)
    scrbar_desc2.pack(side='bottom', fill='x')
    text_desc2.configure(xscrollcommand=scrbar_desc2.set)

    # shape 결과 문자열로 변환 후 삽입
    shape_str = str(df_data.shape)
    text_shape.insert(tk.END, "[데이터 Shape]\n" + shape_str)

    # describe 결과 문자열로 변환 후 삽입
    desc_str = df_origin.describe().to_string()
    text_desc1.insert(tk.END, "[정제 전 데이터의 통계 요약]\n\n" + desc_str)

    desc_str = df_data.describe().to_string()
    text_desc2.insert(tk.END, "[정제 후 데이터의 통계 요약]\n\n" + desc_str)

def save_csv():
    """
    현재 treeview에 도시된 데이터(df_data)를 csv 파일로 저장한다.
    """

    # 파일을 저장할 위치를 선택할 수 있도록 File Dialog 열기
    path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[('CSV files', '*csv')]
    )

    if path:
        df_data.to_csv(path, index=False)

        clear_selected()
        set_ctrl_state(False)
        clear_treeview()
        print_messages(f"{path} 에 파일을 저장했습니다.")
    else:
        print_messages(f"Error: 파일 저장 경로가 잘못됐습니다.")

def print_treeview(data:pd.DataFrame):
    """
    treeview에 데이터를 도시한다.
    :param data: 도시할 데이터프레임
    """
    try:
        tree.config(columns=list(data.columns), show='headings')

        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')

        for idx, row in data.iterrows():
            tree.insert('', idx, values=list(row))
    except Exception as e:
        print(e)

def refresh_treeview(data):
    """
    treeview의 데이터를 다시 도시한다.
    :param data: 새롭게 넣을 데이터 프레임
    """
    try:
        clear_treeview()
        print_treeview(data)
    except Exception as e:
        print(e)

def print_messages(msg:str):
    """
    메시지를 출력창에 출력한다.
    :param msg: 출력할 메시지
    """
    text_result.insert('end', msg)

# Main Window
window = tk.Tk()
window.title('CSV Analysis Program')
window.geometry('1500x800')

# - Main Window Frame들
frame_main = tk.Frame(window)
frame_main.pack(fill='both', expand=True)

frame_top = tk.Frame(frame_main, relief='solid', bd=1, pady=10, padx=5)
frame_top.pack(fill='x', side='top')

frame_search = tk.Frame(frame_top)
frame_search.pack(side='right')

frame_mid = tk.Frame(frame_main)
frame_mid.pack(fill='both', expand=True)

frame_bottom = tk.Frame(frame_main, relief='solid', bd=1)
frame_bottom.pack(fill='x', side="bottom")

frame_selected_file = tk.Frame(frame_top)
frame_selected_file.pack(side='bottom', anchor='w')

# - frame_top의 컨트롤들
btn_open = tk.Button(frame_top, text='csv 불러오기', width=12, command=lambda : open_csv())
btn_open.pack(side='left', padx=2)

btn_print = tk.Button(frame_top, text='csv 출력', width=12, command=lambda : print_treeview(df_data))
btn_print.pack(side='left', padx=2)

btn_solve_outlier = tk.Button(frame_top, text='이상치 해결', width=12, command=lambda : solve_outlier())
btn_solve_outlier.pack(side='left', padx=2)

btn_solve_missing = tk.Button(frame_top, text='결측치 해결', width=12, command=lambda : solve_missing())
btn_solve_missing.pack(side='left', padx=2)

btn_describe = tk.Button(frame_top, text='통계 요약', width=12, command=lambda : show_describe())
btn_describe.pack(side='left', padx=2)

btn_save = tk.Button(frame_top, text='csv 저장', width=12, command=lambda : save_csv())
btn_save.pack(side='left', padx=2)

# - frame_search의 컨트롤들
btn_search = tk.Button(frame_search, text='검색', command=lambda : search())
btn_search.pack(side='right')

btn_reset_search = tk.Button(frame_search, text='초기화', command= lambda : refresh_treeview(df_data))
btn_reset_search.pack(side='left', padx=(0, 5))

combo_search_col = ttk.Combobox(frame_search, width=7)
combo_search_col.pack(side='left', padx=(0, 5))

combo_search_mode = ttk.Combobox(frame_search, values=list(search_modes.values()), width=7)
combo_search_mode.current(0)
combo_search_mode.pack(side="left", padx=(0, 5))

entry_search = tk.Entry(frame_search)
entry_search.bind('<Return>', lambda e: search())
entry_search.pack()

# - frame_selected_file의 컨트롤들
label_selected_title = tk.Label(frame_selected_file, text='선택된 파일: ')
label_selected_title.pack(side='left')

label_selected = tk.Label(frame_selected_file)
label_selected.pack(side='left')

# - frame_mid의 Treeview
tree = ttk.Treeview(frame_mid, columns=list(df_data.columns), show='headings')
tree.pack(fill='both', expand=True)

scrbar_tree = ttk.Scrollbar(tree, orient="vertical", command=tree.yview)
scrbar_tree.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrbar_tree.set)

# - frame_bottom의 컨트롤들
label_result_title = tk.Label(frame_bottom, height=1, text='출력', bg='#dddddd', anchor='w', padx=5)
label_result_title.pack(fill='x', anchor='w')

canvas_result = tk.Canvas(frame_bottom)
canvas_result.pack(side='left', expand=True, fill='both')

text_result = tk.Text(canvas_result, height=15)
text_result.pack(side='left', fill='both', expand=True)

scrbar_resulttext = ttk.Scrollbar(canvas_result, orient="vertical", command=text_result.yview)
scrbar_resulttext.pack(side="right", fill="y")
text_result.configure(yscrollcommand=scrbar_resulttext.set)

set_ctrl_state(False)

window.mainloop()