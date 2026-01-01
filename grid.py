# grid.py
from constants import *

class Node:
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size
        self.color = WHITE
        self.neighbors = []

    def draw(self, canvas):
        x1 = self.col * self.size
        y1 = self.row * self.size
        x2 = x1 + self.size
        y2 = y1 + self.size
        canvas.create_rectangle(x1, y1, x2, y2, fill=self.color, outline=GREY)

    def update_neighbors(self, grid):
        self.neighbors = []
        rows = len(grid)

        if self.row < rows - 1 and grid[self.row + 1][self.col].color != BLACK:
            self.neighbors.append(grid[self.row + 1][self.col])
        if self.row > 0 and grid[self.row - 1][self.col].color != BLACK:
            self.neighbors.append(grid[self.row - 1][self.col])
        if self.col < rows - 1 and grid[self.row][self.col + 1].color != BLACK:
            self.neighbors.append(grid[self.row][self.col + 1])
        if self.col > 0 and grid[self.row][self.col - 1].color != BLACK:
            self.neighbors.append(grid[self.row][self.col - 1])


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap)
            grid[i].append(node)
    return grid
