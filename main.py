# Import all the modules needed
import time, subprocess, sys, csv, random, string

# List all the variables
menu = True
option = 0
arraynumber1 = 0
arraynumber2 = 0

# Menu
while menu:
    option = input('''[1] Skapa Användare
[2] Ta bort användare
[3] Stäng programmet
Val: ''')
    if option == "1" or option == "2":
        if option == "1":
            print("skapa användare")
            with open('Users.csv') as CSVfile:
                readCSV = csv.reader(CSVfile, delimiter=',')
                names = []
                surnames = []
                for row in readCSV:
                    name = row[1]
                    surname = row[2]
                    names.append(name)
                    surnames.append(surname)
                arraynumber1 = int(input("Start From Row: "))
                arraynumber2 = int(input("Stop at Row: "))
                while arraynumber1 <= arraynumber2:
                    print(names[arraynumber1], surnames[arraynumber1])
                    arraynumber1 += 1
                
        else:
            print("ta bort användare")

    elif option == "3":
        print("Stänger av..")
        time.sleep(0.5)
        menu = False
    else:
        print("Välj ett av de tre alternativen")
        

chars = "abcdefghijklmnopqrstuvwxyz"
chars1 = "1234567890"
chars2 = "!#%&/()="
password = ""
for c in range(2):
    password += random.choice(chars)
    password += random.choice(chars.upper())
    password += random.choice(chars1)
    password += random.choice(chars2)
password = ''.join(random.sample(password, len(password)))
print(password)
print(len(password))