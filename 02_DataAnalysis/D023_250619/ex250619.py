# python gui
# import tkinter
# ERP(Enterprise Resource Planning): 기업의 업무 프로세스를 통합적으로 관리, 지원하는 소프트웨어
# DashBoard GUI

# Tkinter 사용
# -----기본틀-----
# import tkinter as tk
#
# # 메인 프레임 생성
# window = tk.Tk()
# # 메인 프레임 제목
# window.title("나의 첫 Tkinter 창")
#
# # 컨트롤 생성
# # 레이블 컨트롤 생성
# label = tk.Label(window, text="안녕하세요")
# # 레이블 컨트롤 배치
# label.pack()
#
# button = tk.Button(window, text="클릭하세요")
# button.pack()
#
# # 프로그램의 루프 실행
# window.mainloop()

# -----tkinter 컨트롤-----
# 라벨, 버튼
# import tkinter as tk
#
# window = tk.Tk()
#
# # 윈도우 사이즈 지정
# window.geometry("300x200")
# # 윈도우 크기조절 가능 여부
# #window.resizable(False, False)
# window.title("Window Title")
#
# # 라벨
# # fg : 글자 색상
# # relief : 테두리
# # textvariable : 라벨에 표시할 문자열을 가져올 변수
# # anchar : 라벨 안에 문자열 위치
# # justify : 라벨의 문자열이 여러 줄일 때 정렬 방법
# label = tk.Label(window, text="fdsf", width=100, height=2, fg="red")
# label.pack()
#
#
# count = 0
#
# def count_up():
#     global count
#     count += 1
#     # config : 이미 만들어진 컨트롤의 속성을 변경
#     label.config(text=str(count))
#
# def count_down():
#     global count
#     if count > 0:
#         count -= 1
#         label.config(text=str(count))
#
# # 버튼
# btn = tk.Button(window, text='countUP', command=count_up)
# btn.pack()
#
# btn2 = tk.Button(window, text='countDOWN', command=count_down)
# btn2.pack()
#
# # 항상 마지막에
# window.mainloop()


# 엔트리
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x200")
# window.title("Window Title")
#
# label = tk.Label(window, text="fdsf", width=100, height=2, fg="red")
# label.pack()
#
# # event 객체를 매개변수로 받을 수 있다.
# def calc(e):
#     label.config(text=e)
#     #label.config(text=str(eval(entry.get())))
#
# entry = tk.Entry(window)
# # bind: entry와 Return 키를 연결.
# # Return 키가 입력되면 calc 함수를 호출하게 된다.
# # <Return> = Enter key
# # bind한 입력의 인식은 포커스 상태에서만 가능
# entry.bind('<Return>', calc)
# entry.pack()
#
# # <Escape> ESC
# # <Delete> del
# # <Space> space
# # <Up> <Down> <Left> <Right>
#
#
# # 항상 마지막에
# window.mainloop()


# 리스트 박스
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x200")
# window.title("Window Title")
#
# def add_item():
#     s = entry.get()
#     listbox.insert(tk.END, s)
#
# entry = tk.Entry(window)
# entry.pack()
#
# btn = tk.Button(window, text="입력", command=add_item)
# btn.pack()
#
# # EXTENDED : 다중선택
# # SINGLE : 단일 선택, 방향키로 이동, 스페이스로 선택
# # BROWSE : 단일 선택, 방향키로 선택
# listbox = tk.Listbox(window, selectmode=tk.EXTENDED, height=0)
# listbox.insert(0, '111')
# listbox.insert(1, '222')
# listbox.insert(2, '333')
# # 시작 인덱스와 끝 인덱스를 입력해서 삭제 가능
# #listbox.delete(1)
# listbox.pack()
#
# # 항상 마지막에
# window.mainloop()


