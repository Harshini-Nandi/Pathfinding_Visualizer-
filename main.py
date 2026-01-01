# main.py
from tkinter import *
from constants import *
from grid import *
from algorithms import *

root = Tk()
root.title("Pathfinding Visualizer")

canvas = Canvas(root, width=WIDTH, height=WIDTH)
canvas.pack()

grid = make_grid(ROWS, WIDTH)
start = None
end = None

def draw():
    canvas.delete("all")
    for row in grid:
        for node in row:
            node.draw(canvas)
    root.update()

def click(event):
    global start, end
    row = event.y // (WIDTH // ROWS)
    col = event.x // (WIDTH // ROWS)
    node = grid[row][col]

    if not start:
        start = node
        node.color = GREEN
    elif not end and node != start:
        end = node
        node.color = RED
    elif node != start and node != end:
        node.color = BLACK
    draw()

def prepare():
    for row in grid:
        for node in row:
            node.update_neighbors(grid)

def run_bfs():
    prepare()
    bfs(draw, grid, start, end)

def run_dfs():
    prepare()
    dfs(draw, grid, start, end)

def run_astar():
    prepare()
    astar(draw, grid, start, end)

Button(root, text="BFS", command=run_bfs).pack(side=LEFT)
Button(root, text="DFS", command=run_dfs).pack(side=LEFT)
Button(root, text="A*", command=run_astar).pack(side=LEFT)

canvas.bind("<Button-1>", click)

draw()
root.mainloop()
