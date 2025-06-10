"""
1조: 아이템
2조: 캐릭터/ 인벤
    # 플레이어: 맵 정보 알고 있음.
3조: 몬스터
    # 좀비: 맵 정보는 모름, 대신 플레이어 좌표는 알고 있고, 사용할지 안할지는 상황에 따라.
4조(팀장): 맵/ 틱 (game manager)
"""
import os
import sys
import time
import subprocess
from DisplayManager import DisplayManager

try:
    import keyboard
except:
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'keyboard'])
    import keyboard

def main():

    # 게임 설정
    disp = DisplayManager()
    disp.set_game(50, 30)

    # 초기 맵 생성
    # - 아이템, 적 초기 위치 포함
    # - 목표 위치
    disp.generate_forest_map()

    # 플레이어 상태 초기화

    while True:
        user_in = ""
        # 키보드 입력 받기
        while True:
            if keyboard.read_key() in ["w", "a", "s", "d"]:
                user_in = keyboard.read_key()
                break
            time.sleep(0.5)

        # 캐릭터 이동 판단
        # - 지형
        # - 적
        # - 아이템

        # 지도 갱신
        os.system('cls')
        disp.display_map()

        # 몬스터 갱신
        # 플레이어 갱신


if __name__ == "__main__":
    main()