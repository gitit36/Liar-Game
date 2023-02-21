import random
import time
from os import system
with open("wordsfm.csv", "r") as f:
    words = f.read().strip().split(",")
    word = words[random.randint(0, len(words))]
    liar = random.randint(0,6)
    print(liar)
    game = []

    for i in range(5):
        
        if i == liar:
            print("liar")
        else:
            if "\n" in word:
                print(word.split("\n")[1])
            else: 
                print(word)
        input()
        system("clear")
        time.sleep(2) 
        
