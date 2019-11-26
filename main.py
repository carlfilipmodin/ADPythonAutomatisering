# Import all the modules needed
import time, subprocess

# List all the variables
menu = True
option = 0

# Menu
while menu:
    option = input('''[1] Skapa Användare
[2] Ta bort användare
[3] Stäng programmet
Val: ''')
    if option == "1" or option == "2":
        if option == "1":
            print("skapa användare")
        else:
            print("ta bort användare")
    elif option == "3":
        print("Stänger av..")
        time.sleep(0.5)
        menu = False
    else:
        print("Välj ett av de tre alternativen")
        