# algorithms.py
import time
from constants import *
from queue import PriorityQueue
from collections import deque

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.color = YELLOW
        draw()

def bfs(draw, grid, start, end):
    queue = deque([start])
    came_from = {}
    visited = {start}

    while queue:
        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                neighbor.color = BLUE
                queue.append(neighbor)
                draw()
                time.sleep(0.02)
    return False


def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}
    visited = {start}

    while stack:
        current = stack.pop()

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                neighbor.color = BLUE
                stack.append(neighbor)
                draw()
                time.sleep(0.02)
    return False


def heuristic(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)


def astar(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic(start, end)

    open_set_hash = {start}

    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            return True

        for neighbor in current.neighbors:
            temp_g = g_score[current] + 1
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + heuristic(neighbor, end)
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.color = BLUE
        draw()
        time.sleep(0.02)
    return False
