import random

# Couleurs pour visualisation
BLUE = "\033[34m"
GREEN = "\033[32m"
RESET = "\033[0m"

# Génération du labyrinthe
def generate_maze(width=16, height=16, seed=None):
    if seed is not None:
        random.seed(seed)

    maze = [["#" for _ in range(width)] for _ in range(height)]
    start_row, start_col = 1, 1
    goal_row, goal_col = height - 2, width - 2

    maze[start_row][start_col] = "S"
    maze[goal_row][goal_col] = "G"
    
    # Chemin
    row, col = start_row, start_col

    while (row, col) != (goal_row, goal_col):
        options = []
        if row < goal_row:
            options.append((row + 1, col))
        if col < goal_col:
            options.append((row, col + 1))

        next_row, next_col = random.choice(options)
        row, col = next_row, next_col

        if maze[row][col] not in ("S", "G"):
            maze[row][col] = "."

    # Mise en forme du labyrinthe autour du chemin généré
    free_probability = 0.55

    for r in range(1, height - 1):
        for c in range (1, width - 1):
            if maze[r][c] in ("S", "G", "."):
                continue
            if random.random() < free_probability:
                maze[r][c] = "."

    return maze

# Récupération des points de départ et d'arrivée
def get_start(maze):
    return (1,1)

def get_goal(maze):
    height = len(maze)
    width = len(maze[0])
    return (height - 2, width -2)

# Vérification de l'état de la case (disponible ou non)
def is_free(maze, row, col):
    height = len(maze)
    width = len(maze[0])
    # Si hors bornes
    if row < 0 or row >= height or col < 0 or col >= width:
        return False
    return maze[row][col] != '#'

# Récupération des voisins disponibles
def get_neighbors(maze, row, col):
    neighbors = []
    # Haut
    if is_free(maze, row - 1, col):
        neighbors.append((row - 1, col))
    # Bas
    if is_free(maze, row + 1, col):
        neighbors.append((row + 1, col))
    # Gauche
    if is_free(maze, row, col - 1):
        neighbors.append((row, col - 1))
    # Droite
    if is_free(maze, row, col + 1):
        neighbors.append((row, col + 1))
    return neighbors

# Affichage du labyrinthe en console
def print_maze(maze):
    for row in maze:
        print(" ".join(row))
    return

# Affichage du labyrinthe avec l'exploration (p)
def display_exploration(maze, visited_order):
    display_copy = [row[:] for row in maze]
    
    for pos in visited_order:
        r, c = pos
        if display_copy[r][c] not in ('S', 'G', '#'):
            display_copy[r][c] = BLUE + 'p' + RESET
    
    print_maze(display_copy)

# Affichage du labyrinthe avec le chemin final (*)
def display_solution(maze, path):
    display_copy = [row[:] for row in maze]
    
    if path:
        for pos in path:
            r, c = pos
            display_copy[r][c] = GREEN + '*' + RESET
    
    print_maze(display_copy)

# Affichage du chemin trouvé
def print_path(path, start, goal):
    if not path:
        print("Aucun chemin trouvé.")
        return
    
    path_str = f"S{start} -> "
    for i, pos in enumerate(path[1:-1]): 
        path_str += f"{pos}"
        if i < len(path) - 3:
            path_str += " -> "
    path_str += f" -> G{goal}"
    print("Chemin :", path_str)

# Affichage des statistiques
def print_stats(path, explored_count, execution_time):
    print(f"Nombre de nœuds explorés : {explored_count}")
    print(f"Longueur du chemin trouvé : {len(path) - 1 if path else 0} étapes")
    print(f"Temps d'exécution : {execution_time:.3f} millisecondes")