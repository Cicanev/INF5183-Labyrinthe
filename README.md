# Algorithmes de Recherche dans un Labyrinthe
*Implémentation et comparaison de DFS, BFS et A**
>Cours : INF5183 - Fondements de l'Intelligence Artificielle
>Étudiante : Cindy CANÉVET - DESS SDIA, UQO, Hiver 2026

## À propos
Le projet vise à se familiariser avec les algorithmes de recherche fondamentaux de l'Intelligence Artificielle.
Nous implémenterons les appproches de recherche non-informée DFS (Depth-First Search), BFS (Breadth-First Search) et informée A* (A-Star) afin de résoudre un labyrinthe, en comparant leurs performances.

## Fonctionnalités
| Fonctionnalité   | Description                                      |
| ---------------- | ------------------------------------------------ |
| 🎲 Générateur    | Labyrinthe 16x16 avec chemin garanti S→G         |
| 🔍 3 algorithmes | DFS (pile), BFS (file), A* (Manhattan)           |
| 📊 Visualisation | Exploration (p), solution (*), statistiques      |
| 🎮 Interface     | Sélection interactive de clé de labyrinthe       |
| 📈 Benchmark     | Tableau comparatif nœuds/longueur/temps          |

## Utilisation
Depuis la racine du projet, lancer :
```bash
python main.py
```

Choisir un nombre aléatoire (entier) :
```
🔑 SÉLECTION DE LA CLÉ DU LABYRINTHE
0   = Labyrinthe aléatoire (différent à chaque fois)
42  = Labyrinthe n°1 (fixe)
123 = Labyrinthe n°2 (fixe)
777 = Labyrinthe n°3 (fixe)
Autre = Votre propre labyrinthe
```
Appuyer sur `Entrée` pour lancer le processus.

## Structure du projet
```
Devoir_I/
├── maze.py      # Génération et affichage du labyrinthe
├── dfs.py       # Depth-First Search (pile LIFO)
├── bfs.py       # Breadth-First Search (file FIFO)
├── astar.py     # A* avec heuristique Manhattan
├── main.py      # Interface + comparatifs
├── .gitignore   # Enlève le cache Python du versionnement
└── README.md 
```

## Exemple (clé 42)

