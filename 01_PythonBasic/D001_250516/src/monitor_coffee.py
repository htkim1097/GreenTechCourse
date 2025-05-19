import keyboard
import time
import os

os.system("mode con: cols=17 lines=9")

def clickScrollLock(hour:int, interval_minute:int) -> None:
    i:int = 0
    cnt:int = int(hour * 60 / interval_minute) + 1

    #print(f"{hour=}, {interval_minute=}, {cnt=}")

    coffee_art = r"""
      ( (
       ) )
    ........
    |      |]
    \      / 
     `----'
    """

    print(coffee_art)

    while i < cnt:
        print(f"\r      {i}/{cnt}", end=' ', flush=True)
        keyboard.press_and_release('scroll lock')
        time.sleep(interval_minute * 60)
        i += 1

if __name__ == '__main__':
    clickScrollLock(9, 4)