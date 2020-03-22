'''Choisir la taille du plateau'''
N1 = int(input("Largeur du plateau:"))
N2 = int(input("Hauteur du plateau:"))
'''Choisir la case de départ'''
x = int(input("x:"))
y = int(input("y:"))
'''Choisir la case que l'on veut atteindre'''
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

min_moves=0
visited = [[False]*N2 for _ in range(N1)]

def valid(x, y):
    if  x>=0 and x<N1 and y>=0 and y<N2 and (not visited[x][y]):
        return True
    return False
        
def knight(x,y):
    visited = [[False]*N2 for _ in range(N1)]
    x, y = x-1, y-1
    Q = []
    Q.append((x, y, 0))
    visited[x][y] = True
    x_move = [-1, -2, -2, -1, 1, 2, 2, 1]
    y_move = [-2, -1, 1, 2, -2, -1, 1, 2]
    while len(Q)!=0:
        x, y, min_moves = Q.pop(0)
        #print(x, y, min_moves)
        if x == x_ar and y == y_ar:
            return min_moves
        for k in range(8):
            next_x = x+x_move[k]
            next_y = y+y_move[k]
            if valid(next_x, next_y):
                visited[next_x][next_y] = True
                Q.append((next_x, next_y, min_moves+1))
    return -1
                    
print(knight(x,y))
