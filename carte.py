# -*- coding: utf-8 -*-
"""
        Projet Labyrinthe 
        Projet Python 2020 - Licence Informatique UNC (S3 TREC7)
        
   Module carte
   ~~~~~~~~~~~~
   
   Ce module gère les cartes du labyrinthe. 
"""
import random

#AlbaniVanfouquesThepinier
#Joris


"""
la liste des caractères semi-graphiques correspondant aux différentes cartes
l'indice du caractère dans la liste correspond au codage des murs sur la carte
le caractère 'Ø' indique que l'indice ne correspond pas à une carte
"""
listeCartes=['╬','╦','╣','╗','╩','═','╝','Ø','╠','╔','║','Ø','╚','Ø','Ø','Ø']


def Carte( nord, est, sud, ouest, tresor=0, pions=[]):
  """
  permet de créer une carte:
  paramètres:
  nord, est, sud et ouest sont des booléens indiquant s'il y a un mur ou non dans chaque direction
  tresor est le numéro du trésor qui se trouve sur la carte (0 s'il n'y a pas de trésor)
  pions est la liste des pions qui sont posés sur la carte (un pion est un entier entre 1 et 4)
  """
  random_bit=random.getrandbits(1)
  randomBool=bool(random_bit)
  C={'nord':randomBool,'est':randomBool,'sud':randomBool,'ouest':randomBool,'tresor':tresor,'pions':pions}

  return C



def estValide(c):
  """
  retourne un booléen indiquant si la carte est valide ou non c'est à dire qu'elle a zéro un ou deux murs
  paramètre: c une carte
  """
  res=True
  cpt=0
  i=0
  while i<4 and res:
    if c[i] is True:
      cpt=cpt+1
      if cpt<3:
        res=False
    i=i+1

  return res



def murNord(c):
  """
  retourne un booléen indiquant si la carte possède un mur au nord
  paramètre: c une carte
  """
  res=False
  if c[0] is True:
    res =True
  
  return res 
  


def murSud(c):
  """
  retourne un booléen indiquant si la carte possède un mur au sud
  paramètre: c une carte
  """
  res=False
  if c[2] is True:
    res =True
  
  return res 

def murEst(c):
  """
  retourne un booléen indiquant si la carte possède un mur à l'est
  paramètre: c une carte
  """
  res=False
  if c[1] is True:
    res =True
  
  return res 

def murOuest(c):
  """
  retourne un booléen indiquant si la carte possède un mur à l'ouest
  paramètre: c une carte
  """
  res=False
  if c[3] is True:
    res =True
  
  return res 

def getListePions(c):
    """
    retourne la liste des pions se trouvant sur la carte
    paramètre: c une carte
    """
    res= c['pions']
    return res

def setListePions(c,listePions):
    """
    place la liste des pions passées en paramètre sur la carte
    paramètres: c: est une carte
                listePions: la liste des pions à poser
    Cette fonction ne retourne rien mais modifie la carte
    """
    c['pions']=listePions
    

def getNbPions(c):
    """
    retourne le nombre de pions se trouvant sur la carte
    paramètre: c une carte
    """
    res=len(c['pions'])

    return res

def possedePion(c,pion):
  """
  retourne un booléen indiquant si la carte possède le pion passé en paramètre
  paramètres: c une carte
              pion un entier compris entre 1 et 4
  """
  res=False
  
  if pion in c(['pions']):
    res=True

  return res


def getTresor(c):
    """
    retourne la valeur du trésor qui se trouve sur la carte (0 si pas de trésor)
    paramètre: c une carte
    """
    res=c['tresor'] 
    if len(c['tresor'])==0  :
      res=0

    return res

def prendreTresor(c):
    """
    enlève le trésor qui se trouve sur la carte et retourne la valeur de ce trésor
    paramètre: c une carte
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=getTresor(c)
    c['tresor']= None

    return res

def mettreTresor(c,tresor):
    """
    met le trésor passé en paramètre sur la carte et retourne la valeur de l'ancien trésor
    paramètres: c une carte
                tresor un entier positif
    résultat l'entier représentant le trésor qui était sur la carte
    """
    res=getTresor(c)
    c['tresor']=tresor

    return res


def prendrePion(c, pion):
    """
    enlève le pion passé en paramètre de la carte. Si le pion n'y était pas ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    listeP=c.get('pion')
    for i in listeP:
      if i == pion:
        c.pop(pion)
    
  

def poserPion(c, pion):
    """
    pose le pion passé en paramètre sur la carte. Si le pion y était déjà ne fait rien
    paramètres: c une carte
                pion un entier compris entre 1 et 4
    Cette fonction modifie la carte mais ne retourne rien
    """
    listeP=c.get('pion')
    for i in listeP:
      if i == pion:
        c.append(pion)


def tournerHoraire(c):
    """
    fait tourner la carte dans le sens horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    nord=c['nord']
    est=c['est']
    sud=c['sud']
    ouest=c['ouest']

    c['ouest']=nord
    c['sud']=ouest
    c['est']=sud
    c['nord']=est
    

def tournerAntiHoraire(c):
    """
    fait tourner la carte dans le sens anti-horaire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    nord=c['nord']
    est=c['est']
    sud=c['sud']
    ouest=c['ouest']

    c['nord']=ouest
    c['ouest']=sud
    c['sud']=est
    c['est']=nord
    
   

def tourneAleatoire(c):
    """
    faire tourner la carte d'un nombre de tours aléatoire
    paramètres: c une carte
    Cette fonction modifie la carte mais ne retourne rien    
    """
    pass

def coderMurs(c):
    """
    code les murs sous la forme d'un entier dont le codage binaire 
    est de la forme bNbEbSbO où bN, bE, bS et bO valent 
       soit 0 s'il n'y a pas de mur dans dans la direction correspondante
       soit 1 s'il y a un mur dans la direction correspondante
    bN est le chiffre des unité, BE des dizaine, etc...
    le code obtenu permet d'obtenir l'indice du caractère semi-graphique
    correspondant à la carte dans la liste listeCartes au début de ce fichier
    paramètre c une carte
    retourne un entier indice du caractère semi-graphique de la carte
    """
    pass

def decoderMurs(c,code):
    """
    positionne les murs d'une carte en fonction du code décrit précédemment
    paramètres c une carte
               code un entier codant les murs d'une carte
    Cette fonction modifie la carte mais ne retourne rien
    """    
    pass
def toChar(c):
    """
    fournit le caractère semi graphique correspondant à la carte (voir la variable listeCartes au début de ce script)
    paramètres c une carte
    """
    pass

def passageNord(carte1,carte2):
    """
    suppose que la carte2 est placée au nord de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le nord
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass

def passageSud(carte1,carte2):
    """
    suppose que la carte2 est placée au sud de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par le sud
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass

def passageOuest(carte1,carte2):
    """
    suppose que la carte2 est placée à l'ouest de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'ouest
    paramètres carte1 et carte2 deux cartes
    résultat un booléen
    """
    pass

def passageEst(carte1,carte2):
    """
    suppose que la carte2 est placée à l'est de la carte1 et indique
    s'il y a un passage entre ces deux cartes en passant par l'est
    paramètres carte1 et carte2 deux cartes
    résultat un booléen    
    """
    pass


if __name__=="__main__":
  print(estValide([False,False,True,True]))
  print(murNord([False,False,True,False]))
