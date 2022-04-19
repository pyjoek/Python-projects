from ast import Num
import random

while True:
    num = int(input("Enter yout guess: "))
    m = random.randint(0,9)
    if num == m:
        print("Wow you are a genius")
        break
    else:
        print("Oops! you missed that")
