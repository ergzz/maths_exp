
from timeit import default_timer

'''Choisir la taille du plateau'''
N1 = int(input("Largeur du plateau:"))
N2 = int(input("Hauteur du plateau:"))
'''Choisir la case de départ'''
x = int(input("x:"))
y = int(input("y:"))
'''Choisir la case que l'on veut atteindre'''
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))

steps = 0
visited = [[False]*N2 for _ in range(N1)]
sol=[]
board = [["x"]*N1 for i in range(N2)]

def valide(i, j): #regarde si case dans le plateau et pas déja visitée
    if ((i>=0) and (i<N1) and (j>=0) and j<N2) and (not visited[i][j]): 
        return True
    return False

def possiblePath(i,j,steps):  
    Q = []
    Q.append((i,j,steps))
    mvmt_x= [-1, -2, -2, -1, 1, 2, 2, 1]
    mvmt_y = [-2, -1, 1, 2, -2, -1, 1, 2]  
    if i == x_ar and j == y_ar:
        board[x_ar][y_ar]=steps #visualisation: nombre minimal de mouvements sur la case d'arrivée
        board[x][y]=0 #0 sur la case de départ
        solution(board)
        print(Q)
        print(steps)
        return True
    while len(Q)!=0:
        i,j,steps = Q.pop(0)
        for k in range(0,8): #longueur de la liste des différents mouvements
            next_x = i + mvmt_x[k]
            next_y = j + mvmt_y[k] #test mouvement pour chaque 
            if valide(next_x, next_y):
                visited[next_x][next_y]=steps 
                sol.append((mvmt_x[k],mvmt_y[k]))
                Q.append((next_x,next_y, steps+1))
                if possiblePath(next_x,next_y,steps+1): #recursion
                    return True 
                visited[next_x][next_y]=-1;
        return False
    return False  


def solution(board): #visualisation 
    for j in range(N2):
        for i in range(N1):
            print(board[i][j],'|', end = '')
        print()

start = default_timer()
print(possiblePath(x,y,0))
end = default_timer()

print(end-start)