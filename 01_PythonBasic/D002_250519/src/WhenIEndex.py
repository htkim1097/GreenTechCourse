import time
import keyboard
import os

os.system("mode con: cols=17 lines=9")
coffee_art = r"""
  ( (
   ) )
........
|      |]
\      / 
 `----'
"""

print(coffee_art)

def main():
    # 17:50:00 까지
    end_hour = 17
    end_minute = 50

    end_total_sec = (end_hour * 60 * 60) + (end_minute * 60)

    cnt = 0

    while True:
        now_time = time.strftime('%X')
        hour, minute, sec = now_time.split(":")

        now_time_to_sec = (int(hour) * 60 * 60) + (int(minute) * 60)

        # sleep(30) 30초 * 8 = 약 4분 정도 소요시
        if cnt >= 480:
            keyboard.press_and_release('scroll lock')
            cnt = 0

        total_remain_sec = end_total_sec - now_time_to_sec

# 10000
        # 10000 // 3600 = 2
        # 2800 // 60 = 40
        #

        remain_hour = total_remain_sec // 3600
        remain_min = (total_remain_sec - (3600 * remain_hour)) // 60
        remain_sec = (total_remain_sec - (remain_min * 60))

        print(f"\r {remain_hour}:{remain_min}:{remain_sec}", end=' ', flush=True)

        time.sleep(1)
        cnt += 1

if __name__ == '__main__':
    main()