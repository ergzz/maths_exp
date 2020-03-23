'''Choisir la taille du plateau'''
N1 = int(input("Largeur du plateau:"))
N2 = int(input("Hauteur du plateau:"))
'''Choisir la case de départ'''
x = int(input("x:"))
y = int(input("y:"))
'''Choisir la case que l'on veut atteindre'''
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

steps=0
visit = [[False]*N2 for _ in range(N1)] #liste vide pour ajouter cases déja visitées

board = []
for i in range(N2):
    a = ["x"]*N1
    board.append(a)

def valide(x, y): #regarde si case dans le plateau et pas déja visitée
    if x>=0 and x<N1 and y>=0 and y<N2 and (not visit[x][y]): #numérotation commence à 0 
        return True
    return False

def possiblePath(x,y):  
    visit = [[False]*N2 for _ in range(N1)]   
    sol=[]
    Q=[]
    Q.append((x,y,0))
    visit[x][y]=True
    board[x][y]=0
    mvmt_x = [-1, -2, -2, -1, 1, 2, 2, 1]
    mvmt_y = [-2, -1, 1, 2, -2, -1, 1, 2]
    while len(Q)!=0:
        x,y,steps = Q.pop(0)
        if x == x_ar and y == y_ar:
            solution(board)
            print(Q)
            print(steps)
            print(sol)
            return True

        for k in range(8): #longueur de la liste des différents mouvements
            next_x = x + mvmt_x[k]
            next_y = y + mvmt_y[k] #test mouvement pour chaque 
            if valide(next_x, next_y):
                sol.append((mvmt_x[k],mvmt_y[k]))
                visit[next_x][next_y]=True
                Q.append((next_x, next_y,steps+1))
                board[next_x][next_y]=steps
    return False

def solution(board): #visualisation 
    for x in range(N1):
        for y in range(N2):
            print(board[x][y],"|", end = '')
        print()

print(possiblePath(x,y))
            
