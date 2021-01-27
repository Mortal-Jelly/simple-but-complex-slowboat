#you stopped at 2543



import sqlite3
import time
from time import sleep

AdminUsername = "slowboat"
AdminPassword = "china"

mealdeal = 0

wonton = False
hotsoursoup = False
chickensweetcornsoup = False
item1 = ""
item2 = ""
item3 = ""
item4 = ""
item5 = ""


with sqlite3.connect("Login.db") as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
    firstname VARCHAR(20) NOT NULL,
    secondname VARCHAR NOT NULL,
    email VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    postcode VARCHAR(20) NOT NULL,
    city VARCHAR(20) NOT NULL,
    housenum VARCHAR(20) NOT NULL,
    addressline VARCHAR(50) NOT NULL
    )''')



#cursor.execute('''
#INSERT INTO user(firstname, secondname, email, password, city, housenum, addressline)
#VALUES("John", "Doe", "johndoe@gmail.com", "johnspassword", "York", "2", "2 eastfield haxby york")''')
#db.commit()



def mainmenu():
    print("1. Meal for 2 - 5 items.")
    print("2. Meal for 3 - 6 items.")
    print("3. Meal for 4 - 7 items.")
    choice = int(input("Please choose a meal deal. 1 to 3: "))
    
    
    if choice == 1:
        mealdeal = 5
        print("1. Crispy wonton. ")
        print("2. Hot and sour soup. ")
        print("3. Chicken with sweetcorn soup. ")
        choice = int(input("Please choose one starter. 1 to 3: "))

        if choice == 1:
            wonton = True
            if mealdeal == 5:
                items5()
        
            elif mealdeal == 6:
                items6()
        
            elif mealdeal == 7:
                items7()


        
        elif choice == 2:
            hotsoursoup = True
            if mealdeal == 5:
                items5()
        
            elif mealdeal == 6:
                items6()
        
            elif mealdeal == 7:
                items7()
        

    
            elif choice == 3:
                chickensweetcornsoup = True

            if mealdeal == 5:
                items5()
        
            elif mealdeal == 6:
                items6()
        
            elif mealdeal == 7:
                items7()


    
            else:
                print("That is not a choice!")
                mainmenu()
    
        elif choice == 2:
            mealdeal = 6
            print("1. Crispy wonton. ")
            print("2. Hot and sour soup. ")
            print("3. Chicken with sweetcorn soup. ")
            choice = int(input("Please choose one starter. 1 to 3: "))

            if choice == 1:
                startermeal = "Crispy wonton"
                if mealdeal == 5:
                    items5()
        
                elif mealdeal == 6:
                    items6()
        
                elif mealdeal == 7:
                    items7()
    
        elif choice == 3:
            mealdeal = 7
        print("1. Crispy wonton. ")
        print("2. Hot and sour soup. ")
        print("3. Chicken with sweetcorn soup. ")
        choice = int(input("Please choose one starter. 1 to 3: "))

        if choice == 1:
            startermeal = "Crispy wonton"
            if mealdeal == 5:
                items5()
        
            elif mealdeal == 6:
                items6()
        
            elif mealdeal == 7:
                items7()


        
        elif choice == 2:
            startermeal = "Hot and sour soup"
            if mealdeal == 5:
                items5()
        
            elif mealdeal == 6:
                items6()
        
            elif mealdeal == 7:
                items7()
        

    
        elif choice == 3:
            startermeal = "Chicken with sweetcorn soup"

            if mealdeal == 5:
                items5()
        
            elif mealdeal == 6:
                items6()
        
            elif mealdeal == 7:
                items7()


    
        else:
            print("That is not a choice!")
            return
    
    else:
        print("Thats not a choice!")
        sleep(2)
        mainmenu()




