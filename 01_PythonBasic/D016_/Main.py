"""
1조: 아이템
2조: 캐릭터/ 인벤
    # 플레이어: 맵 정보 알고 있음.
3조: 몬스터
    # 좀비: 맵 정보는 모름, 대신 플레이어 좌표는 알고 있고, 사용할지 안할지는 상황에 따라.
4조(팀장): 맵/ 틱 (game manager)

# 게임 매니저
#  - 이동 체크
#  - 각 조의 속성, 메서드 호출만
#  - 플레이어와 적 사이에서 통보
#  - 메시지 출력
"""
import os
import sys
import time
import subprocess
import Player
import Item
import Enemy
from DisplayManager import DisplayManager

try:
    import keyboard
except:
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'keyboard'])
    import keyboard

def main():
    # 게임 설정
    mn = DisplayManager()
    mn.set_map_res(70, 30)

    # 플레이어 상태 초기화
    player = Player.Player("플레이어", 30,30)

    # 초기 맵 생성
    mn.generate_forest_map()
    # TODO 적 초기 위치 추가
    mn.update_enemy([Enemy.get_final_zombie_position(mn.get_map(), [10, 10], player.my_position())])

    # - 목표 위치

    # 아이템 추가
    mn.add_itmes(Item.ran_item(mn.get_map(), 10))

    os.system('cls')
    mn.display_map()


    # 게임루프 시작
    while True:
        user_in = ""

        # 키보드 입력 받기
        while True:
            # TODO 캐릭터의 위치 가져오기
            player_xy = player.my_position()

            if keyboard.read_key() in ["w", "a", "s", "d"]:
                user_in = keyboard.read_key()

            # 캐릭터 이동
            if user_in == "w":
                player.move("w")
                mn.move_obj(0, player_xy, [player_xy[0], player_xy[1] - 1])
                break
            elif user_in == "a":
                mn.move_obj(0, player_xy, [player_xy[0] - 1, player_xy[1]])
                break
            elif user_in == "s":
                mn.move_obj(0, player_xy, [player_xy[0], player_xy[1] + 1])
                break
            elif user_in == "d":
                mn.move_obj(0, player_xy, [player_xy[0] + 1, player_xy[1]])
                break

            time.sleep(0.1)

        # ---이동 후 상호작용---
        # TODO 적과의 상호작용

        # TODO 아이템 박스 열기

        # ---화면 갱신---
        # TODO 적 위치 갱신
        # mn.update_enemy([Enemy.get_final_zombie_position(mn.get_map())])

        # 지도 갱신
        os.system('cls')
        mn.display_map()

        # TODO 플레이어 상태창 갱신

        # TODO 메시지 창 갱신

if __name__ == "__main__":
    main()