#Voici un petit pierre, feuille, ciseaux. Créé le 21/11/2021

import numpy as np  #on importe la blibliothèque qui nous permet de faire un choix aléatoire pour l'ordianateur

choix=['pierre', 'feuille', 'ciseaux'] #on initialise une variable listant les différents choix possibles pour l'ordinateur
gg='Bravo, vous avez gagnez' # à afficher si le joueur gagne
nope="Désolé, c'est perdu. ;)" # à afficher si le joueur perd
eql="Egalité, on recommence ?" # à affiher en cas d'égalité
nbtour=int(input("Nombre de tour")) #on demande au joueur le nombre de tour qu'il voudrait faire
ppc=0 #on initialise la variable des points du joueur
pj=0 #on initialise la variable des point de l'ordinateur
for k in range(0,nbtour): #boule for qui tournera jusqu'à que nbtour soient effectués
  cj=input("pierre, feuille, ou ciseaux ?") #on demande au joueur qu'est-ce qu'il veut jouer

  if cj=='pierre': # si le joueur joue pierre
    if np.random.choice(choix)=='pierre': #si l'ordinateur joue pierre
      print(eql) # afficher eql (phrase d'égalité)
    elif np.random.choice(choix)=='feuille': #sinon, si l'ordinateur joue la feuille
      print(nope) #afficher nope (phrase de défaite)
      ppc+=1 # ajouter 1 aux points de l'ordinateur
    else: #sinon
      print(gg) #afficher gg (phrase de victoire)
      pj+=1 #ajouter 1  aux points du joueur

  elif cj=='feuille':
    if np.random.choice(choix)=='feuille':
      print(eql)
    elif np.random.choice(choix)=='ciseaux':
      print(nope)
      ppc+=1
    else:
      print(gg)
      pj+=1

  elif cj=='ciseaux':
    if np.random.choice(choix)=='ciseaux':
      print(eql)
    elif np.random.choice(choix)=='pierre':
      print(nope)
      ppc+=1
    else:
      print(gg)
      pj+=1

  else:
    pass

if pj==ppc: #si le joueur et l'ordinateur ont le même nombre de point
  print(f"Vous avez une égalité de point(s) de {pj}.") #afficher  égalité et nombre de point (pj)
elif pj>ppc:
  print(f"Vous avez {pj} point(s) et la machine a {ppc} point(s), bravo !")
else:
  print(f"Vous avez {pj} point(s) et la machine a {ppc} point(s), dommage !")
