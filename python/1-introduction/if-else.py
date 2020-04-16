#!/bin/python3
#from random import randrange

if __name__ == '__main__':
    #n = randrange ( 99 ) + 1
    n = int( input() )
    # range(start, stop) take into account from start to stop-1
    if 1 <= n <= 100:
    #if n in range(1,101):
        if (n % 2) != 0:
            print("Weird")
        else:
            #if n in range(2,6):
            if 2<=n<=5:
                print("Not Weird")
            #elif n in range(6,21):
            elif 6<=n<=20:
                print("Weird")
            elif n > 20:
                print("Not Weird")