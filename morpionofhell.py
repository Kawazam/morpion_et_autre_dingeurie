def playerVesusTerminatorGame():
    #Definir un tableau de 3 x 3 avec des symboles vide.
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    #Definir un dictionaire dans lequel on stock le nom des joueurs
    curPlayer = {
        1: "Joueur 1",
        -1: "Terminator"
    }
    #Definir une variable à laquelle on assigne l'ID du joueur actuel
    curPlayerID = 1
    #Definir un dictionaire dans lequel on stock le symbole de chaque joueur en fonction de son ID
    playerSymbole = {
        1: "O",
        -1: "X"
    }
    #Définir la variable actionTurn à 0
    actionTurn = 0

    #Rentrer la première action de Terminator qui joue aux coordonnées [1][1]
    tab[1][1] = "X"

    #Tant que True
    while True:

        #Initialiser check à False
        check = False
        #Tant que check est False
        while not check:
            #Si le joueur est cpu
            if curPlayerID == -1:
                print("Au tour de Terminator")



                #Si actionTurn est égal à 1
                if actionTurn == 1:
                    #Si la position 2-2 est égale à "O" ou si la position 0-0 est égale à "O"
                    if tab[2][2] == "O" or tab[0][0] == "O":
                        #placer le symbole du joueur à la position 2-0
                        tab[2][0] = "X"
                    #Sinon si la position 2-2 est différent de "_"
                    elif tab[2][2] == "_":
                        #placé le symbole du joueur à la position 2-2
                        tab[2][2] = "X"
                #Sinon si actionTurn est égale 3
                elif actionTurn == 3:
                    #Si la position la position 2-2 est égale à "X" et que la position 0-0 est égale à "_"
                    if tab[2][2] == "X" and tab[0][0] == "_":
                        #placé le symbole du joueur à la position 0-0
                        tab[0][0] = "X"
                    #Sinon si la position 2-0 est égale à "X" et que la position 0-2 est égale à "_"
                    elif tab[2][0] == "X" and tab[0][2] == "_":
                        #placé le symbole du joueur à la position 0-2
                        tab[0][2] = "X"
                    #Sinon si la position 0-0 est égale à "O"
                    elif tab[0][0] == "O":
                        #Si la position 1-0 est égale à "O"
                        if tab[1][0] == "O":
                            #placé le symbole du joueur à la position 2-0
                            tab[2][0] = "X"
                        #Sinon si la position 2-0 est égale à "O"
                        elif tab[2][0] == "O":
                            #placé le symbole du joueur à la position 1-0
                            tab[1][0] = "X"
                        #Sinon si la position 0-2 est égale à "O"
                        elif tab[0][2] == "O":
                            #placé le symbole du joueur à la position 0-1
                            tab[0][1] = "X"
                        #Sinon si la position 0-1 est égale à "O"
                        elif tab[0][1] == "O":
                            #placé le symbole du joueur à la position 0-2
                            tab[0][2] = "X"
                        #Sinon
                        else:
                            #placé le symbole du joueur à la position 2-0
                            tab[2][0] = "X"
                    #Sinon si la position 2-0 est égale à "X" et que la position 0-0 est égale à "O"
                    elif tab[2][0] == "X" and tab[0][0] == "O":
                        #placé le symbole du joueur à la position 0-1
                        tab[0][1] = "X"
                    #Sinon si la position 2-0 est égale à "X" et que la position 2-2 est égale à "O"
                    elif tab[2][0] == "X" and tab[2][2] == "O":
                        #placé le symbole du joueur à la position 1-2
                        tab[1][2] = "X"
                    #Sinon
                    else:
                        #placé le symbole du joueur à la position 2-0
                        tab[2][0] = "X"
                #Sinon si actionTurn est égale à 5
                elif actionTurn == 5:
                    #Si il y une situation de victoire assuré au positions 1-1  2-2  2-0
                    if tab[1][1] == "X" and tab[2][2] == "X" and tab[2][0] == "X":
                        #Si le joueur joue en 2-1
                        if tab[2][1] == "O":
                            #Jouer en 0-2
                            tab[0][2] = "X"
                        #Si le joueur joue en 0-2
                        elif tab[0][2] == "O":
                            #Jouer en 2-1
                            tab[2][1] = "X"
                        #Sinon
                        else:
                            #placé le symbole du joueur à la position 0-2
                            tab[0][2] = "X"
                    #Sinon si il y a une situation de victoire assuré au positions 1-1  2-2  0-2
                    elif tab[1][1] == "X" and tab[2][2] == "X" and tab[0][2] == "X":
                        #Si le joueur joue en 1-2
                        if tab[1][2] == "O":
                            #Jouer en 2-0
                            tab[2][0] = "X"
                        #Si le joueur joue en 2-0
                        elif tab[2][0] == "O":
                            #Jouer en 1-2
                            tab[1][2] = "X"
                        #Sinon
                        else:
                            #placé le symbole du joueur à la position 2-0
                            tab [2][0] = "X"
                    #Sinon si il peut gagner directement il le fait
                    elif tab[1][1] == "X" and tab[1][0] == "X":
                        tab[1][2] = "X"
                    elif tab[1][1] == "X" and tab[1][2] == "X":
                        tab[1][0] = "X"
                    elif tab[1][1] == "X" and tab[0][1] == "X":
                        tab[2][1] = "X"
                    elif tab[1][1] == "X" and tab[2][1] == "X":
                        tab[0][1] = "X"
                    #Si la position 1-2 est égale à "_"
                    elif tab[2][1] == "_":
                        #placé le symbole du joueur à la position 1-2
                        tab[2][1] = "X"
                    #Sinon si la position 2-1 est égale à "_"
                    elif tab[1][2] =="_":
                        #placé le symbole du joueur à la position 2-1
                        tab[1][2] = "X"
                    #Sinon si la position 1-0 est égale à "_"
                    elif tab[1][0] == "_":
                        #placé le symbole du joueur à la position 1-0
                        tab[1][0] = "X"
                    #Sinon si la position 0-1 est égale à "_"
                    elif tab[0][1] == "_":
                        #placé le symbole du joueur à la position 0-1
                        tab[0][1] = "X"
                    #Sinon si la position 0-2 est égale à "_"
                    elif tab[0][2] == "_":
                        #placé le symbole du joueur à la position 0-2
                        tab[0][2] = "X"
                    #Sinon si la position 2-0 est égale à "_"
                    elif tab[2][0] == "_":
                        #placé le symbole du joueur à la position 2-0
                        tab[2][0] = "X"
                    elif tab[2][2] == "_":
                        tab[2][2] = "X"
                #Sinon si actionTurn est égale à 7
                elif actionTurn == 7:
                    #Sinon si il peut gagner directement il le fait
                    if tab[1][1] == "X" and tab[1][0] == "X":
                        tab[1][2] = "X"
                    elif tab[1][1] == "X" and tab[1][2] == "X":
                        tab[1][0] = "X"
                    elif tab[1][1] == "X" and tab[0][1] == "X":
                        tab[2][1] = "X"
                    elif tab[1][1] == "X" and tab[2][1] == "X":
                        tab[0][1] = "X"
                    #Si la position 1-2 est égale à "_"
                    elif tab[1][2] == "_":
                        #placé le symbole du joueur à la position 1-2
                        tab[1][2] = "X"
                    #Sinon si la position 2-1 est égale à "_"
                    elif tab[2][1] =="_":
                        #placé le symbole du joueur à la position 2-1
                        tab[2][1] = "X"
                    #Sinon si la position 1-0 est égale à "_"
                    elif tab[1][0] == "_":
                        #placé le symbole du joueur à la position 1-0
                        tab[1][0] = "X"
                    #Sinon si la position 0-1 est égale à "_"
                    elif tab[0][1] == "_":
                        #placé le symbole du joueur à la position 0-1
                        tab[0][1] = "X"
                    #Sinon si la position 0-2 est égale à "_"
                    elif tab[0][2] == "_":
                        #placé le symbole du joueur à la position 0-2
                        tab[0][2] = "X"
                    #Sinon si la position 2-0 est égale à "_"
                    elif tab[2][0] == "_":
                        #placé le symbole du joueur à la position 2-0
                        tab[2][0] = "X"
                    elif tab[2][2] == "_":
                        tab[2][2] = "X"
                    elif tab[0][0] == "_":
                        tab[0][0] = "X"



            #Sinon si curPlayerID égale à 1
            else:
                #Ecrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 
                print(f"{curPlayer[curPlayerID]}, c'est à toi !")

                #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
                choixX = int(input("coordonné x : "))
                #Si choixX ne rentre pas dans le tableau
                while choixX < 0 or choixX > 2:
                    #Afficher un message d'erreur
                    print("Choix invalide")
                #Assigner à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
                choixY = int(input("coordonné y : "))
                #Si choixY ne rentre pas dans le tableau
                if choixY < 0 or choixY > 2:
                #Afficher un message d'erreur
                    print("Choix invalide")
                    #Assigner à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
                    choixY = int(input("coordonné y : "))

            #Si tab[choixX][choixY] est different de "_".
            if tab[choixX][choixY] != "_" and curPlayerID == 1:
                #Si curPlayerID égale à 1
                if curPlayerID == -1:
                    #On ecrit "case occupée, fais un autre choix".
                    print("case occupée, fais un autre choix")
            
            #Sinon
            else:
                if curPlayerID == 1:
                    #Assigner le symbole du joueur aux coordonnées choixX, choixY dans tab.
                    tab[choixX][choixY] = playerSymbole[curPlayerID]
                #Incrémenter actionTurn de 1
                actionTurn = actionTurn + 1
                #Définir check égale à True
                check = True

        #Pour chaque element de tab
        for i in tab:
            #On imprime la ligne du tableau
            print(i)

        #On stock temporairement le symbole du joueur actuel dans la variable cur.
        cur = playerSymbole[curPlayerID]
        #Si l'action du joueur est un action qui lui fait gagner la partie.
        if (tab[0][0] == cur and tab[0][1] == cur and tab[0][2] == cur) or (tab[1][0] == cur and tab[1][1] == cur and tab[1][2] == cur) or (tab[2][0] == cur and tab[2][1] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][0] == cur and tab[2][0] == cur) or (tab[0][1] == cur and tab[1][1] == cur and tab[2][1] == cur) or (tab[0][2] == cur and tab[1][2] == cur and tab[2][2] == cur) or (tab[0][0] == cur and tab[1][1] == cur and tab[2][2] == cur) or (tab[0][2] == cur and tab[1][1] == cur and tab[2][0] == cur):
            #Alors on ecrit quel joueur à gagné
            print(f"{curPlayer[curPlayerID]} a gagné")
            #Afficher un retour au menu
            # print("retour au menu")
            # print("retour au menu.")
            # print("retour au menu..")
            # print("retour au menu...")
            # morpionMenu()
        #Sinon si action égale à 8
        elif actionTurn == 8:
            #Afficher "Pas de gagnant"
            print("Pas de gagant")
            return
            # #Afficher un retour au menu
            # print("retour au menu")
            # print("retour au menu.")
            # print("retour au menu..")
            # print("retour au menu...")
            # morpionMenu()

        
        curPlayerID = curPlayerID * -1
        # #Si tab[choixX][choixY] est égal au symbole du joueur.
        # if tab[choixX][choixY] == playerSymbole[curPlayerID]:
        #     #Alors on change l'ID de curPlayerID en multipliant la variable par -1.
        #     print("bloup")

playerVesusTerminatorGame()