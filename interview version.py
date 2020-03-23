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
board = [["x"]*N1 for i in range(N2)]

board[x][y]=0

def valid(x, y):
    if  x>=0 and x<N1 and y>=0 and y<N2 and (not visited[x][y]):
        return True
    return False
        
def knight(x,y):
    visited = [[False]*N2 for _ in range(N1)]
    sol = []
    Q = []
    Q.append((x, y, 0))
    visited[x][y] = True
    
    x_move = [-1, -2, -2, -1, 1, 2, 2, 1]
    y_move = [-2, -1, 1, 2, -2, -1, 1, 2]
    while len(Q)!=0:
        x, y, min_moves = Q.pop(0)
        #print(x, y, min_moves)
        if x == x_ar and y == y_ar:
            board[x_ar][y_ar]=min_moves
            solution(board)
            #print(sol)
            #print(Q)
            return min_moves
        for k in range(8):
            next_x = x+x_move[k]
            next_y = y+y_move[k]
            if valid(next_x, next_y):
                sol.append((x_move[k],y_move[k]))
                visited[next_x][next_y] = True
                Q.append((next_x, next_y, min_moves+1))
    return -1

def solution(board):
    for y in range(N2):
        for x in range(N1):
            print(board[x][y],"|", end='')
        print()

print(knight(x,y))
