bill=0
firstValue=int(input("Welcome to restaurant\n 1-Menu\n 2-Exit\n Please make your choice:"))
while True:
    if firstValue==1:
        Menu=["Dishes","Soup","Desserts","Salads"]
        for m in Menu:
            print(m)
        secondValue=int(input("Please make your choice:\n"))
        if secondValue==1:
            Dishes=["1-Pide:30 TL ","2-Mantı:40 TL","3-Sarma:40 TL","4-Ciğer:40 TL","5-Köfte:40 TL"]
            for d in Dishes:
                print(d)
            thirdValue=int(input("Please make your choice:"))
            if thirdValue==1:
                print("Your choice",Dishes[0])
                bill=bill+30
                print("Your total bill:",bill)
            elif thirdValue==2:
                print("Your choice",Dishes[1])
                bill=bill+40
                print("Your total bill:",bill)
            elif thirdValue == 3:
                print("Your choice",Dishes[2])
                bill = bill + 40
                print("Your total bill:", bill)
            elif thirdValue ==4:
                print("Your choice",Dishes[3])
                bill = bill + 40
                print("Your total bill:", bill)
            elif thirdValue == 5:
                print("Your choice",Dishes[4])
                bill = bill + 40
                print("Your total bill:", bill)
            else:
                print("Error")
        elif secondValue==2:
            Soup=["1-Mercimek:30 TL ","2-Kelle Paça:40 TL","3-Yayla:30 TL","4-Mantar:30 TL","5-Tarhana:30 TL"]
            for s in Soup:
                print(s)
            thirdValue = int(input("Please make your choice:\n"))
            if thirdValue == 1:
                print("Your choice", Soup[0])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 2:
                print("Your choice",Soup[1])
                bill = bill + 40
                print("Your total bill:", bill)
            elif thirdValue == 3:
                print("Your choice", Soup[2])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 4:
                print("Your choice", Soup[3])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 5:
                print("Your choice", Soup[4])
                bill = bill + 30
                print("Your total bill:", bill)
            else:
                print("Error")
        elif secondValue == 3:
            Desserts = ["1-Baklava:50 TL ", "2-CheeseCake:40 TL", "3-Ekler:30 TL", "4-Kazandibi:30 TL", "5-Medovik:30 TL"]
            for da in Desserts:
                print(da)
            thirdValue = int(input("Please make your choice:\n"))
            if thirdValue == 1:
                print("Your choice",Desserts[0])
                bill = bill + 50
                print("Your total bill:", bill)
            elif thirdValue == 2:
                print("Your choice", Desserts[1])
                bill = bill + 40
                print("Your total bill:", bill)
            elif thirdValue == 3:
                print("Your choice", Desserts[2])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 4:
                print("Your choice", Desserts[3])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 5:
                print("Your choice", Desserts[4])
                bill = bill + 30
                print("Your total bill:", bill)
            else:
                print("Error")
        elif secondValue == 4:
            Salads = ["1-Coban:30 TL ", "2-Mevsim:40 TL", "3-Rus Salad:30 TL", "4-Caesar:30 TL", "5-Gavurdagı:30 TL"]
            for a in Salads:
                print(a)
            thirdValue = int(input("Please make your choice:\n"))
            if thirdValue == 1:
                print("Your choice",Salads[0])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 2:
                print("Your choice", Salads[1])
                bill = bill + 40
                print("Your total bill:", bill)
            elif thirdValue == 3:
                print("Your choice", Salads[2])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 4:
                print("Your choice", Salads[3])
                bill = bill + 30
                print("Your total bill:", bill)
            elif thirdValue == 5:
                print("Your choice", Salads[4])
                bill = bill + 30
                print("Your total bill:", bill)
            else:
                print("Error")
        elif firstValue==0:
            print("Hope to see you again")
        else:
            print("Error")













