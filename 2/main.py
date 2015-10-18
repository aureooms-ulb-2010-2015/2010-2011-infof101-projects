# -*- coding: utf-8 -*-

"""
projet2.py

réalisé par OOMS Aurélien
[Groupe 3]
"""

from random import randint


def creer_labyrinthe(n,m):
    
    if m > n-2:
        matrice='Impossible de créer un tel labyrinthe car le nombre de murs maximums est trop élevé!!!'

        #au cas où trop de murs
        
    else:
        matrice=[n*[1]]#initialise la matrice
        
        for k in range(n-1):
            matrice.append(n*[1])
            
            """
            Ne peut pas la créer avec n*[n*[1]] car
            il considère alors les éléments de même
            indice comme identiques, il y a alors un
            soucis lors de modifications au sein de
            la matrice.
            """
            
            #matrice de taille n crée
            
        for x in range(1,n-1):
            
            for y in range(1,n-1):
                matrice[x][y]=0
                
            #rempli l'intérieur de la matrice de 0
            #(donc tout sauf les bords)
                
        for murs in range(m):
            
            for i in range(1,n-1):
                j=randint(1,n-2)
                matrice[i][j]=1

            #sur chaque ligne, recalcule m fois
            #une colonne j dans laquelle mettre
            #un 1 (donc de 1 à m murs par ligne)
                
        for i in range(0,n):
            
            for j in range(0,n):
                
                if matrice[i][j]==0:
                    matrice[i][j]=' '
                    
                else:
                    matrice[i][j]='x'
                    
            #remplace les 0 par des espaces et
            #les 1 par des x

            """
            La matrice créée est une liste de longueur n
            comprenant n sous-listes de longueur n
            contenant des x et des espaces.
            """
            
    return matrice


def print_labyrinthe(l):
    
    if not isinstance(l,list):
        print l

        #si trop de murs, retourne la phrase d'erreur
        
    else:
        labyrinthe=''
    
        for s in range(len(l)):            
                          
            labyrinthe=labyrinthe+'\n'
            
            for t in range(len(l)):
                
                labyrinthe=labyrinthe+l[s][t]+' '
        
        print labyrinthe


n=int(raw_input('Dimension n du labyrinthe:\n'))

m=int(raw_input('Nombre m de murs par ligne(hors bords):\n'))

l=creer_labyrinthe(n,m)

if isinstance(l,list):
    print 'Voici un tel labyrinthe:'
    print_labyrinthe(l)
    
else:
    print_labyrinthe(l)#plus "logique" quand trop de murs
