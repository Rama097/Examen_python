tab=[]
def saisi_tab():
    nom=str (input("Nom:"))
    prenom=str (input("Prenom:"))
    numero_rue=int (input("Numero de la rue:"))
    numero_tel=int (input("Numero de telephone:"))
    nom_rue=str (input("Nom de la rue:"))
    code_postal=int(input("Code postal:"))
    ville=str (input("Ville:"))

    informations={
        "Nom":nom,
        "Prenom":prenom,
        "Numero_Rue":numero_rue,
        "Numero_Tel":numero_tel,
        "Nom_Rue":nom_rue,
        "Code_Postal":code_postal,
        "Ville":ville
    }
    tab.append(informations)

def critere_recherche(): 
     print("1. Nom")
     print("2. Prenom")
     print("3. Numero_Rue")
     print("4. Numero_Tel")
     print("5. Nom_Rue")
     print("6. Code_Postal")
     print("7. ville")
     choix = input("Veuillez donner le critere à rechercher")
     if choix=="1":
          critere="Nom"
     elif choix=="2":   
          critere="Prenom"  
     elif choix=="3":   
          critere="Numero_Rue"
     elif choix=="4":   
          critere="Num_Tel"
     elif choix=="5":   
          critere="Nom_Rue"
     elif choix=="6":   
          critere="Code_Postal"
     elif choix=="7":   
          critere="Ville" 

     else:
          print("Veuillez faire un bon choix")
          return None                 


def affiche_tab():
     if tab:
          for informations in tab:
               print(informations) 
     else:
          print("Le tableau est vide")                  
    

