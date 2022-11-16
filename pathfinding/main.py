#!/usr/bin/env python3

import pygame
import os

from grid import *
from aStar import *
from dijkstra import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

def get_clicked_pos(pos, rows, width):
    """
    Calculates the position on the grid was clicked
    (Window is assumed to be square)

    :params pos: Position of the mouse
    :params rows: Number of rows of grid squares on the screen
    :params width: width of each grid square
    :return: The row and col the was clicked
    """
    gap = width // rows
    y,x = pos

    row = y // gap
    col = x // gap
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
            if event.type == pygame.QUIT:
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

                if event.key == pygame.K_ESCAPE:
                    menu()

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)


    pygame.quit()


def text_objects(text, font, color=BLACK):
    """
    Creates a text object with inputted text and font

    :param text: Text to be returned
    :param font: The font for the text to use
    :param color: The color for the text to be
    :returns: TextSurface, TextSurface.get_rect()
    """
    TextSurface = font.render(text, True, color)
    return TextSurface, TextSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, algo):
    """
    Draw a button with text to the screen

    :param msg: A string to be displayed on the button
    :param x: x position on the screen
    :param y: y position on the screen
    :param w: Width of the button
    :param h: Height of the button
    :param ic: Buttons colour when not hovered over
    :param ac: Buttons colour when hovered over
    :param algo: A string of the pathfinding algorithm name
    """
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if mouse_pos[0] > x and mouse_pos[0] < x + w and mouse_pos[1] > y and mouse_pos[1] < y + h:
        pygame.draw.rect(WIN, ac,(x,y,w,h))
        if click[0] == 1 and algo == "aStar":
            pygame.display.set_caption("A* Pathfinding")
            start_game(WIN, WIDTH, "aStar")
        if click[0] == 1 and algo == "dijkstra":
            pygame.display.set_caption("Dijkstra Pathfinding")
            start_game(WIN, WIDTH, "dijkstra")
    else:
        pygame.draw.rect(WIN, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    WIN.blit(textSurf, textRect)


def main():
    """Runs the starting components of the program"""
    menu()


def menu():
    """Displays the main menu and changes the caption"""
    pygame.display.set_caption("Pathfinding Visualiser using pygame")
    WIN.fill(BLACK)

    # TODO: Display image as background
    background = pygame.image.load(os.path.join("images", "pathfinder-bw.png"))
    WIN.blit(background, (0,0))

    # Display an rect at the top of the screen with a 50px margin either size
    # pygame.draw.rect(WIN, WHITE, (50, 0, int(WIDTH-100), int(WIDTH/6)))

    while True:

        WIN.blit(WIN, (0, 0))


        button("aStar", WIDTH/4, WIDTH/2 + WIDTH/4, 80, 40, WHITE, GRAY,  "aStar")
        button("Dijkstra", WIDTH/4 + WIDTH/3,WIDTH/2 + WIDTH/4, 80, 40, WHITE, GRAY,  "dijkstra")
        # button(WIDTH/4 + WIDTH/3,WIDTH/2 + WIDTH/4,80,40,"dijkstra")

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()

        pygame.display.update()


if __name__ == "__main__":
    main()
