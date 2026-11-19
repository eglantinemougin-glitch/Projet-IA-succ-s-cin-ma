from sklearn import linear_model
from Code_Recup_Donnee_Projet_IA import dico_données

Features = np.array([dico_données['Durée'], dico_données['Budget'], dico_données['Date de naissance'],
                     dico_données['Date de production jour']]).T
Target = np.array(dico_données['Gain mondial'])

dico = {"Titre" : 0,                   #A 
        "Date de production jour" : 1, #B
        "Genre" : 2,                   #C
        "Durée" : 3,                   #D
        "Directeur" : 4,               #E
        "Date de naissance" : 6,       #G
        "Budget" : 11,                 #L
        "Gain domestic" : 12,          #M
        "Gain mondial" : 13            #N
        }

print("Forme de Features :", Features.shape)
print("Forme de Target :", Target.shape)