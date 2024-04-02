import random

import tileData as tileData
from random import choice
from threadHandler import task
import time
import pygame

px = tileData.dim


class cell:
    def __init__(self, coords, thread_handler, screen):
        self.screen = screen
        self.coords = coords
        self.thread_handler = thread_handler

        self.state = 1  # 0 = collapsed, 1 = ready, 2 = updating, 3 = update needed, -1 = collision
        self.edges = [set(tileData.connections.keys()) for _ in range(4)]
        self.options = [[tile, [0, 1, 2, 3]] for tile in tileData.edges.keys()]

        self.collapsed = [None, None]
        self.neighbours = [None, None, None, None]
        self.show()
        # print(coords)

    def __repr__(self):
        if self.state == 0:
            return tileData.tile_representations[self.collapsed[0]]
        return str(self.state) + " " + str(len(self.options))

    def show(self):
        if self.state == 0:
            self.screen.blit(pygame.transform.rotate(tileData.images[self.collapsed[0]], 90 * self.collapsed[1]),
                             self.coords)
        else:
            entropy = 1 - len(self.options) / len(tileData.edges.keys())
            colors = {1: (int(255 * entropy), int(255 * entropy), int(255 * entropy)),
                      2: (255, 50, 100),
                      3: (255, 200, 100),
                      -1: (0, 0, 0)}
            pygame.draw.rect(self.screen, colors[self.state], (self.coords[0], self.coords[1], px[0], px[1]))
        pygame.display.update()

    def testOption(self, tile, rotation):
        for side in (range(4)):
            if self.neighbours[side] is None:
                continue
            valid = list(self.neighbours[side].edges[(side + 2) % 4])
            try:
                con = list(tileData.connections[tileData.edges[tile][(side + rotation) % 4]])
            except:
                return False
            if not any(e in valid for e in con):
                # if tileData.connections[tileData.edges[tile][(side + rotation) % 4]] not in self.neighbours[side].edges[(side + 2) % 4]:
                return False
        return True

    def queueUp(self):
        # print("Q", int(self.coords[0] / px[0]), int(self.coords[1] / px[1]))
        self.setState(3)
        self.thread_handler.add_task(task(self.update, conditions=self.canUpdate))

    def canUpdate(self):
        for neighbour in self.neighbours:
            if neighbour is not None and neighbour.state in [2]:
                return False
        return True

    def update(self):
        # print("U", int(self.coords[0] / px[0]), int(self.coords[1] / px[1]))

        if self.state == -1:

            self.setState(2)
            updated_edges = [set(tileData.connections.keys()) for _ in range(4)]
            final_state = -1
        elif self.state == 0:

            self.setState(2)
            # print(self.collapsed)
            updated_edges = [{tileData.edges[self.collapsed[0]][(side + self.collapsed[1]) % 4]} for side in
                             range(4)]
            final_state = 0
        else:

            self.setState(2)
            updated_edges = [set() for _ in range(4)]

            time.sleep(2 / random.randint(3, 10))

            # print(self.options)

            tbdo = []
            for option in self.options:
                tbdr = []
                print (option)
                for rotation in option[1]:
                    if self.testOption(option[0], rotation):
                        for side in range(4):
                            updated_edges[side].add(tileData.edges[option[0]][(side + rotation) % 4])
                    else:
                        tbdr.append(rotation)
                for element in tbdr:
                    option[1].remove(element)
                if not option[1]:
                    tbdo.append(option)
            for element in tbdo:
                self.options.remove(element)

            # print(self.options)
            # print("\n\n\n")
            final_state = 1

        for side in range(4):
            if set(updated_edges[side]) != set(self.edges[side]):
                self.edges[side] = updated_edges[side]
                if self.neighbours[side] is not None and self.neighbours[side].state not in [0, -1]:
                    self.neighbours[side].queueUp()

        # print(int(self.coords[0] / px[0]), int(self.coords[1] / px[1]),":",self.edges)
        self.setState(final_state)
        self.show()

    def setState(self, state):
        self.state = state
        self.show()

    def collapse(self):
        # print(self.options)
        if len(self.options) == 0:
            self.setState(-1)
        if len(self.options) > 0:
            self.options = choice(self.options)
            self.collapsed[0] = self.options[0]
            self.options[1] = choice(self.options[1])
            self.collapsed[1] = self.options[1]
            self.setState(0)
        self.update()
