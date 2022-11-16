#On admet la fonction input() qui renvoie la valeur donné par l'utilisateur.

#Definir une fonction morpion() qui lance une partie de morpion entre deux joueurs.
def morpion():
    #Definir un tableau de 3 x 3 avec des symboles vide.
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    #Definir un dictionaire dans lequel on stock le nom des joueurs
    curPlayer = {
        1: "Joueur 1",
        -1: "Joueur 2"
    }
    #Definir une variable à laquelle on assigne l'ID du joueur actuel
    curPlayerID = 1
    #Definir un dictionaire dans lequel on stock le symbole de chaque joueur en fonction de son ID
    playerSymbole = {
        1: "O",
        -1: "X"
    }

    #Tant que True
    while True:
        #Ecrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 
        print(f"{curPlayer[curPlayerID]}, c'est à toi !")

        #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
        choixX = int(input("coordonné x : "))
        #Si choixX ne rentre pas dans le tableau
        while choixX < 0 or choixX > 2:
        #Afficher un message d'erreur
            print("Choix invalide")
            #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
            choixX = float(input("coordonné x : "))
        #Assigner à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
        choixY = int(input("coordonné y : "))
        #Si choixY ne rentre pas dans le tableau
        if choixY < 0 or choixY > 2:
        #Afficher un message d'erreur
            print("Choix invalide")
            #Assigner à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
            choixY = int(input("coordonné y : "))

        #Si tab[choixX][choixY] est different de "_".
        if tab[choixX][choixY] != "_":
            #Alors on ecrit "case occupée, fais un autre choix".
            print("case occupée, fais un autre choix")
        
        #Sinon
        else:
            #Assigner le symbole du joueur aux coordonnées choixX, choixY dans tab.
            tab[choixX][choixY] = playerSymbole[curPlayerID]

        #Pour chaque element de tab
        for i in tab:
            #On imrpime la ligne du tableau
            print(i)

        #On stock temporairement le symbole du joueur actuel dans la variable cur.
        cur = playerSymbole[curPlayerID]
        #Si l'action du joueur est un action qui lui fait gagner la partie.
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            #Alors on ecrit quel joueur à gagné
            print(f"{curPlayer[curPlayerID]} a gagné")
            #Puis on force la sortie de la boucle infinie avec un break
            break
        
        #Si tab[choixX][choixY] est égal au symbole du joueur.
        if tab[choixX][choixY] == playerSymbole[curPlayerID]:
            #Alors on change l'ID de curPlayerID en multipliant la variable par -1.
            curPlayerID = curPlayerID * -1

morpion()