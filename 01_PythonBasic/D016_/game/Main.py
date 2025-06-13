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

# 우선순위: 플레이어 > 아이템 > 적
"""
import os
import sys
import time
import subprocess
import Player
import Item
import Enemy
import MapObjectId as oid
from GameManager import GameManager

try:
    import keyboard
except:
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'keyboard'])
    import keyboard

def update_display(displayer:GameManager):
    # 지도 갱신
    os.system('cls')
    displayer.display_map()

    # 플레이어 상태창 갱신
    displayer.display_status("player", 3, ["a", "b", "c", "d"], 5)

    # 메시지 창 갱신
    displayer.display_message()

def main():
    tick_count = 0
    item_event = 0

    # 게임 설정
    game_manager = GameManager()
    game_manager.set_map_size(60, 30)

    # 초기 맵 생성
    # game_manager.generate_forest_map()

    # TODO 초기 틱 전달
    # 각 모듈의 tick 함수에 tick 전달
    # 각 모듈의 수행 여부 반환 받기
    # - 플레이어 틱
    #Player.Player.tick(tick_count)

    # - 아이템 틱
    game_manager.add_itmes(Item.Item.tick(tick_count, item_event, game_manager.get_map(), 10, "숲", False))

    # - 적 틱
    print(Enemy.ZombieManager.tick(tick_count, game_manager.get_map()))

    update_display(game_manager)

    # 게임루프 시작
    while True:
        user_in = ""

        # 키보드 입력 받기
        while True:
            # TODO 캐릭터의 위치 가져오기
            player_xy = game_manager.get_player_xy()

            if keyboard.read_key() in ["w", "a", "s", "d"]:
                user_in = keyboard.read_key()

            # 캐릭터 이동
            if user_in == "w":
                game_manager.move_obj(0, [player_xy[0], player_xy[1] - 1])
                break
            elif user_in == "a":
                game_manager.move_obj(0, [player_xy[0] - 1, player_xy[1]])
                break
            elif user_in == "s":
                game_manager.move_obj(0, [player_xy[0], player_xy[1] + 1])
                break
            elif user_in == "d":
                game_manager.move_obj(0, [player_xy[0] + 1, player_xy[1]])
                break

            # # 캐릭터 이동
            # if user_in == "w":
            #     if game_manager.check_move(oid.PLAYER, [player_xy[0], player_xy[1] - 1]):
            #         # TODO 이동
            #         game_manager.player_loc = [player_xy[0], player_xy[1] - 1]
            #         #Player.move(user_in)
            #         break
            # elif user_in == "a":
            #     if game_manager.check_move(oid.PLAYER, [player_xy[0] - 1, player_xy[1]]):
            #         game_manager.player_loc = [player_xy[0], player_xy[1] - 1]
            #         #Player.move(user_in)
            #         break
            # elif user_in == "s":
            #     if game_manager.check_move(oid.PLAYER, [player_xy[0], player_xy[1] + 1]):
            #         #Player.move(user_in)
            #         break
            # elif user_in == "d":
            #     if game_manager.check_move(oid.PLAYER, [player_xy[0] + 1, player_xy[1]]):
            #         #Player.move(user_in)
            #         break

            time.sleep(0.1)

        # ---플레이어 이동 후 상호작용---
        # TODO tick 보내기
        # - 플레이어 틱
        # [이벤트코드, ]
        # 0:캐릭터 생성 1: 이동x, 2: 이동, 3: 피해, 4: 아이템획득, 5: 탈출,
        #Player.Player.tick(tick_count, 2, data={"input_key":user_in})

        # - 아이템 틱
        Item.Item.tick(tick_count, item_event, game_manager.get_map(), 10, "숲", False)

        # - 적 틱
        # Enemy.tick(tick_count, )

        # TODO 적과의 상호작용
        # 적과의 상호작용은 어떤 것이 있을까?
        # 적은 1칸 이내로 들어왔을 때(인접했을 때) 상호작용

        # TODO 아이템 박스 열기
        # 아이템은 겹칠 때 먹기

        # ---화면 갱신---
        # TODO 적 위치 갱신
        # game_manager.update_enemy([Enemy.get_final_zombie_position(game_manager.get_map())])

        # 맵, 상태창, 메시지창 갱신
        update_display(game_manager)

if __name__ == "__main__":
    main()