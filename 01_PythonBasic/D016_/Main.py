import os
import sys
import time
import subprocess
import Player
import Item
import Enemy
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
        self.item_event = 0
        self.player_xy = []
        self.player_data = {}
        self.game_manager = game_manager
        self.enemy_manager = Enemy.Zombie()
        self.player_data = { "name":"player111", "x":self.game_manager.get_player_xy()[0], "y":self.game_manager.get_player_xy()[1], "health":3 }

    def init_game(self):
        # 각 모듈의 초기화 tick 전달

        # - 플레이어 틱
        # 플레이어 위치 초기화
        # self.player_xy = self.game_manager.get_player_xy()
        data = {"name":"player111", "x":self.game_manager.get_player_xy()[0], "y":self.game_manager.get_player_xy()[1], "health":3}

        self.player_data = Player.Player.tick(self.tick_count, data)

        # - 아이템 틱
        available_item_loc_lst = []
        map_data = self.game_manager.get_map()
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j] == 101:
                    available_item_loc_lst.append((i, j))

        self.game_manager.add_itmes(Item.Item.tick(self.tick_count, self.item_event, available_item_loc_lst, 10))

        # - 적 틱
        available_enemy_loc_lst = []
        for i in range(len(map_data)):
            for j in range(len(map_data[0])):
                if map_data[i][j] == 101:
                    available_enemy_loc_lst.append((i, j))

        self.game_manager.update_enemy(self.enemy_manager.return_positions(available_enemy_loc_lst, self.tick_count))

        # 게임 화면 초기화
        self.update_display()

    def update_display(self):
        # 지도 갱신
        os.system('cls')
        self.game_manager.display_map()

        # 플레이어 상태창 갱신
        self.game_manager.display_status(self.player_data['name'], self.player_data['hp'], self.player_data['protect'], self.player_data['status'])

        # 메시지 창 갱신
        self.game_manager.display_message()

    def start(self):
        self.item_event = 2

        while True:
            user_in = ""

            # 키보드 입력 받기
            while True:
                if keyboard.read_key() in ["w", "a", "s", "d"]:
                    user_in = keyboard.read_key()

                # 캐릭터 이동
                if user_in == "w":
                    data = {"input_key":user_in}
                    self.player_data = Player.Player.tick(1,data)
                    self.game_manager.move_obj(0, [self.player_data["x"], self.player_data["y"]])
                    break
                elif user_in == "a":
                    data = {"input_key":user_in}
                    self.player_data = Player.Player.tick(1,data)
                    self.game_manager.move_obj(0, [self.player_data["x"], self.player_data["y"]])
                    break
                elif user_in == "s":
                    data = {"input_key":user_in}
                    self.player_data = Player.Player.tick(1,data)
                    self.game_manager.move_obj(0, [self.player_data["x"], self.player_data["y"]])
                    break
                elif user_in == "d":
                    data = {"input_key":user_in}
                    self.player_data = Player.Player.tick(1,data)
                    self.game_manager.move_obj(0, [self.player_data["x"], self.player_data["y"]])
                    break

                time.sleep(0.1)

            # tick 카운트 증가
            self.tick_count += 1

            # 플레이어가 목표에 도달했는지 확인
            self.player_xy = [self.player_data["x"], self.player_data["y"]]
            goal_xy = self.game_manager.get_goal_xy()

            if self.player_xy[0] == goal_xy[0] and self.player_xy[1] == goal_xy[1]:
                print(True)
                break

            # ---플레이어 이동 후 상호작용---
            # TODO tick 보내기
            # - 플레이어 틱
            # [이벤트코드, ]
            # 0:캐릭터 생성 1: 이동x, 2: 이동, 3: 피해, 4: 아이템획득, 5: 탈출,
            # print(self.game_manager.get_items())
            # print(self.game_manager.get_items().keys)

            print(self.player_xy[0], self.player_xy[1])

            for i in enumerate(self.game_manager.get_items()):
                print(i[1][0], i[1][1])
                if self.player_xy[0] == i[1][1] and self.player_xy[1] == i[1][0]:
                    print("item 획득!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    break


            # - 아이템 틱
            #Item.Item.tick(self.tick_count, self.item_event, self.game_manager.get_map(), 10)

            # - 적 틱
            # Enemy.tick(tick_count, )
            # game_manager.update_enemy([[10, 10], [12, 12], [13, 20]])
            available_enemy_loc_lst = []
            map_data = self.game_manager.get_map()
            for i in range(len(map_data)):
                for j in range(len(map_data[0])):
                    if map_data[i][j] == 101:
                        available_enemy_loc_lst.append((i, j))

            self.game_manager.update_enemy(self.enemy_manager.return_positions(available_enemy_loc_lst, self.tick_count))

            # TODO 적과의 상호작용
            # 적과의 상호작용은 어떤 것이 있을까?
            # 적은 1칸 이내로 들어왔을 때(인접했을 때) 상호작용

            # TODO 아이템 박스 열기
            # 아이템은 겹칠 때 먹기

            # ---화면 갱신---
            # TODO 적 위치 갱신
            # game_manager.update_enemy([Enemy.get_final_zombie_position(game_manager.get_map())])

            # 맵, 상태창, 메시지창 갱신
            self.update_display()

if __name__ == "__main__":
    gm = GameManager()
    game = EscapeGame(gm)

    clear_count = 0

    while True:
        if clear_count < 3:
            gm.gen_map()

            game.init_game()
            game.update_display()
            game.start()
        else:
            print("클리어")
            break
