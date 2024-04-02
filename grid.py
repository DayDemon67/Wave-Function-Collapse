import random

from cell import cell
from tileData import dim as tilePx
from random import choice
from threadHandler import threadHandler
import time

class grid:
    def __init__(self, screen, size=20):
        self.screen = screen
        self.thread_handler = threadHandler()
        self.thread_handler.start()
        self.cells = [[cell((x * tilePx[0], y * tilePx[1]), self.thread_handler,self.screen) for x in range(size)] for y in
                      range(size)]
        for y in range(size):
            for x in range(size):
                neighbours = []
                for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    new_y, new_x = y + dy, x + dx
                    if 0 <= new_y < size and 0 <= new_x < size:
                        neighbours.append(self.cells[new_y][new_x])
                    else:
                        neighbours.append(None)
                self.cells[y][x].neighbours = neighbours

    def collapseRandom(self):
        indices = [(i, j) for i, row in enumerate(self.cells) for j, cell in enumerate(row) if cell.collapsed == [None,None]]
        #print (indices)
        if len(indices) == 0:
            return False
        random.shuffle(indices)
        target = min(indices,key = lambda x:len(self.cells[x[0]][x[1]].options))
        #print (target)
        self.cells[target[0]][target[1]].collapse()
        return True

    def printProgress(self):
        for row in self.cells:
            print(row)

    def stop_thread_handler(self):
        self.thread_handler.stop()






