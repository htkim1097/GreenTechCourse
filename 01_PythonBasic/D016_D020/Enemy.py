import MapObjectId as ids
import random
import MyUtils as util

class ZombieSpawner:
    def __init__(self, max_zombies):
        self.__max_zombies = max_zombies
        self.__zombie_lst = []
        self.__stun = 3

    @property
    def zombie_list(self):
        return self.__zombie_lst

    @property
    def max_zombies(self):
        return self.__max_zombies

    @max_zombies.setter
    def max_zombies(self, val):
        self.__max_zombies = val

    def spawn_zombies(self, able_place_lst:list):

        zombies_pos = self.get_zombies_pos()

        i = 0
        while i < len(zombies_pos):
            try:
                able_place_lst.remove(zombies_pos[i])
            except:
                pass
            finally:
                i += 1

        while len(self.__zombie_lst) <= self.max_zombies:
            spawn_place = random.choice(able_place_lst)
            able_place_lst.remove(spawn_place)
            self.__zombie_lst.append(Zombie(100, 5, spawn_place))

    def garbage_z_collector(self, zombie):
        if zombie.life == 0:
            self.zombie_list.remove(zombie)

    def tick_move_zombies(self, map_data, player_pos):
        for z in self.zombie_list:
            z.move(map_data, player_pos)
            self.garbage_z_collector(z)

    def get_zombies_pos(self):
        tmp_lst = []

        for z in self.zombie_list:
            tmp_lst.append(z.pos)

        return tmp_lst

    def stun_zombie(self, pos):
        z = self.get_zombie_by_pos(pos)

        if z is not None:
            z.stun = self.__stun

    def get_zombie_by_pos(self, pos):
        for z in self.zombie_list:
            if pos == z.pos:
                return z
        return None

class Zombie:
    def __init__(self, life, sight, pos, z_type=ids.NORMAL_ZOMBIE):
        self.__life = life
        self.__sight = sight
        self.__pos = pos
        self.__z_type = z_type
        self.__stun = 0

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, val):
        self.__life = val

    @property
    def sight(self):
        return self.__sight

    @sight.setter
    def sight(self, val):
        self.__sight = val

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, val):
        self.__pos = val

    @property
    def stun(self):
        return self.__stun

    @stun.setter
    def stun(self, val):
        self.__stun = val

    def move(self, map_data, player_pos):

        if self.__stun > 0:
            self.__stun -= 1
            return

        new_pos = self.__pos

        # 플레이어와 거리가 시야거리 이하일 때
        dist_to_player = util.calc_dist(player_pos, self.__pos)
        if dist_to_player == 1:
            pass

        elif dist_to_player <= self.__sight:
            xy = self.__pos
            direction = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            min_dist = 9999
            idx = 0

            for i in range(len(direction)):
                dist = util.calc_dist(player_pos, [xy[0] + direction[i][0], xy[1] + direction[i][1]])
                # 최소값이고 이동 가능 지역일 때
                if dist < min_dist and map_data[xy[1] + direction[i][1]][xy[0] + direction[i][0]] == ids.ROAD:
                    min_dist = dist
                    idx = i

            new_pos = [xy[0] + direction[idx][0], xy[1] + direction[idx][1]]

        else:
            xy = self.__pos
            around = [(xy[0] - 1, xy[1]) if map_data[xy[1]][xy[0] - 1] == ids.ROAD else None,
                      (xy[0] + 1, xy[1]) if map_data[xy[1]][xy[0] + 1] == ids.ROAD else None,
                      (xy[0], xy[1] - 1) if map_data[xy[1] - 1][xy[0]] == ids.ROAD else None,
                      (xy[0], xy[1] + 1) if map_data[xy[1] + 1][xy[0]] == ids.ROAD else None]

            random.shuffle(around)

            for i in around:
                if i is not None:
                    new_pos = i

        self.__pos = new_pos
        self.life -= 1

    # 이동
    # 플레이어와 거리 측정
    # 거리가 sight 이하일 경우 추적
    # 아니면 주변 이동

