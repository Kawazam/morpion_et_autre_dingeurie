#DEBUT

#On admet la fonction input() qui renvoie la valeur donné par l'utilisateur.

#Definir une fonction morpion() qui lance une partie de morpion entre deux joueurs.
    #Definir un tableau de 3 x 3 avec des symboles vide.
    #Definir un dictionaire dans lequel on stock le nom des joueurs
    #Definir une variable à laquelle on assigne l'ID du joueur actuel
    #Definir un dictionaire dans lequel on stock le symbole de chaque joueur en fonction de son ID
    #Tant que True
        #Ecrire le nom du joueur dont c'est le tour en fonction de l'ID du joueur actuel dans curPlayer 
        #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
        #Si choixX ne rentre pas dans le tableau
        #Afficher un message d'erreur
            #Assigner à la variable choixX le retour de la variable input("coordonné x : ") sous forme d'entier
        #Assigner à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
        #Si choixY ne rentre pas dans le tableau
        #Afficher un message d'erreur
            #Assigner à la variable choixX le retour de la variable input("coordonné y : ") sous forme d'entier
        #Si tab[choixX][choixY] est different de "_".
            #Alors on ecrit "case occupée, fais un autre choix".
        #Sinon
            #Assigner le symbole du joueur aux coordonnées choixX, choixY dans tab.
        #Pour chaque element de tab
            #On imrpime la ligne du tableau
        #On stock temporairement le symbole du joueur actuel dans la variable cur.
        #Si l'action du joueur est un action qui lui fait gagner la partie.
            #Alors on ecrit quel joueur à gagné
            #Puis on force la sortie de la boucle infinie avec un break        
        #Si tab[choixX][choixY] est égal au symbole du joueur.
            #Alors on change l'ID de curPlayerID en multipliant la variable par -1.

#Executer la fonction morpion()

#FIN