import time
from maze import (generate_maze, get_start, get_goal, print_maze,
                 display_exploration, display_solution, print_path, print_stats)
from bfs import bfs
from dfs import dfs
from astar import astar
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_seed():
    print("\n" + "="*60)
    print("     🔑 SÉLECTION DE LA CLÉ DU LABYRINTHE")
    print("="*60)
    print("0   = Labyrinthe différent à chaque fois")
    print("42  = Labyrinthe n°1 (fixe)")
    print("123 = Labyrinthe n°2 (fixe)")
    print("777 = Labyrinthe n°3 (fixe)")
    print("Autre = Votre propre labyrinthe")
    
    while True:
        try:
            choice = input("\nVotre clé (0 pour aléatoire) : ").strip()
            if choice == "0":
                return None
            seed = int(choice)
            return seed
        except ValueError:
            print("❌ Entrez un nombre entier (ex: 42, 123, 0)")
        except KeyboardInterrupt:
            print("\n👋 Au revoir !")
            exit()

def run(algorithm, algorithm_function, maze, start, goal):
    print(f"\n{'='*50}")
    print(f"ALGORITHME : {algorithm.upper()}")
    print('='*50)

    start_time = time.perf_counter()
    path, explored_count, visited_order = algorithm_function(maze, start, goal)
    execution_time = (time.perf_counter() - start_time) * 1000

    print("\n--- EXPLORATION ---")
    display_exploration(maze, visited_order)
    
    print("\n--- SOLUTION ---")
    display_solution(maze, path)
    
    print("\n--- CHEMIN ---")
    print_path(path, start, goal)
    
    print("\n--- STATISTIQUES ---")
    print_stats(path, explored_count, execution_time)

    return len(visited_order), len(path)-1 if path else 0, execution_time

def print_comparison_table(results, seed_info):
    print("\n" + "="*60)
    print("          TABLEAU COMPARATIF")
    print("="*60)
    print(f"\n✅ Résultats avec la clé {seed_info} :\n")
    print("Algorithme          Noeuds  Longueur  Temps (ms)")
    print("-" * 48)
    
    for algo, (nodes, length, time_ms) in results.items():
        print(f"{algo:<15} {nodes:>6}  {length:>6}        {time_ms:.3f}")
    
    print("-" * 48)

if __name__ == "__main__":
    seed = get_user_seed()
    seed_info = "aléatoire" if seed is None else f"{seed}"

    maze = generate_maze(seed=seed)
    start = get_start(maze)
    goal = get_goal(maze)
    
    print(f"\n✅ Labyrinthe généré avec la clé {seed_info}")
    print("Appuyez sur Entrée pour continuer...")
    input()
    clear_screen()

    print("LABYRINTHE ORIGINAL" + "\n")
    print_maze(maze)
    print("\n" + "="*60 + "\n")
    
    dfs_result = run("DFS", dfs, maze, start, goal)
    bfs_result = run("BFS", bfs, maze, start, goal)
    astar_result = run("A*", astar, maze, start, goal)

    results = {
            "DFS": dfs_result,
            "BFS": bfs_result, 
            "A* (manhattan)": astar_result
        }
    
    print_comparison_table(results, seed_info)

    print("\n" + "="*60)
    print("🎉 RECHERCHES TERMINÉES")
    print("👉 Relancez pour tester une autre clé !")