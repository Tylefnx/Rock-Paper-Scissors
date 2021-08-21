from random import randrange
import os
wdtgs = ["rock", "scissors", "paper"]
while (1):
    print("""
##################
# Rock = 1       #\n
# Paper = 2      #\n 
# Scissors = 3   #\n 
##################\n\n""")
    try:
        selection = int(input("Select 1, 2 or 3: "))
        selection -= 1
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\nOnly numbers pls")
    else: 
        if (selection <= 2 or selection >= 0):
            while (1):
                gselection = randrange(0,3)
                try:
                    usaid = wdtgs[selection]
                except IndexError:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Please select a valid number")
                    break
                else:
                    print("")
                
                gsaid = wdtgs[gselection]
                
                print("\n\nYou: " + usaid)
                print("\nCPU: " + gsaid)
                
                if (gselection == selection):
                    print("\nIt's a tie !!!\n")
                    a = input("Press enter to try again, q to quit...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if a == "q":
                        exit(0)
                    else:
                        break 
                if ((gselection == 2 and selection == 0) or (gselection == 1 and selection == 2) or (gselection == 0 and selection == 1)):
                    print("\nYou LOSE !!!!!\n\n\n")
                    a = input("Press enter to try again, q to quit...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if a == "q":
                        exit(0)
                    else:
                        break
                if ((gselection == 0 and selection == 2) or (gselection == 2 and selection == 1) or (gselection == 1 and selection == 0)):
                    print("\nYou WIN !!!!!\n\n\n")
                    a = input("Press enter to try again, q to quit...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if a == "q":
                        exit(0)
                    else:
                        break
        else:
            print("\n\nPls select a valid number")

