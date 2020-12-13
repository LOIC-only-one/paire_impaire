import os
import time, sys
os.system('cls')

jeu_lance = True

def loading():
    for i in range(0, 10):
        time.sleep(0.1)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "/10 Calcul en cour...")
        sys.stdout.flush()
    print()




print('''\u001b[32m         ______          _      _    ___  ___      _   _     
         | ___ \        (_)    | |   |  \/  |     | | | |    
         | |_/ / __ ___  _  ___| |_  | .  . | __ _| |_| |__  
         |  __/ '__/ _ \| |/ _ \ __| | |\/| |/ _` | __| '_ \ 
         | |  | | | (_) | |  __/ |_  | |  | | (_| | |_| | | |
         \_|  |_|  \___/| |\___|\__| \_|  |_/\__,_|\__|_| |_|
                        / |                                  
                       |__/                                   \u001b[30m''')
print("")
print("\u001b[32mTitre : Nombre Paire et Impaire.\u001b[30m")
print("\u001b[32mLoïc Maurer 2de1\u001b[30m")
print("")


while jeu_lance:
	n = input("\u001b[32m\u001b[4m\u001b[33mQuelle est votre valeur ?\u001b[30m\u001b[m\u001b[33m ")
	n = int(n)
	r = n % 2


	if( r == 0):
		loading()
		print("\u001b[34mTu as choisie une valeur paire.\u001b[30m")
		print()

	else:
		loading()
		print("\u001b[31mTu as choisie une valeur impaire.\u001b[30m")
		print()

input()
