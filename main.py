#Metamo kauliņu kalkulators
# Autors: Oskar A.
# Datums: 03.11.2021 V2V
from random import randint
from datetime import date
import math

today = date.today()
print("Šodienas datums:","[",today,"]")
print ("Autors: Oskar A.")
txt = ('\033[94m{}\033[0m'.format("[Metamo kauliņu kalkulators]"))
INF = txt.center(65)
print(INF)

def paraSkaitlis(skaits):

    P = 3*skaits / 6 * skaits
    print(P)
    print("Tev ir 50% iespeja uzmest para skaitli")

def NeparaSkaitlis(skaits):

    print("WIP")

def vienadSkaitlis(skaits):

    print("WIP")

def metode(skaits):
    print("1")

def skate():
    total = sum(diRoll())
    while total > 8 and total < 20:
        print(diRoll())
    while True:
        total = sum(diRoll())
        if total > 8 and total < 20:
            print(diRoll())
            break

def diRoll():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    dice3 = randint(1, 6)
    dice4 = randint(1, 6)
    diceRolls = dice1, dice2, dice3, dice4
    return sorted(diceRolls)

if __name__ == '__main__':
    print("This is ...")
    metode = int(input("Ko velies apreikint? [1- , 2- , 3- , 4- ] : "))
    skaite = int(input("Cik kaulinos metisi: "))
    if metode == 2:
        skate()
    if metode == 1:
        paraSkaitlis(skaite)
    else:
        exit(0)

