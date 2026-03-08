from maze import get_neighbors

def dfs(maze, start, goal):
    stack = [start]  # pile LIFO
    visited = set([start])
    parent = {start: None}
    visited_order = [start]
    
    while stack:
        current = stack.pop()
        
        if current == goal:
            return reconstruct_path(parent, goal), len(visited_order), visited_order
        
        neighbors = list(get_neighbors(maze, *current))[::-1]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
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