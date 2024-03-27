import random
import tkinter as tk

alphabet = {
    'a':None,
    'b':None,
    'c':None,
    'd':None,
    'e':None,
    'f':None,
    'g':None,
    'h':None,
    'i':None,
    'j':None,
    'k':None,
    'l':None,
    'm':None,
    'n':None,
    'o':None,
    'p':None,
    'q':None,
    'r':None,
    's':None,
    't':None,
    'u':None,
    'v':None,
    'w':None,
    'x':None,
    'y':None,
    'z':None
}

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

word = random.choice(wordleLa)

wordLetters = {}
for letter in word:
    if letter not in wordLetters:
        wordLetters.update({letter:0})
    wordLetters[letter] += 1

guesses = 0

def submit():
    global guesses

    guess = guess_var.get()

    if not guess.isalpha():
        error.config(text="guess must be only letters")
        return
    elif len(guess) != len(word):
        error.config(text=f"guess must be {len(word)} letters")
        return
    elif not (guess in wordleLa or guess in wordleTa):
        error.config(text="guess is not in word list")
        return
    
    error.config(text="")
    entry.delete(0, 'end')

    guesses += 1
    wordLettersC = wordLetters.copy()

    guess_frame = tk.Frame(main)
    guess_frame.pack(side=tk.TOP)

    for i, letter in enumerate(guess):
        color = ''

        if letter not in word or wordLettersC[letter] == 0:
            color = 'grey'
            alphabet[letter].config(bg='grey')
        elif letter == word[i]:
            wordLettersC[letter] -= 1
            color = 'green'
            alphabet[letter].config(bg='green')
        else:
            wordLettersC[letter] -= 1
            color = 'yellow'
            if alphabet[letter].cget('bg') == 'white':
                alphabet[letter].config(bg='yellow')
        
        label = tk.Label(guess_frame, text=letter, bg=color, width=2, pady=5)
        label.pack(side=tk.LEFT, padx=2, pady=2)

    if guess == word:
        entry_frame.pack_forget()
        error.config(text=str(guesses) + " guesses!")

root = tk.Tk()
root.title("wordle")

main = tk.Frame()
main.pack(padx=3, pady=3)


keyboard_frames = [tk.Frame(main) for i in range(3)]
keyboard = ['zxcvbnm', 'asdfghjkl', 'qwertyuiop']
for i, row in enumerate(keyboard):
    keyboard_frames[i].pack(side=tk.BOTTOM)
    for letter in row:
        label = tk.Label(keyboard_frames[i], text=letter, bg='white', width=2, pady=5)
        label.pack(side=tk.LEFT)
        alphabet[letter] = label

entry_frame = tk.Frame(main)
guess_var = tk.StringVar()
entry = tk.Entry(entry_frame, textvariable=guess_var)
btn = tk.Button(entry_frame, text="submit", command=submit)
error = tk.Label(main)

entry_frame.pack(side=tk.BOTTOM, pady=5)
entry.pack(side=tk.LEFT, padx=5)
btn.pack(side=tk.LEFT, padx=5)
error.pack(side=tk.BOTTOM, pady=5)

main.mainloop()