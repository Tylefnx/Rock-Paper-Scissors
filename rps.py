from random import randrange
import os
wdtgs = ["anan", "rock", "scissors", "paper"]
while (1):
    print("""
##############
Rock = 1\n
Paper= 2\n
Scissors = 3\n
##############\n\n""")
    try:
        selection = int(input("Select 1, 2 or 3: "))
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n\nOnly numbers pls")
    else: 
        if (selection <= 3 or selection >= 1):
            while (1):
                gselection = randrange(1,4)
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
                if ((gselection == 3 and selection == 1) or (gselection == 2 and selection == 3) or (gselection == 1 and selection == 2)):
                    print("\nYou LOSE !!!!!\n\n\n")
                    selection = 0
                    a = input("Press enter to try again, q to quit...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if a == "q":
                        exit(0)
                    else:
                        break
                if ((gselection == 1 and selection == 3) or (gselection == 3 and selection == 2) or (gselection == 2 and selection == 1)):
                    print("\nYou WIN !!!!!\n\n\n")
                    selection = 0
                    a = input("Press enter to try again, q to quit...")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    if a == "q":
                        exit(0)
                    else:
                        break
        else:
            print("\n\nPls select a valid number")

