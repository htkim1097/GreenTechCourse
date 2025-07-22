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



