# python gui
import tkinter
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



# radio button
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
