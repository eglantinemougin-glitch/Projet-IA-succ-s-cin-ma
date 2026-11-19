# Programme pour sortir les informations des colonnes choisis 

import numpy as np
# dictionnaire contenant les informations associer à leurs numéro de colonne dans le  fichier 
dico = {#"Titre" : 0,                   #A 
        "Date de production jour" : 1, #B
        "Genre" : 2,                   #C
        "Durée" : 3,                   #D
        #"Directeur" : 4,               #E
        "Date de naissance" : 6,       #G
        "Avis sur 10" :8,              #I
        "Budget" : 11,                 #L
        "Gain domestic" : 12,          #M
        "Gain mondial" : 13            #N
        }

#"Date de décès" : 7,           #F

# dictionnaire contenant les données
dico_données = {} 

# Ouverture doc excel
fichier = 'movie_statistic_dataset_modif.csv'

texte = open(fichier, mode='r', newline='', encoding='utf-8', errors="ignore")
ligne_des_titres = texte.readline()
données = texte.readlines()
texte.close()

# Séparation de chaque ligne du fichier en une liste contennant les informations de la ligne
for l in range (len(données)):
    données[l] = données[l].strip().split(";")

    
# Initialisation loop principale
#print(données[0])
bug_line = [] # ajout les lignes où un problème a été trouvé
liste_genre = [] # liste de tout les genres trouver dans le fichier
date_bis = ["Date de production jour","Date de production mois","Date de production année"] # 

# Création des clés "Date de production mois" et "Date de production année" associer à une liste vide
# dans le dictionnaire contenant les données 
dico_données["Date de production mois"] = [] 
dico_données["Date de production année"] = []

for l in range (len(données)):
    Genres = données[l][dico['Genre']].split(",")
    for i in range (len(Genres)):
        if Genres[i] not in liste_genre and Genres[i] != '\\N':
            liste_genre.append(Genres[i])

# Début loop principale
for key in dico.keys(): # parcours toutes les colonnes
    val = dico[key]
    dico_données[key] = []

    for l in range (len(données)): # parcours chaque case 

        # Cas de la date de production
        if key == "Date de production jour":
            date = données[l][val].split("/")
            #print(date)
            if len(date) == 3 :
                for i in range (3):
                    try :
                        int(date[i])  
                    except :
                        bug_line.append(l)
                    else :
                        dico_données[date_bis[i]].append(int(date[i]))
            else :
                bug_line.append(l)

        # Pour le moment ne sert à rien (il faudrait compiler tout les genres en une chaine de caractère ou chiffre)
        if key == "Genre" : # ne rentre pas dans dico_données !
            Genres = données[l][val].split(",")
            
            Compilation_genre = [[0 for j in range(len(liste_genre))] for i in range(len(liste_genre))]

            for y in range (len(liste_genre)):
                #print(len(liste_genre))
                for i in range (len(Genres)):
                    if Genres[i] == liste_genre[y] :
                        Compilation_genre[y] = 1
                        #print(Genres[i],liste_genre[y])
                    else :
                        Compilation_genre[y] = 0
            #print(len(Compilation_genre),Compilation_genre,' : ',Genres)

            genre = ''
            for i in range (len(Compilation_genre)):
                genre += str(Compilation_genre[i])
            dico_données['Genre'].append(genre)

        # cas date de naissace du réalisateur
        if key == "Date de naissance" :
            Date_naissance = données[l][val]
            #print(Date_naissance)
            Date_naissance_list = []
            try :
                int(Date_naissance)
            except :
                dico_données["Date de naissance"].append(None)
            else :
                dico_données["Date de naissance"].append(int(Date_naissance))
                    

        if key != "Date de production jour" and key != "Genre" and key!= "Date de naissance" :
            try :
                int(données[l][val])
            except:
                try :
                    float(données[l][val])
                except :
                    dico_données[key].append(données[l][val])
                else :
                    dico_données[key].append(float(données[l][val]))
            else :
                dico_données[key].append(int(données[l][val]))
    
    # Turn into array    
    if key != "Date de production jour" :
        dico_données[key] = np.array(dico_données[key]) # Pour le moment ne marche pas a cause des liste dans Date de production et genre
    
    if key == "Date de production jour" :
        for i in range (len(date_bis)):
            dico_données[date_bis[i]] = np.array(dico_données[date_bis[i]])
 
# Création d'un dico genre associant le genre à un chiffre
dico_genre = {}
for l in range (len(liste_genre)):
    dico_genre[liste_genre[l]] = l



    
#print()
#print("---------------------------------------------------")
#print()
    
#print(dico_données)
for key in dico_données.keys():
    print(key,dico_données[key]) # print nombre de valeur par clé

# vérification que "Date de production jour" contient moins de 3 caractères 
for l in range(len(dico_données["Date de production jour"])):
    if len(str(dico_données["Date de production jour"][l])) > 3 :
        bug_line.append(dico_données["Date de production jour"][l])    
   
    
#print("\n dico_donnée (Date de naissance):\n",dico_données["Date de naissance"])

print("\n liste genre :\n",liste_genre)
#print("---------------------------------------------------")
#print("\n dico_genre :\n",dico_genre)
#print("---------------------------------------------------")
#print("\n ligne bug :\n",bug_line)

#for key in dico_données.keys() :
#    print(key," : ",dico_données[key])