# 체크박스 버튼
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x200")
# window.title("Window Title")
#
# def flash():
#     # 버튼을 깜빡이게 한다.
#     checkButton1.flash()
#
# Checkvariety_1 = tk.IntVar()
# Checkvariety_2 = tk.IntVar()
#
# # activebackground : 활성화 됐을 때 배경
# # text는 고정적인 문자, 단순 출력용.
# # variable은 변수의 역할, 동적인 상황에서 사용.
# checkButton1 = tk.Checkbutton(window, variable=Checkvariety_1, text='1', activebackground='blue')
# checkButton2 = tk.Checkbutton(window, variable=Checkvariety_2, text='2')
# # 동적 변수를 2번 버튼과 같이 묶었기 때문에 클릭 상태가 동기화 된다.
# checkButton3 = tk.Checkbutton(window, variable=Checkvariety_2, text='3', command=flash)
# # 이벤트 객체의 흐름
# # mainloop 중 마우스, 키보드 입력 등의 Interept 이벤트 발생.
# # 이벤트는 gui 상위 계층부터 전달되어 목적지 까지 이동 후 다시 되돌아온다.
#
# # 버튼의 command에 들어가는 함수와 달리 bind에서 사용되는 함수는 event 객체를 매개변수로 받아줘야 한다.
# #
#
# checkButton1.pack()
# checkButton2.pack()
# checkButton3.pack()
#
# # 항상 마지막에
# window.mainloop()



# 라디오 버튼
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x200")
# window.title("Window Title")
#
# def check():
#     label.config(text="RadioVariety_1 = " + str(RadioVariety_1.get()) + "\n" \
#                       + "RadioVariety_2 = " + str(RadioVariety_2.get()) + "\n\n" \
#                       + "Total = " + str(RadioVariety_1.get() + RadioVariety_2.get()) + "\n")
#
# RadioVariety_1 = tk.IntVar()
# RadioVariety_2 = tk.IntVar()
#
# # 라디오 버튼이 활성(클릭)되면 value 값이 variable로 들거간다.
# # variable이 라디오 버튼 그룹, value가 각 버튼의 id라고 보면 된다.
# # variable에 활성화된 값과 동일한 value의 모든 버튼이 활성화 된다.
# radio1 = tk.Radiobutton(window, text='1번', value=3, variable=RadioVariety_1, command=check)
# radio1.pack()
#
# radio2 = tk.Radiobutton(window, text='2번(1번)', value=3, variable=RadioVariety_1, command=check)
# radio2.pack()
#
# radio3 = tk.Radiobutton(window, text='3번', value=9, variable=RadioVariety_1, command=check)
# radio3.pack()
#
# radio4 = tk.Radiobutton(window, text='4번', value=12, variable=RadioVariety_2, command=check)
# radio4.pack()
#
# radio5 = tk.Radiobutton(window, text='5번', value=15, variable=RadioVariety_2, command=check)
# radio5.pack()
#
# label = tk.Label(window, text="None", height=5)
# label.pack()
#
#
# # 항상 마지막에
# window.mainloop()



# pack 정적 배치(상대위치 배치)
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x200")
# window.title("Window Title")
#
# b1 = tk.Button(window, text='top')
# b1_1 = tk.Button(window, text='top-1')
# b2 = tk.Button(window, text='bottom')
# b2_1 = tk.Button(window, text='bottom-1')
# b3 = tk.Button(window, text='left')
# b3_1 = tk.Button(window, text='left-1')
# b4 = tk.Button(window, text='right')
# b4_1 = tk.Button(window, text='right-1')
# b5 = tk.Button(window, text='center', bg='red')
#
# b1.pack(side=tk.BOTTOM)
# b1_1.pack(side=tk.TOP, fill=tk.X)
#
# b2.pack(side=tk.BOTTOM)
# b2_1.pack(side=tk.BOTTOM, anchor="e")
#
# b3.pack(side=tk.LEFT)
# b3_1.pack(side=tk.LEFT, fill="y")
#
# b4.pack(side=tk.RIGHT)
# b4_1.pack(side=tk.RIGHT, anchor=tk.S)
#
# b5.pack(expand=True, fill=tk.BOTH)
#
# # side : 특정 위치로 공간 할당. right/left/top/bottom : 부모 컨트롤의 어느쪽 면으로 붙을지, pack 순서대로 가장 바깥쪽으로 배치된다.
# # anchor : 할당 공간 내 위치 지정. center/n/e/s/w 또는 ne처럼 조합. : 동, 서, 남, 북, 중앙 정렬
# # expand : 미사용 공간에 확장. True/False
# # fill : 할당 공간에 대한 크기 맞춤. none/x/y/both : x축, y축 방향으로 컨트롤의 크기를 맞추기
#
# # 항상 마지막에
# window.mainloop()



