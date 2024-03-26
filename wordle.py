import random
import tkinter as tk
from enum import Enum
from colorama import Fore

Hints = Enum("Hints", ["GREY", "YELLOW", "GREEN"])

wordleLa = []
wordleTa = []

with open(r"wordleDictionary\wordle-La.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        wordleLa.append(line.strip())

with open(r"wordleDictionary\wordle-Ta.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        wordleTa.append(line.strip())

word = random.choice(wordleLa).strip()
guesses = 0

root = tk.Tk()
root.geometry('600x400')

def submit():
    global guesses

    guesses += 1
    guess = guess_var.get()
    out = [["", None] for i in range(5)]
    for i, letter in enumerate(guess):
        out[i][0] = letter
        if letter not in word:
            out[i][1] = Hints.GREY
        elif letter == word[i]:
            out[i][1] = Hints.GREEN
        elif guess.count(letter) > word.count(letter):
            if guess[:i+1].count(letter) - sum([1 for a, b in zip(word[i:], guess[i:]) if a == b and a == letter]) > word.count(letter): #subtract number of green letter after i
                out[i][1] = Hints.GREY
            else:
                out[i][1] = Hints.YELLOW
        else:
            out[i][1] = Hints.YELLOW

def validate(input):
    if not input.isalpha():
        print("guess is not only letters")
        return False
    elif len(input) != 5:
        print("guess is wrong length")
        return False
    elif not (input in wordleLa or input in wordleTa):
        print("guess is not in word list")
        return False
    else:
        return True

guess_var = tk.StringVar()

guess_label = tk.Label(root, text = 'guess:')

entry = tk.Entry(root, textvariable=guess_var)
reg = root.register(validate)
entry.config(validate='key', validatecommand=(reg, '%P'))

btn = tk.Button(root, text='submit', command=submit)
guess_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
btn.grid(row=1, column=1)

root.mainloop()