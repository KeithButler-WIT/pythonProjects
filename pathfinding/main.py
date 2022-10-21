#!/usr/bin/env python3

import pygame
from grid import *
from aStar import *
from dijkstra import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualiser using pygame")
# pygame.display.set_caption("A* Pathfinding")
# pygame.display.set_caption("Dijkstra Pathfinding")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

def get_clicked_pos(pos, rows, width):
    gap = width //rows
    y,x = pos

    row = y//gap
    col = x//gap
    return row, col

def start_game(win, width, algo):
    ROWS = 50
    grid = make_grid(ROWS, width)
    start = None
    end = None
    run = True
    started = False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
            if started:
                continue
            if pygame.mouse.get_pressed()[0]:  # left mouse button
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start and  spot != end:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()
                elif spot != end and spot != start:
                    spot.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot ==start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbours(grid)
                    if algo == "aStar":
                        astar(lambda: draw(win, grid, ROWS, width), grid, start, end)   #having lambda lets you run the function inside the function
                    elif algo == "dijkstra":
                        dijkstra(lambda: draw(win, grid, ROWS, width), grid, start, end)   #having lambda lets you run the function inside the function

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)


    pygame.quit()


def text_objects(text, font):
    TextSurface = font.render(text, True, BLACK)
    return TextSurface, TextSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, algo):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if mouse_pos[0] > x and mouse_pos[0] < x + w and mouse_pos[1] > y and mouse_pos[1] < y + h:
        pygame.draw.rect(WIN, ac,(x,y,w,h))
        if click[0] == 1 and algo == "aStar":
            start_game(WIN, WIDTH, "aStar")
        if click[0] == 1 and algo == "dijkstra":
            start_game(WIN, WIDTH, "dijkstra")
    else:
        pygame.draw.rect(WIN, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    WIN.blit(textSurf, textRect)


# def button_old(x,y,w,h,algo):
#     pos = pygame.mouse.get_pos()
#     click = pygame.mouse.get_pressed()

#     smallText = pygame.font.Font("freesansbold.ttf",20)
#     textSurf, textRect = text_objects("GO!", smallText)
#     textRect.center = ( (w+(h/2)), (450+(50/2)) )
#     WIN.blit(textSurf, textRect)

#     if pos[0] > x and pos[0] < x + w and pos[1] > y and pos[1] < y + h:
#         pygame.draw.rect(WIN, WHITE, (x,y,w,h))


def main():
    menu()


def menu():
 while True:

    WIN.blit(WIN, (0, 0))


    button("aStar", WIDTH/4, WIDTH/2 + WIDTH/4, 80, 40, WHITE, GREEN,  "aStar")
    button("Dijkstra", WIDTH/4 + WIDTH/3,WIDTH/2 + WIDTH/4, 80, 40, WHITE, GREEN,  "dijkstra")
    # button(WIDTH/4 + WIDTH/3,WIDTH/2 + WIDTH/4,80,40,"dijkstra")

    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           pygame.quit()
    pygame.display.update()


if __name__ == "__main__":
    main()
