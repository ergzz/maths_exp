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

def valid(i, j):
    if  i>=0 and i<N1 and j>=0 and j<N2 and (not visited[i][j]):
        return True
    return False
        
def knight(i,j):
    visited = [[False]*N2 for _ in range(N1)]
    sol = []
    Q = []
    Q.append((i, j, 0))
    visited[i][j] = True
   
    x_move = [-1, -2, -2, -1, 1, 2, 2, 1]
    y_move = [-2, -1, 1, 2, -2, -1, 1, 2]
    while len(Q)!=0:
        i, j, min_moves = Q.pop(0)
        #print(x, y, min_moves)
        if i == x_ar and j == y_ar:
            board[x_ar][y_ar]=min_moves
            board[x][y]=0
            solution(board)
            #print(sol)
            #print(Q)
            return min_moves
        for k in range(8):
            next_x = i+x_move[k]
            next_y = j+y_move[k]
            if valid(next_x, next_y):
                sol.append((x_move[k],y_move[k]))
                visited[next_x][next_y] = True
                Q.append((next_x, next_y, min_moves+1))
                board[next_x][next_y]=min_moves+1
    return -1

def solution(board):
    for j in range(N2):
        for i in range(N1):
            print(board[i][j],"|", end='')
        print()

print(knight(x,y))