# pack 실습
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x200")
# window.title("Window Title")
#
# b1 = tk.Button(window, text='top')
# b2 = tk.Button(window, text='top-1')
# b3 = tk.Button(window, text='top-2')
# b4 = tk.Button(window, text='top-3')
#
#
# b1.pack(side=tk.TOP, anchor=tk.W)
# b2.pack(side=tk.TOP, anchor=tk.CENTER)
# b3.pack(side=tk.TOP, fill=tk.X)
# b4.pack(side=tk.TOP, anchor=tk.W)
#
# # 항상 마지막에
# window.mainloop()



# place 절대 배치 방식(좌표계)
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("300x300")
# window.title("Window Title")
#
# label = tk.Label(window, text='label1', bg='red')
# label.place(x=50, y=50)
#
# label2 = tk.Label(window, text='label2', bg='green')
# label2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
#
# b1 = tk.Button(window, text='btn')
# b1.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
#
# # 항상 마지막에
# window.mainloop()



# 프레임
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("1000x1000")
# window.title("Window Title")
# window.resizable(width=True, height=1)
#
# frame1 = tk.Frame(window, relief='solid', bd=2)
# frame1.pack(side='left', fill='both', expand=True)
#
# frame2 = tk.Frame(window, relief='solid', bd=2)
# frame2.pack(side='right', fill='both', expand=True)
#
# btn1 = tk.Button(frame1, text='f1 버튼')
# btn1.pack(side='right')
# btn2 = tk.Button(frame2, text='f2 버튼')
# btn2.pack(side='left')
#
# # 항상 마지막에
# window.mainloop()



# 캔버스
# import tkinter as tk
#
# window = tk.Tk()
#
# window.geometry("800x600")
# window.title("Window Title")
# window.resizable(width=True, height=1)
#
# canvas = tk.Canvas(window, width=200, height=200)
# line = canvas.create_line(10, 10, 20, 20, 20, 130, 30, 140, fill='red')
# polygon = canvas.create_polygon(50, 50, 170, 170, 100, 170, outline='yellow')
# arc = canvas.create_arc(100, 100, 300, 300, start=0, extent=150, fill='green')
#
# # create_line : 선 긋기 => 좌표쌍, 좌표쌍, ...
# # create_polygon : 다각형 만들기 => 좌표쌍, 좌표쌍, ...
# # create_arc : 호 그리기 => 100, 100에서 300, 300 크기를 가지는 start 0 각도에서 시작해서 extent 까지의 각을 갖는 호를 그린다.
#
# # 캔버스는 그림, 사진을 올리고 싶을 때 활용.
#
# canvas.pack()
#
# # 항상 마지막에
# window.mainloop()


# 프로그래스 바
# import tkinter as tk
# # 부수적인 컨트롤의 모음
# import tkinter.ttk
#
# window = tk.Tk()
#
# window.geometry("800x600")
# window.title("Window Title")
#
# progressbar = tk.ttk.Progressbar(window, maximum=80, mode='indeterminate')
# progressbar.pack(side=tk.BOTTOM)
# progressbar.start(50)
#
# # start() : ms 단위로 시작 (프로그래스바가 밀리초마다 움직이는 효과)
# # step(value) : 값 증가, 현재 표시되는 값에서 value만큼 값 추가.
# # stop() : 종료, 프로그래스바 애니메이션 종료
#
# # mode 설정 : determinate, 프로그래스바 표시 스타일. determinate/indeterminate
# # length : 프로그래스바의 절대적 너비 설정, 기본값은 100이고 상수로 설정 가능
# # orient : 프로그래스바 표시 방향 vertical/horizontal
# # maximum : 최대값 설정. 기본값 100
#
#
# # 항상 마지막에
# window.mainloop()


# 프로그래스바2
# import tkinter as tk
# import tkinter.ttk
# import time
#
# window = tk.Tk()
#
# window.geometry("800x600")
# window.title("Window Title")
#
# progressbar = tk.ttk.Progressbar(window, maximum=100, mode='determinate')
# progressbar.pack(pady=50)
#
# def update_progressbar():
#     for i in range(100):
#         progressbar['value'] = i
#         window.update_idletasks()
#         time.sleep(0.01)
# update_progressbar()
#
# # 항상 마지막에
# window.mainloop()