def items5():
    print("1. Sizzling beef with black bean sauce.")
    print("2. Sizzling king prawns.")
    print("3. Sizzling chicken with ginger.")
    print("4. Beef with chilli sauce.")
    print("5. Chicken with curry sauce.")
    print("6. Chicken with cashew nuts.")
    print("7. Pork with sweet and sour sauce.")

    choice = int(input("Please choose your first item: "))

    if choice == 1:
        item1 = "Sizzling beef with black bean sauce"
        print("1. Sizzling beef with black bean sauce.")
        print("2. Sizzling king prawns.")
        print("3. Sizzling chicken with ginger.")
        print("4. Beef with chilli sauce.")
        print("5. Chicken with curry sauce.")
        print("6. Chicken with cashew nuts.")
        print("7. Pork with sweet and sour sauce.")
        choice = int(input("Please choose your second item: "))
        
        if choice == 1:
            item2 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 2:
            item2 = "Sizzling king prawns"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 3:
            item2 = "Sizzling chicken with ginger"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 4:
            item2 = "Beef with chilli sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 5:
            item2 = "Chicken with curry sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 6:
            item2 = "Chicken with cashew nuts"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            
            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 7:
            item2 = "Pork with sweet and sour sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
    elif choice == 2:
        item1 = "Sizzling king prawns"
        if choice == 1:
            item1 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your second item: "))
        
            if choice == 1:
                item2 = "Sizzling beef with black bean sauce"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")
                choice = int(input("Please choose your third item: "))

                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")

                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")

                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
            elif choice == 2:
                item2 = "Sizzling king prawns"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")

                choice = int(input("Please choose your third item: "))

                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")

                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")

            elif choice == 3:
                item2 = "Sizzling chicken with ginger"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")
                choice = int(input("Please choose your third item: "))
                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
            elif choice == 4:
                item2 = "Beef with chilli sauce"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")

                choice = int(input("Please choose your third item: "))

                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")

                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                        print("Crispy wonton")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif hotsoursoup == True:
                        print("Hot and sour soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice")
    
                    elif chickensweetcornsoup == True:
                        print("Chicken and sweetcorn soup")
                        print(item1)
                        print(item2)
                        print(item3)
                        print(item4)
                        print(item5)
                        print("egg fried rice"))
# here is where you stopped ctrl v
#          
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

            elif choice == 5:
                item2 = "Chicken with curry sauce"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")
                choice = int(input("Please choose your third item: "))
                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

            elif choice == 6:
                item2 = "Chicken with cashew nuts"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")
                choice = int(input("Please choose your third item: "))
                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

            elif choice == 7:
                item2 = "Pork with sweet and sour sauce"
                print("1. Sizzling beef with black bean sauce.")
                print("2. Sizzling king prawns.")
                print("3. Sizzling chicken with ginger.")
                print("4. Beef with chilli sauce.")
                print("5. Chicken with curry sauce.")
                print("6. Chicken with cashew nuts.")
                print("7. Pork with sweet and sour sauce.")
                choice = int(input("Please choose your third item: "))
                if choice == 1:
                    item3 = "Sizzling beef with black bean sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 2:
                    item3 = "Sizzling king prawns"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 3:
                    item3 = "Sizzling chicken with ginger"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 4:
                    item3 = "Beef with chilli sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 5:
                    item3 = "Chicken with curry sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 6:
                    item3 = "Chicken with cashew nuts"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
                if choice == 7:
                    item3 = "Pork with sweet and sour sauce"
                    if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

    elif choice == 3:
        item1 = "Sizzling chicken with ginger"
        print("1. Sizzling beef with black bean sauce.")
        print("2. Sizzling king prawns.")
        print("3. Sizzling chicken with ginger.")
        print("4. Beef with chilli sauce.")
        print("5. Chicken with curry sauce.")
        print("6. Chicken with cashew nuts.")
        print("7. Pork with sweet and sour sauce.")

        choice = int(input("Please choose your second item: "))

        if choice == 1:
            item2 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
                
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 2:
            item2 = "Sizzling king prawns"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 3:
            item2 = "Sizzling chicken with ginger"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 4:
            item2 = "Beef with chilli sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 5:
            item2 = "Chicken with curry sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 6:
            item2 = "Chicken with cashew nuts"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 7:
            item2 = "Pork with sweet and sour sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

    
    elif choice == 4:
        item1 = "Beef with chilli sauce"
        print("1. Sizzling beef with black bean sauce.")
        print("2. Sizzling king prawns.")
        print("3. Sizzling chicken with ginger.")
        print("4. Beef with chilli sauce.")
        print("5. Chicken with curry sauce.")
        print("6. Chicken with cashew nuts.")
        print("7. Pork with sweet and sour sauce.")
        choice = int(input("Please choose your second item: "))
        
        if choice == 1:
            item2 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 2:
            item2 = "Sizzling king prawns"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 3:
            item2 = "Sizzling chicken with ginger"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 4:
            item2 = "Beef with chilli sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 5:
            item2 = "Chicken with curry sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 6:
            item2 = "Chicken with cashew nuts"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 7:
            item2 = "Pork with sweet and sour sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

    elif choice == 5:
        item1 = "Chicken with curry sauce"
        print("1. Sizzling beef with black bean sauce.")
        print("2. Sizzling king prawns.")
        print("3. Sizzling chicken with ginger.")
        print("4. Beef with chilli sauce.")
        print("5. Chicken with curry sauce.")
        print("6. Chicken with cashew nuts.")
        print("7. Pork with sweet and sour sauce.")
        choice = int(input("Please choose your second item: "))
        
        if choice == 1:
            item2 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 2:
            item2 = "Sizzling king prawns"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 3:
            item2 = "Sizzling chicken with ginger"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 4:
            item2 = "Beef with chilli sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 5:
            item2 = "Chicken with curry sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
        
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 6:
            item2 = "Chicken with cashew nuts"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 7:
            item2 = "Pork with sweet and sour sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

    elif choice == 6:
        item1 = "Chicken with cashew nuts"
        print("1. Sizzling beef with black bean sauce.")
        print("2. Sizzling king prawns.")
        print("3. Sizzling chicken with ginger.")
        print("4. Beef with chilli sauce.")
        print("5. Chicken with curry sauce.")
        print("6. Chicken with cashew nuts.")
        print("7. Pork with sweet and sour sauce.")
        choice = int(input("Please choose your second item: "))
        
        if choice == 1:
            item2 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 2:
            item2 = "Sizzling king prawns"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 3:
            item2 = "Sizzling chicken with ginger"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))
            
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 4:
            item2 = "Beef with chilli sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 5:
            item2 = "Chicken with curry sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 6:
            item2 = "Chicken with cashew nuts"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 7:
            item2 = "Pork with sweet and sour sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

    elif choice == 7:
        item1 = "Pork with sweet and sour sauce"
        print("1. Sizzling beef with black bean sauce.")
        print("2. Sizzling king prawns.")
        print("3. Sizzling chicken with ginger.")
        print("4. Beef with chilli sauce.")
        print("5. Chicken with curry sauce.")
        print("6. Chicken with cashew nuts.")
        print("7. Pork with sweet and sour sauce.")
        choice = int(input("Please choose your second item: "))
        
        if choice == 1:
            item2 = "Sizzling beef with black bean sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 2:
            item2 = "Sizzling king prawns"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 3:
            item2 = "Sizzling chicken with ginger"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
        elif choice == 4:
            item2 = "Beef with chilli sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 5:
            item2 = "Chicken with curry sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 6:
            item2 = "Chicken with cashew nuts"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")
            choice = int(input("Please choose your third item: "))
            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

        elif choice == 7:
            item2 = "Pork with sweet and sour sauce"
            print("1. Sizzling beef with black bean sauce.")
            print("2. Sizzling king prawns.")
            print("3. Sizzling chicken with ginger.")
            print("4. Beef with chilli sauce.")
            print("5. Chicken with curry sauce.")
            print("6. Chicken with cashew nuts.")
            print("7. Pork with sweet and sour sauce.")

            choice = int(input("Please choose your third item: "))

            if choice == 1:
                item3 = "Sizzling beef with black bean sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 2:
                item3 = "Sizzling king prawns"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 3:
                item3 = "Sizzling chicken with ginger"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 4:
                item3 = "Beef with chilli sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 5:
                item3 = "Chicken with curry sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 6:
                item3 = "Chicken with cashew nuts"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
            
            if choice == 7:
                item3 = "Pork with sweet and sour sauce"
                if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")

