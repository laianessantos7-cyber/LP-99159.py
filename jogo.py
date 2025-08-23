import random
import os

#Limpar terminal
os.system("cls")


number= random.randint(1, 10)

guess= input("Vamos brincar! ")
guess= int(guess)

if(guess== number) :
    print("Voce venceu! ")
