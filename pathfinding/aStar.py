#!/usr/bin/env python3


import pygame
from queue import PriorityQueue


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


# Gets the absolute distance between the start and end node
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1-x2) + abs(y1-y2)


def astar(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()   # returns the smallest value in the list
    open_set.put((0, count, start))
    came_from = {}
    # Distance from start to current node
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0
    # g_score + h_score
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}
    while not open_set.empty():
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
        current = open_set.get()[2]      # returns the best value
        open_set_hash.remove(current)
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbour in current.neighbours:
            temp_g_score = g_score[current]+1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())
                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_open()
        draw()
        if current != start:
            current.make_closed()

    return False
