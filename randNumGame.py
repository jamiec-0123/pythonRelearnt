import random
import sys
import os

correctGuess = False
randomNumber = random.randint(0,20)

while(correctGuess == False):
        stringGuess = input("Guess the random nuber between 1 and 10 ")
        try:
                intGuess = int(stringGuess)

        except:
                stringGuess = input("ERROR Guess the random nuber between 1 and 10 ")
        else:
                if(intGuess > randomNumber ):
                    print("Too high")
                elif(intGuess<randomNumber):
                    print("Too low")
                else:
                    print("Youve won")
                    correctGuess = True
