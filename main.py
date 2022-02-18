import string
from sys import * 
import os
from time import sleep
from pathlib import *
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n♦ Bienvenue dans le pack script de ©ROSCA. \n•[0] Comment setup les scripts dans un projet py :).\n •[1] setup script par défaut. \n •[2] setup script tkinder \n •[4] Quitter :'( \n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
H = int(input("Votre choix est:"))
print("Vous avez choisi le script:",H)
print("Merci d'attendre le chargement du script:",H,"...")
sleep(2)

if H == 0:
    print("♦Comment setup mes scripts ?")

if H == 1:
    print("♦Bienvenue dans l'installateur du pack N°1:")
    Path_s = input("Entrez le chemin d'acces de votre:")
    
    file_name = "main.py"

    acces_file = os.path.join(Path_s, file_name)

    file1 = open(acces_file, "w")
    file1.write("print(\"caca\")")
    file1.close()
    
  

if H == 2:
    print("♦Comment setup mes scripts ?")
if H == 9:
    print("Fermeture de Pack script.")
    sleep(1)
    exit()
if H > 4:
    print("♦Aucun pack-script trouver.♦")
    exit()