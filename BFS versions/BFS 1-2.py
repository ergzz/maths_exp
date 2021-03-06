from timeit import default_timer

print("ATTENTION: la numérotation commence à 0")

print("Choisir la taille du plateau")
N1 = int(input("Largeur du plateau:"))
N2 = int(input("Hauteur du plateau:"))

print("Choisir la case de départ")
x = int(input("x:"))
y = int(input("y:"))

print("Choisir la case que l'on veut atteindre")
x_ar = int(input("x à atteindre:"))
y_ar = int(input("y à atteindre:"))



min_moves=0 #initialise nombre de mouvements
visited = [[False]*N2 for _ in range(N1)] #aucune case n'est visitée au début
board = [["x"]*N1 for i in range(N2)] #crée un plateau pour visualiser résultat final 

def valid(i, j):
    if  i>=0 and i<N1 and j>=0 and j<N2 and (not visited[i][j]): #verifie si la case est dans le plateau + si elle n'a pas été déja visitée
        return True
    return False
        
def knight(i,j):
    sol = [] #liste de solutions vide: cases testées 
    sol.append((i,j)) #ajoute position de départ dans la liste
    Q = [] #queue pour utiliser BFS 
    Q.append((i, j, 0))
    visited[i][j] = True #marque première case visitée comme vraie
   
    x_move = [-1, -2, -2, -1, 1, 2, 2, 1] #liste des mouvements dans directions x et y
    y_move = [-2, -1, 1, 2, -2, -1, 1, 2]
    
    while len(Q)!=0: #début du Breadth-First Search: continue tant que la longueur de queue est diff de 0
        i, j, min_moves = Q.pop(0) #enleve elément d'indice 0
        if i == x_ar and j == y_ar: #teste si on est arrivés à la position voulue
            sol.append((x_ar,y_ar))
            board[x_ar][y_ar]=min_moves #visualisation: nombre minimal de mouvements sur la case d'arrivée
            board[x][y]=0 #0 sur la case de départ
            solution(board) 
            sol = list(dict.fromkeys(sol)) #enlève les doubles dans la liste de solution en la transformant en dict puis à nouveau en liste: montre toutes les cases testées
            print(sol)
            print("Le nombre minimal de mouvements est:")
            return min_moves
        for k in range(8): #boucle *8 car longueur du nb de mouvements possibles
            next_x = i+x_move[k]
            next_y = j+y_move[k]
            if valid(next_x, next_y): #vérifie validité
                sol.append((i,j)) #ajoute case visitée à liste des sols
                visited[next_x][next_y] = True #marque case comme visitée
                Q.append((next_x, next_y, min_moves+1)) #ajoute dans queue 
    return -1 #rend -1 si impossible à atteindre

def solution(board): #visualisation du plateau + arrivée et départ 
    for j in range(N2):
        for i in range(N1):
            print(board[i][j],"|", end='')
        print()

start=default_timer() #mesure temps mis par l'algo: timeit serait meilleur? 
print(knight(x,y))
end = default_timer()

print("Le temps mis par le programme est:", end-start,"s")
