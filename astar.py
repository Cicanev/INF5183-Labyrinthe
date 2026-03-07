import heapq
from maze import get_neighbors

def heuristique(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def astar(maze, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, 0, start))
    
    came_from = {start: None}
    g_score = {start: 0}
    visited_order = [start]
    
    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        
        if current == goal:
            path = reconstruct_path(came_from, goal)
            return path, len(visited_order), visited_order
        
        for neighbor in get_neighbors(maze, *current):
            tentative_g = g_score[current] + 1
            
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristique(neighbor, goal)
                
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))
                if neighbor not in visited_order:
                    visited_order.append(neighbor)
    
    return None, len(visited_order), visited_order

def reconstruct_path(came_from, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path