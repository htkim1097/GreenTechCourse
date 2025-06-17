import os
import sys
import time
import subprocess
import Player
import Item
import Enemy
import MapObjectId as ObjId
from GameManager import GameManager

try:
    import keyboard
except:
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable,'-m', 'pip', 'install', '--upgrade', 'keyboard'])
    import keyboard

class EscapeGame:
    def __init__(self, game_manager:GameManager):
        self.tick_count = 0
        self.enemy_spawn_amount = 5
        self.game_manager = game_manager
        self.enemy_manager = Enemy.ZombieSpawner(self.enemy_spawn_amount)

    def init_game(self, spawn_amount):
        self.tick_count = 0
        self.enemy_manager.max_zombies = spawn_amount

        # 플레이어 초기 위치 전달
        p_receive_data = Player.tick(self.tick_count, { "name":"Player", "init_pos" : self.game_manager.get_init_player_xy(), "hp" : 5})

        # 아이템 모듈 초기 틱 : 아이템 박스를 생성할 랜덤 위치
        i_data = { "able_place" : self.game_manager.get_able_place(), "num" : 5 }
        self.game_manager.add_itmes(Item.tick(self.tick_count, i_data))

        # 몬스터 모듈 초기 틱 : 몬스터 초기 스폰 위치
        able_place = self.game_manager.get_able_place()
        self.enemy_manager.spawn_zombies(able_place)
        self.game_manager.update_enemy(self.enemy_manager.zombie_list)

        return p_receive_data

    def update_display(self, p_data):
        # 지도 갱신
        os.system('cls')
        self.game_manager.display_map()

        # 플레이어 상태창 갱신
        self.game_manager.display_status(p_data)

        # 메시지 창 갱신
        try:
            if len(p_data["message"]) > 0:
                self.game_manager.add_message(p_data["message"])
        except:
            pass

        self.game_manager.display_message()

    def start(self) -> bool:
        p_send_data = {}
        p_receive_data = {}
        skip_move = False
        player_xy = self.game_manager.get_init_player_xy()

        while True:
            user_in = ""

            # 플레이어 송신 데이터 초기화
            p_send_data = {}

            # 키보드 입력 받기
            while True:
                # if skip_move:
                #     p_send_data["pass"] = True
                #     skip_move = False
                #     break

                if keyboard.read_key() in ["w", "a", "s", "d"]:
                    user_in = keyboard.read_key()

                # 플레이어 이동 입력 체크
                if user_in == "w":
                    if self.game_manager.check_move(ObjId.PLAYER, [player_xy[0], player_xy[1] - 1]):
                        p_send_data["input_key"] = "w"
                    break
                elif user_in == "a":
                    if self.game_manager.check_move(ObjId.PLAYER, [player_xy[0] - 1, player_xy[1]]):
                        p_send_data["input_key"] = "a"
                    break
                elif user_in == "s":
                    if self.game_manager.check_move(ObjId.PLAYER, [player_xy[0], player_xy[1] + 1]):
                        p_send_data["input_key"] = "s"
                    break
                elif user_in == "d":
                    if self.game_manager.check_move(ObjId.PLAYER, [player_xy[0] + 1, player_xy[1]]):
                        p_send_data["input_key"] = "d"
                    break

                time.sleep(0.1)

            # tick 카운트 증가
            self.tick_count += 1

            p_send_data["able_place"] = self.game_manager.get_able_place()

            # 플레이어 이동 전달
            self.game_manager.move_obj(ObjId.PLAYER, player_xy)

            # 아이템 상자를 열었을 때
            if self.game_manager.get_place_type(player_xy) == ObjId.ITEM_BOX:
                p_send_data["item"] = True
                self.game_manager.del_item(player_xy)

            # 플레이어가 목표에 도달했을 때
            if self.game_manager.get_place_type(player_xy) == ObjId.DOOR:
                return True

            # 적 이동하기
            self.enemy_manager.tick_move_zombies(self.game_manager.get_map(), player_xy)

            # 적과의 상호작용(상하좌우 인접시)
            # 플레이어 인접 좌표
            near_pos_lst = [[player_xy[0] + 1, player_xy[1]],
                        [player_xy[0] - 1, player_xy[1]],
                        [player_xy[0], player_xy[1] + 1],
                        [player_xy[0], player_xy[1] - 1]]

            enemy_pos_lst = self.enemy_manager.get_zombies_pos()

            for near in near_pos_lst:
                if near in enemy_pos_lst:
                    p_send_data["damaged"] = 1
                    self.enemy_manager.stun_zombie(near)

            # 좀비 보충 스폰
            able_place = self.game_manager.get_able_place()
            self.enemy_manager.spawn_zombies(able_place)

            p_receive_data = Player.tick(self.tick_count, p_send_data)

            p_send_data = {}

            player_xy = p_receive_data["pos"]

            # 플레이어 사망
            if p_receive_data["hp"] <= 0:
                self.game_manager.clear_messages()
                return False

            # 화면 갱신
            self.update_display(p_receive_data)

if __name__ == "__main__":
    stage_num = 3
    clear_count = 0

    gm = GameManager()
    game = EscapeGame(gm)

    while True:
        if clear_count < stage_num:
            gm.gen_map()

            if clear_count == 0:
                gm.add_message("1")
            elif clear_count == 1:
                gm.add_message("2")
            elif clear_count == 2:
                gm.add_message("3")

            # 게임 초기화
            p = game.init_game(clear_count + 5)
            game.update_display(p)

            if game.start():
                clear_count += 1
            else:
                print("사망")
                break
        else:
            print("클리어")
            break
