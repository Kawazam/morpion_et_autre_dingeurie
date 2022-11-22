#On admet la fonction input() qui renvoie la valeur donné par l'utilisateur.
from random import randint
import os
clear = lambda: os.system('cls')



#-----------------------MORPION--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Definir une fonction morpionGame() qui lance une partie de morpion entre deux joueurs.
def morpionClassic():
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
    #Définir la variable actionTurn à 0
    actionTurn = 0

    #Tant que True
    while True:
        #Initialiser check à False
        check = False
        #Tant que check est False
        while not check:
            #Ecrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 
            print(f"{curPlayer[curPlayerID]}, c'est à toi !")

            #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
            choixX = int(input("coordonné x : "))
            #Si choixX ne rentre pas dans le tableau
            while choixX < 0 or choixX > 2:
            #Afficher un message d'erreur
                print("Choix invalide")
                #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
                choixX = int(input("coordonné x : "))
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
            print("retour au menu")
            print("retour au menu.")
            print("retour au menu..")
            print("retour au menu...")
            morpionMenu()
        #Sinon si action égale à 9
        elif actionTurn == 9:
            #Afficher "Pas de gagnant"
            print("Pas de gagant")
            print("retour au menu")
            print("retour au menu.")
            print("retour au menu..")
            print("retour au menu...")
            morpionMenu()

        
        #Si tab[choixX][choixY] est égal au symbole du joueur.
        if tab[choixX][choixY] == playerSymbole[curPlayerID]:
            #Alors on change l'ID de curPlayerID en multipliant la variable par -1.
            curPlayerID = curPlayerID * -1


#-----------------------PLAYER VS CPU--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Définir une fonction playerVersusCpuGame() qui permet de jouer conter l'ordinateur
def playerVesusCpuGame():
    #Definir un tableau de 3 x 3 avec des symboles vide.
    tab = [ ["_" for i in range(3)] for i in range(3) ]
    #Definir un dictionaire dans lequel on stock le nom des joueurs
    curPlayer = {
        1: "Joueur 1",
        -1: "CPU"
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

    #Tant que True
    while True:
        #Initialiser check à False
        check = False
        #Tant que check est False
        while not check:
            #Si le joueur est cpu
            if curPlayerID == -1:
                print("Au tour du CPU")
                #Assigner à la variable choixX le retour de l'execution de la variable randint(0, 2)
                choixX = randint(0, 2)
                #Assigner à la variable choixY le retour de l'execution de la variable randint(0, 2)
                choixY = randint(0, 2)
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
            if tab[choixX][choixY] != "_":
                #Si curPlayerID égale à 1
                if curPlayerID == -1:
                    #On ecrit "case occupée, fais un autre choix".
                    print("case occupée, fais un autre choix")
            
            #Sinon
            else:
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
            print("retour au menu")
            print("retour au menu.")
            print("retour au menu..")
            print("retour au menu...")
            morpionMenu()
        #Sinon si action égale à 9
        elif actionTurn == 9:
            #Afficher "Pas de gagnant"
            print("Pas de gagant")
            #Afficher un retour au menu
            print("retour au menu")
            print("retour au menu.")
            print("retour au menu..")
            print("retour au menu...")
            morpionMenu()

        
        #Si tab[choixX][choixY] est égal au symbole du joueur.
        if tab[choixX][choixY] == playerSymbole[curPlayerID]:
            #Alors on change l'ID de curPlayerID en multipliant la variable par -1.
            curPlayerID = curPlayerID * -1


#-----------------------PLAYER VS IA--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Définir une fonction playerVersusJarvisGame() qui permet de jouer contre une intelligence artificiel qui ne peux que gagner ou égaliser


#-----------------------PLAYER VS TERMINATOR-------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    #Afficher une primière fois la grille
    for i in tab:
        print(i)

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
                        if tab[0][2] == "_":
                            #Jouer en 0-2
                            tab[0][2] = "X"
                        #Si le joueur joue en 0-2
                        elif tab[2][1] == "_":
                            #Jouer en 2-1
                            tab[2][1] = "X"
                        #Sinon
                        else:
                            #placé le symbole du joueur à la position 0-1
                            tab[0][1] = "X"
                    #Sinon si il y a une situation de victoire assuré au positions 1-1  2-2  0-2
                    elif tab[1][1] == "X" and tab[2][2] == "X" and tab[0][2] == "X":
                        #Si le joueur joue en 1-2
                        if tab[2][0] == "_":
                            #Jouer en 2-0
                            tab[2][0] = "X"
                        #Si le joueur joue en 2-0
                        elif tab[1][2] == "_":
                            #Jouer en 1-2
                            tab[1][2] = "X"
                        #Sinon
                        else:
                            #placé le symbole du joueur à la position 2-0
                            tab [1][0] = "X"
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
            print("retour au menu")
            print("retour au menu.")
            print("retour au menu..")
            print("retour au menu...")
            morpionMenu()
        #Sinon si action égale à 8
        elif actionTurn == 8:
            #Afficher "Pas de gagnant"
            print("Pas de gagant")
            # #Afficher un retour au menu
            print("retour au menu")
            print("retour au menu.")
            print("retour au menu..")
            print("retour au menu...")
            morpionMenu()

        #Définir curPlayerID à sa valeur multiplié par -1
        curPlayerID = curPlayerID * -1


#-----------------------MENU--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Définir la fonction morpionMenu() qui présente le menu du jeux et les différentes option
def morpionMenu():
    #Initialiser la variable gameMode à None
    gameMode = None
    #Appeler print("--------- MENU SHIFUMI ----")
    print("--------- MENU SHIFUMI ----")
    #Appeler print("0 - Quitter")
    print("0 - Quitter")
    #Appeler print("1 - Mode Joueur vs Joueur")
    print("1 - Mode Joueur vs Joueur")
    #Appeler print("2 - Mode Joueur vs CPU")
    print("2 - Mode Joueur vs CPU")
    #Appeler print("3 - Mode contre Terminator")
    print("3 - Mode contre Terminator")
    #Appeler print("---------------------------")
    print("---------------------------")
    #Définir la variable gameMode avec comme valeur le retour de l'execution de la fonction float(input("Mode de jeu : "))
    gameMode = float(input("Mode de jeu : "))

    #Si gameMode égale à 0
    if gameMode == 0:
        #Afficher un message qui éteind le jeu
        print(" ")
        print("arrêt du jeu")
        print("arrêt du jeu.")
        print("arrêt du jeu..")
        print("arrêt du jeu...")
        #retourner
        return
    #Sinon si gameMode égale à 1
    elif gameMode == 1:
        #Exécuter la fonction morpionClassic   
        morpionClassic()
    #Sinon si gameMode égale à 2
    elif gameMode == 2:
        #Exécuter la fonction playerVersusCpuGame   
        playerVesusCpuGame()
    #Sinon si gameMode égale à 3
    elif gameMode == 3:
        #Exécuter la fonction playerVersusTerminatorGame
        playerVesusTerminatorGame()


#Executer la fonction morpionMenu
clear()
morpionMenu()