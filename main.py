### Imports et définition des variables globales
"""Modifie le nombre max d'itérations
qu'on peut faire en appel récursif dans Python"""
import sys
sys.setrecursionlimit(20000)


#### Fonctions secondaires

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de 
    caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    n=len(s)
    c=[s[0]]
    o=[1]
    k=1
    t=[]
    while k<n:
        if s[k]==s[k-1]:
            o[-1]+=1
            k+=1
        else:
            c+=s[k]
            o.append(1)
            k+=1
    t=list(zip(c,o))
    return t


def artcode_r(s,c=0):
    """retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)"""
    # votre code ici

    # cas de base
    if len(s)==0:
        return [('',1)]
    if len(s)==1:
        return [(s[0],c+1)]
    if s[0]==s[1]:
        return artcode_r(s[1:],c+1)
    if c!=0:
        return [(s[0],c+1)]+artcode_r(s[1:])
    return [(s[0],c+1)]+artcode_r(s[1:])
    # recherche nombre de caractères identiques au premier
    # appel récursif (cas où le terme est le même que le suivant,
    # cas où ce n'est pas le même et le terme précédent est le même, cas autre)
    #on retourne une liste qui contient le terme courant et ses occurences
    # et on ajoute la liste créee par la récurrence sur le terme suivant

#### Fonction principale


def main():
    """
    Appel protégé de la fonction
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))


if __name__ == "__main__":
    main()
