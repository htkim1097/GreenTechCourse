# import asyncio
#
# async def worker(who, time):
#     for i in range(5):
#         print(f"{who} - {i}번째 작업중")
#
#         # time.sleep() 과 다르게 블록킹을 일으키지 않음
#         await asyncio.sleep(time)
#
# async def main():
#     await asyncio.gather(
#         worker("A", 0.3),
#         worker("B", 1)
#     )
#
# asyncio.run(main())
# print("프로세스 종료 시점")

# import threading
# import time
#
# def task(name, delay):
#     print(f"{name} 시작")
#     time.sleep(delay)
#     print(f"{name} 완료")
#
# t1 = threading.Thread(target=task, args=("작업1", 2))
# t2 = threading.Thread(target=task, args=("작업2", 1))
# t3 = threading.Thread(target=task, args=("작업3", 4))
# t1.start()
# t2.start()
# t3.start()

import tkinter as tk
import threading
import time

def long_running_task():
    # 시간이 오래 걸리는 작업 시뮬레이션
    time.sleep(5)
    result = "결과 값"
    root.after(0, update_label, result) # 메인 스레드에서 레이블 업데이트

def update_label(result):
    label.config(text=f"Result: {result}")

def start_task():
    # 백그라운드 스레드에서 작업 실행
    thread = threading.Thread(target=long_running_task)
    thread.start()

root = tk.Tk()
root.title("멀티스레딩 예제")

button = tk.Button(root, text="Start Task", command=start_task)
button.pack()

label = tk.Label(root, text="Result: ")
label.pack()

root.mainloop()