'''import time

start =time.time()

k=556
for i in range(100000000):
    somme=i+1
    if (somme%2==0):
        somme=somme**2
    else :
        somme=somme-i**2

end=time.time()
duration =end-start
print("resultat = ", somme ,"  ------   temps = " , duration,"secondes")


liste =["mots", "voyelles","lettres","choix"]
dict={mot:mot[-1] for mot in liste}

print(dict) '''


def lettre_z(mot):
    if "z" in mot :
        return True
    else :
        return False


def lettre_z2(mot):
    bool =False
    for lettre in mot :
        if lettre =="z":
            bool=True
    return bool


print(lettre_z("bonzjour"))


print(lettre_z2("bonjour"))
