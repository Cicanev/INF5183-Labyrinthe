from collections import deque
from maze import get_neighbors

def bfs(maze, start, goal):
    queue = deque([start]) # file FIFO
    visited = set([start])
    parent = {start: None}
    visited_order = [start]
    
    while queue:
        current = queue.popleft()
        
        if current == goal:
            return reconstruct_path(parent, goal), len(visited_order), visited_order
        
        for neighbor in get_neighbors(maze, *current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = current
                visited_order.append(neighbor)
    
    return None, len(visited_order), visited_order

def reconstruct_path(parent, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    return path