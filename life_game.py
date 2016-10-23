import os
import sys
import time
import random

class GameMap(object):

    __slots__ = ('map', 'rows', 'cols')

    def __init__(self, rows, cols):

        GameMap.rows = rows
        GameMap.cols = cols
        GameMap.map = [[0]*cols for j in range(rows)]

    def reset(self, life_ratio):
        for i in range(len(GameMap.map)):
            for j in range(len(GameMap.map[i])):
                if random.random()<life_ratio:
                    GameMap.map[i][j]=1 # 0-empty 1-alive 2-dead


    def get_neighbor_count(self, row, col):

        alive_num = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r >= 0 and r <GameMap.rows and c >= 0 and c < GameMap.cols:
                    if GameMap.map[r][c] == 1:
                        alive_num += 1
        return alive_num

    def set(self, row, col, val):

        GameMap.map[row][col] = val


    def get(self, row, col):

        return GameMap.map[row][col]

class LifeGame(object):

    __slots__ = ('map', 'neighbor_map', 'map_rows', 'map_cols', 'life_init_ratio')

    def __init__(self, map_rows, map_cols, life_init_ratio):
        LifeGame.map = GameMap(map_rows, map_cols)
        LifeGame.map.reset(life_init_ratio)
        LifeGame.neighbor_map = [[0] * map_cols for j in range(map_rows)]

    def game_cycle(self):

        for row in range(LifeGame.map.rows):
            for col in range(LifeGame.map.cols):
                LifeGame.neighbor_map[row][col] = LifeGame.map.get_neighbor_count(row, col)
                # print LifeGame.neighbor_map[row][col], LifeGame.map.get_neighbor_count(row, col)

        for row in range(LifeGame.map.rows):
            for col in range(LifeGame.map.cols):
                if LifeGame.neighbor_map[row][col] == 3:
                    LifeGame.map.set(row, col, 1)
                elif LifeGame.neighbor_map[row][col] == 2:
                    pass
                else:
                    LifeGame.map.set(row, col, 0)

    def print_map(self):
        for i in range(LifeGame.map.rows):
            print [LifeGame.map.get(i, j) for j in range(LifeGame.map.cols)]

class GameTime(object):

    __slots__ = ('trigger', 'interval')

    def __init__(self, trigger, interval):

        pass

    def start(self):

        pass

def lifegame(row=8, col=8):
    # map = GameMap(row,col)
    # map.reset(0.3)
    # for i in range(map.rows):
    #         print [map.get(i, j) for j in range(map.cols)]
    os.system('clear')
    game = LifeGame(row, col, 0.4)
    MAX = 20
    for cnt in range(MAX):
        time.sleep(0.5)
        game.game_cycle()
        os.system('cls')
        game.print_map()

if __name__ == '__main__':
    lifegame(16, 16)

    # def gui()
    #
