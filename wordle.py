import random
import sys
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
        wordleLa.append(line.strip().casefold())

with open(r"wordleDictionary\wordle-Ta.txt", "r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        wordleTa.append(line.strip().casefold())

if len(sys.argv) > 1:
    temp = sys.argv[1]
    if not temp.isalpha():
        print("word must be only letters")
        sys.exit()
    elif len(temp) != 5:
        print("guess must be 5 letters")
        sys.exit()
    elif not (temp in wordleLa or temp in wordleTa):
        print("guess is not in word list")
        sys.exit()
    else:
        word = temp.casefold()
else:
    word = random.choice(wordleLa).casefold()

wordLetters = {}
for letter in word:
    if letter not in wordLetters:
        wordLetters.update({letter:0})
    wordLetters[letter] += 1

guesses = 0
clear = None

def set_message(text, flash=False):
    global clear
    if clear is not None:
        root.after_cancel(clear)
    message.config(text=text)
    if flash:
        clear = root.after(1000, lambda: message.config(text=""))

def submit(_=None):
    global guesses

    guess = guess_var.get().casefold()

    if not guess.isalpha():
        set_message("guess must be only letters", True)
        return
    elif len(guess) != len(word):
        set_message(f"guess must be {len(word)} letters", True)
        return
    elif not (guess in wordleLa or guess in wordleTa):
        set_message("guess is not in word list", True)
        return
    
    set_message("")
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
        
        label = tk.Label(guess_frame, text=letter.upper(), bg=color, width=2, pady=5)
        label.pack(side=tk.LEFT, padx=2, pady=2)

    if guess == word:
        entry_frame.pack_forget()
        set_message(str(guesses) + (" guess!" if guesses == 1 else " guesses!"))

root = tk.Tk()
root.title("wordle")

main = tk.Frame()
main.pack(padx=3, pady=3)

keyboard_frames = [tk.Frame(main) for i in range(3)]
keyboard = ['zxcvbnm', 'asdfghjkl', 'qwertyuiop']
for i, row in enumerate(keyboard):
    keyboard_frames[i].pack(side=tk.BOTTOM)
    for letter in row:
        label = tk.Label(keyboard_frames[i], text=letter.upper(), bg='white', width=2, pady=5)
        label.pack(side=tk.LEFT)
        alphabet[letter] = label

entry_frame = tk.Frame(main)
guess_var = tk.StringVar()
entry = tk.Entry(entry_frame, textvariable=guess_var)
btn = tk.Button(entry_frame, text="submit")
root.bind('<Return>', submit)
message = tk.Label(main)

entry_frame.pack(side=tk.BOTTOM, pady=5)
entry.pack(side=tk.LEFT, padx=5)
btn.pack(side=tk.LEFT, padx=5)
message.pack(side=tk.BOTTOM, pady=5)

main.mainloop()