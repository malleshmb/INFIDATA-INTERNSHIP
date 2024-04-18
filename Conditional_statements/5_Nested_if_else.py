print("Select a Food Category 1: veg, 2:Non-veg")
choice = int(input())
if(choice == 1):
    print("You have selected veg category")
    menu = int(input("select menu 1:meals, 2:Idli, 3:Dosa"))
    if(menu==1):
        print("You have selected meals")
    elif(menu==2):
        print("you have selected Idli")
    elif(menu==3):
        print("You have selected Dosa")
    else:
        print("Menu is not available")
elif(choice==2):
    print("You have selected Non-veg")
    menu = int(input("select menu 4:Chiken, 5:Mutton, 6:Fish"))
    if(menu==4):
        print("You have selected chiken")
    elif(choice==5):
        print("You have selected mutton")
    elif(choice==6):
        print("You have selected beaf")
else:
    print("Invalid category")
