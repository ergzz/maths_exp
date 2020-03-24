import sys
sys.setrecursionlimit(2000)

'''Choisir la taille du plateau'''
N1 = int(input("Largeur du plateau:"))
N2 = int(input("Hauteur du plateau:"))
'''Choisir la case de départ'''
x = int(input("x:"))
y = int(input("y:"))
'''Choisir la case que l'on veut atteindre'''
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

mvmt_x= [-1, -2, -2, -1, 1, 2, 2, 1]
mvmt_y = [-2, -1, 1, 2, -2, -1, 1, 2]

visit = [] #liste vide pour ajouter cases déja visitées
steps = 0
board = [["x"]*N1 for i in range(N2)]


def valide(i, j): #regarde si case dans le plateau et pas déja visitée
    if ((i>=0) and (i<N1) and (j>=0) and j<N2): 
        if not (i,j) in visit: 
            return True
    return False

def possiblePath(i,j,steps):    
    board[x][y]=0
    if i == x_ar and j == y_ar:
        solution(board)
        print(steps)
        print(visit)
        return True

    for k in range(0,8): #longueur de la liste des différents mouvements
        next_x = i + mvmt_x[k]
        next_y = j + mvmt_y[k] #test mouvement pour chaque 
        if valide(next_x, next_y):
            steps+=1
            visit.append((mvmt_x[k],mvmt_y[k]))
            board[next_x][next_y]=steps
            if (possiblePath(next_x,next_y,steps)): #recursion
                return True 
    return False

def solution(board): #visualisation 
    for j in range(N2):
        for i in range(N1):
            print(board[i][j], end = '')
        print()

print(possiblePath(x,y,0))