```
LABYRINTHE ORIGINAL

################
#S.#........#..#
#.##...#####..##
#....###.#....##
##...#.##..###.#
#..##..#.#.#.#.#
#..##..##.#..###
##..###....#####
#....##....#####
#....##..#.###.#
#.#.#..######.##
#.#.....##.#...#
#......###....##
#...#.##.##....#
#.............G#
################

============================================================


==================================================
ALGORITHME : DFS
==================================================

--- EXPLORATION ---
################
#Sp#........#..#
#p##...#####..##
#ppp.###.#....##
##pp.#.##..###.#
#pp##..#.#.#.#.#
#pp##..##.#..###
##pp###....#####
#ppp.##....#####
#ppp.##..#.###.#
#p#p#pp######p##
#p#pppp.##p#ppp#
#pppppp###pppp##
#ppp#p##p##pppp#
#pppppppppppppG#
################

--- SOLUTION ---
################
#*.#........#..#
#*##...#####..##
#**..###.#....##
##*..#.##..###.#
#.*##..#.#.#.#.#
#.*##..##.#..###
##*.###....#####
#.*..##....#####
#**..##..#.###.#
#*#.#..######.##
#*#***..##.#...#
#*.*.*.###.***##
#*.*#*##.##*.*.#
#***.*******.**#
################

--- CHEMIN ---
Chemin : S(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (4, 2) -> (5, 2) -> (6, 2) -> (7, 2) -> (8, 2) -> (9, 2) -> (9, 1) -> (10, 1) -> (11, 1) -> (12, 1) -> (13, 1) -> (14, 1) -> (14, 2) -> (14, 3) -> (13, 3) -> (12, 3) -> (11, 3) -> (11, 4) -> (11, 5) -> (12, 5) -> (13, 5) -> (14, 5) -> (14, 6) -> (14, 7) -> (14, 8) -> (14, 9) -> (14, 10) -> (14, 11) -> (13, 11) -> (12, 11) -> (12, 12) -> (12, 13) -> (13, 13) -> (14, 13) -> G(14, 14)

--- STATISTIQUES ---
Nombre de nœuds explorés : 67
Longueur du chemin trouvé : 38 étapes
Temps d'exécution : 0.423 millisecondes

==================================================
ALGORITHME : BFS
==================================================

--- EXPLORATION ---
################
#Sp#pppppppp#..#
#p##ppp#####..##
#pppp###.#....##
##ppp#.##..###.#
#pp##..#.#.#.#.#
#pp##..##.#..###
##pp###....#####
#pppp##....#####
#pppp##..#.###.#
#p#p#pp######.##
#p#ppppp##p#p..#
#pppppp###pppp##
#ppp#p##p##pppp#
#pppppppppppppG#
################

--- SOLUTION ---
################
#*.#........#..#
#*##...#####..##
#**..###.#....##
##*..#.##..###.#
#.*##..#.#.#.#.#
#.*##..##.#..###
##*.###....#####
#.*..##....#####
#.**.##..#.###.#
#.#*#..######.##
#.#*....##.#...#
#..*...###....##
#..*#.##.##....#
#..************#
################

--- CHEMIN ---
Chemin : S(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (4, 2) -> (5, 2) -> (6, 2) -> (7, 2) -> (8, 2) -> (9, 2) -> (9, 3) -> (10, 3) -> (11, 3) -> (12, 3) -> (13, 3) -> (14, 3) -> (14, 4) -> (14, 5) -> (14, 6) -> (14, 7) -> (14, 8) -> (14, 9) -> (14, 10) -> (14, 11) -> (14, 12) -> (14, 13) -> G(14, 14)

--- STATISTIQUES ---
Nombre de nœuds explorés : 80
Longueur du chemin trouvé : 26 étapes
Temps d'exécution : 0.098 millisecondes

==================================================
ALGORITHME : A*
==================================================

--- EXPLORATION ---
################
#Sp#........#..#
#p##p..#####..##
#pppp###.#....##
##ppp#.##..###.#
#pp##..#.#.#.#.#
#pp##..##.#..###
##pp###....#####
#pppp##....#####
#pppp##..#.###.#
#.#p#pp######.##
#.#ppppp##.#...#
#.ppppp###....##
#.pp#p##p##ppp.#
#.ppppppppppppG#
################

--- SOLUTION ---
################
#*.#........#..#
#*##...#####..##
#**..###.#....##
##*..#.##..###.#
#.*##..#.#.#.#.#
#.*##..##.#..###
##**###....#####
#..*.##....#####
#..*.##..#.###.#
#.#*#..######.##
#.#***..##.#...#
#....*.###....##
#...#*##.##....#
#....**********#
################

--- CHEMIN ---
Chemin : S(1, 1) -> (2, 1) -> (3, 1) -> (3, 2) -> (4, 2) -> (5, 2) -> (6, 2) -> (7, 2) -> (7, 3) -> (8, 3) -> (9, 3) -> (10, 3) -> (11, 3) -> (11, 4) -> (11, 5) -> (12, 5) -> (13, 5) -> (14, 5) -> (14, 6) -> (14, 7) -> (14, 8) -> (14, 9) -> (14, 10) -> (14, 11) -> (14, 12) -> (14, 13) -> G(14, 14)

--- STATISTIQUES ---
Nombre de nœuds explorés : 58
Longueur du chemin trouvé : 26 étapes
Temps d'exécution : 0.103 millisecondes

============================================================
          TABLEAU COMPARATIF
============================================================

✅ Résultats avec la clé 42 :

Algorithme          Noeuds  Longueur  Temps (ms)
------------------------------------------------
DFS                 67      38        0.423
BFS                 80      26        0.098
A* (manhattan)      58      26        0.103
------------------------------------------------
```

## Prérequis

Python standard (3.11) est suffisant (dépendances internes utilisées : `random`, `time`, `collections.deque`, `heapq`).

