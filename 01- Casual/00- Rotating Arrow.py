import time
import os
clear = lambda: os.system('cls')
clear()
while 1:
    #Right Arrow
    for n in range(1,5):
        print("\n")
    for n in range(1,6):
        print ("                                                  ","*"*n)
    print("                              * * * * * * * * * * * * * *")
    for n in range(5,0,-1):
        print ("                                                  ","*"*n)

    time.sleep(.5)
    clear()

    #Down Arrow
    for n in range(1,10):
        print("\n")
    for n in range (0,8):
        print("                            *")
    for n in range(0,7):
        print("                ","  "*(n), "* "*(11-2*n))

    time.sleep(.5)
    clear()

    #Left Arrow
    for n in range(1,5):
        print("\n")
    for n in range(1,6):
        print (" "*(5-n), "*"*n)
    print("* * * * * * * * * * * * * *")
    for n in range(1,6):
        print (" "*(n-1),"*"*(6-n))

    time.sleep(.5)
    clear()

    #Up Arrow
    for n in range(1,7):
        print("                 ", " "*(12-2*n), "* "*(2*n-1))
    for n in range(1,9):
        print("                             *")


    time.sleep(.5)
    clear()