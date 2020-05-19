# maths_exp
experimental maths project

This code is meant to be used for the experimental maths project of Summer Semester 2020.

The goal of the project is to determine if a knight, starting from a point (x,y),  can reach another point (x',y') on an arbitrary rectangle chess board with (a,b) moves.

We also want the knight to perform as few moves as possible. 

Finally, we'd like to visualize the moves of the knight.

BFS versions : uses Breadth-First search to find shortest path (version with a regular knight + version with arbitrary (a,b)-knight).

DFS versions : uses Depth-First search to find out if coordinates reachable or not (version with a regular knight + version with arbitrary (a,b)-knight).

Visualisation: create animated SVG files then convert them online as .gif images.

We also want to consider "special" versions of chess: 
- what would it be like if instead of a board we play chess in a cube with a knight performing (a,b,c)-moves? (3D.py)
- what if when we reach the edge of the board, instead of the movement being impossible we just teleport on the other side of the board, like in the famous "snake" game? (snake.py)
- what if some squares of the chessboard did not exist, or if the board was not rectangle? (carré4.py, 2carré2.py, etc.)

Inspiration: in said folder, programs that inspired what approach to use for these problems. 
