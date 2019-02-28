for i in range (1,7):
    r=input("press r to roll, q to quit : " )

    if r=='r':  
        if i%3 == 1:
            print("you got",6)

        elif i%3 == 2:
            print("you got",2)

        else:
            print("you got",3)

    if r == 'q':
        print("Bye!")
        exit()

print("congratulations,you won!")               