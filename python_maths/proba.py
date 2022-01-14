import time 
from math import*
from random import randint

liste=["0","1","2","3","4","5","6","7","8","9"]

# Fonction qui génére des mots de passe
def password(longueur_mot_de_passe, quantité_mot_de_passe):
    liste_pwd=[]
    for i in range(quantité_mot_de_passe):
        mot_de_passe=""
        for i in range(longueur_mot_de_passe):
            mot_de_passe=mot_de_passe+str(randint(0,9))
        liste_pwd.append(mot_de_passe)
    return liste_pwd

#print(password(4,2))

print("----------------------------")
# Trouve les occurences dans une liste, prend en argument une chaine de caractère et une liste
def occurence(chaine,liste):
    cp=0
    if chaine in liste:
        print(chaine," est dans la liste")
    print("----------------------------")
    for i in liste:
        if i==chaine :
            cp+=1 
    return cp 


#print ("la liste des mots de passe", liste_mot_de_passe)



start=time.time()
liste_mot =password(2,10000000)
print("Fréquence observée = ", occurence("26",liste_mot)/10000000)
print("----------------------------")
end=time.time()
duration=end-start
print ("Temps d'execution =", duration, " secondes" )


