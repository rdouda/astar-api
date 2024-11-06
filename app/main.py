from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Tuple, Optional
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class Cell(BaseModel):
    x: int
    y: int
    isBarrier: bool
    isStart: bool
    isEnd: bool

class PathfindingRequest(BaseModel):
    grid: List[List[Cell]]
    start: Tuple[int, int]
    end: Tuple[int, int]

def astar(grid: List[List[Cell]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    open_list = []
    closed_list = set()
    came_from = {}

    def heuristic(a, b):
        # Manhattan distance as the heuristic
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(node):
        x, y = node
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Adding diagonals
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                # If moving diagonally, ensure that the adjacent cells are not barriers
                if (dx != 0 and dy != 0):  # Diagonal movement
                    if (not grid[x + dx][y].isBarrier and not grid[x][y + dy].isBarrier):
                        if not grid[nx][ny].isBarrier:
                            neighbors.append((nx, ny))
                else:  # Vertical or horizontal movement
                    if not grid[nx][ny].isBarrier:
                        neighbors.append((nx, ny))
        return neighbors

    open_list.append((start, 0 + heuristic(start, end), 0))  # (position, f_score, g_score)
    g_scores = {start: 0}
    f_scores = {start: heuristic(start, end)}

    while open_list:
        current, _, _ = min(open_list, key=lambda x: x[1])

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        open_list = [item for item in open_list if item[0] != current]  # Remove current from open list
        closed_list.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_list:
                continue
            tentative_g_score = g_scores[current] + (1 if current[0] == neighbor[0] or current[1] == neighbor[1] else 1.414)

            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristic(neighbor, end)
                open_list.append((neighbor, f_scores[neighbor], g_scores[neighbor]))

    return None  # No path found


@app.post("/find-path")
async def find_path(request: PathfindingRequest):
    grid = request.grid
    start = request.start
    end = request.end

    path = astar(grid, start, end)

    if path:
        print({"path": path})
        return {"path": path}
    else:
        return {"message": "No path found"}