def items6():
    print("1. Sizzling beef with black bean sauce.")
    print("2. Sizzling king prawns.")
    print("3. Sizzling chicken with ginger.")
    print("4. Beef with chilli sauce.")
    print("5. Chicken with curry sauce.")
    print("6. Chicken with cashew nuts.")
    print("7. Pork with sweet and sour sauce.")

def items7():
    pass

def Login():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    if email == AdminUsername and password == AdminPassword:
        AdminMainmenu()
    
    else:
        find_user = ("SELECT * FROM user WHERE email = ? AND password = ?")
        cursor.execute(find_user, [(email), (password)])
        results = cursor.fetchall()
        
        if results:
            for i in results:
                mainmenu()
                
            else:
                return
            

def LoginorRegister():
    print("1: Login")
    print("2: Register")
    choice = int(input("Please choose an option. 1 or 2"))

    if choice == 1:
        Login()

    elif choice == 2:
        Register()
        
    elif choice != 1 or 2:
        print("That is not a choice! ")
        LoginorRegister()

def if wonton == True:
                    print("Crispy wonton")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif hotsoursoup == True:
                    print("Hot and sour soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice")
    
                elif chickensweetcornsoup == True:
                    print("Chicken and sweetcorn soup")
                    print(item1)
                    print(item2)
                    print(item3)
                    print(item4)
                    print(item5)
                    print("egg fried rice"):
    if wonton == True:
        print("Crispy wonton")
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        print(item5)
        print("egg fried rice")
    
    elif hotsoursoup == True:
        print("Hot and sour soup")
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        print(item5)
        print("egg fried rice")
    
    elif chickensweetcornsoup == True:
        print("Chicken and sweetcorn soup")
        print(item1)
        print(item2)
        print(item3)
        print(item4)
        print(item5)
        print("egg fried rice")

LoginorRegister()
