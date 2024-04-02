import pygame
import sys
from grid import grid
from tileData import dim as px


dim = 60

pygame.init()

canvas_width = dim*px[0]
canvas_height = dim*px[1]

screen = pygame.display.set_mode((canvas_width, canvas_height))
wfc = grid(screen, dim)
pygame.display.set_caption("WFC")



# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wfc.thread_handler.stop()
            pygame.quit()
            sys.exit()

    if wfc.thread_handler.check_idle():
        if not wfc.collapseRandom():
            wfc.stop_thread_handler()
        #print("\n\n\n")
        #wfc.printProgress()
