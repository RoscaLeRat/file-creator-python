import string
import sys
from time import sleep
from pathlib import *
print("♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦\n♦ Bienvenue dans le pack script de ©ROSCA. \n•[0] Comment setup les scripts dans un projet py :).\n •[1] setup script par défaut. \n •[2] setup script tkinder \n •[9] Quitter :'( \n♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦♦")
H = int(input("Votre choix est:"))
print("Vous avez choisi le script:",H)
print("Merci d'attendre le chargement du script:",H,"...")
sleep(2)

if H == 0:
    print("♦Comment setup mes scripts ?")
#faire le truc chiant pour créer un script dans un autre script (file-creator.py)
if H == 1:
    print("♦Bienvenue dans l'installateur du pack N°1:")
    Path_s = input("Entre le chemin d'acces de votre:")
    myfile = Path(Path_s)
    file = open(Path_s,'main.py','w+')

    myfile.touch(exist_ok=True)
    print(myfile)

if H == 2:
    print("♦Comment setup mes scripts ?")
if H == 9:
    print("Fermeture de Pack script.")
    sleep(1)
    exit()
