def Saisie():
    t=[]
    nom=str (input("Entrer le nom de la personne :"))
    annee=int (input("Entrer l'annee:"))
    temps=int(input("Donner le temps en second:"))

    personne={
        "Nom":nom,
        "Annee de naissance":annee,
        "Temps":temps
        
    }
    t.append(personne)
    return t
liste_personnes=Saisie()
print("Les informations des personnes saisie:",liste_personnes)


def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        nom = personne["Nom"]
        annee = personne["Année de naissance"]
        
        print("Personne :", nom)
        
        annee_max=10000
        annee_min=-10000

        annee_voyage = int(input("En quelle annee souhaitez-vous voyagez? "))
        if annee_voyage < annee_min or annee_voyage > annee_max:
               
        
