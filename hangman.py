import random
words = ["apple","hydroelectricity","windmill","biospherereserve","biodiversity","dragon","fiction","python","snake","Tiger","lion","eagle","fountain","elctromagnetism","acid","base","salt","metal","magnetism","mathematics","java","javascript"]
mode = input("Do you want to play in easy or normal mode?\nPress E for easy and N for normal mode.   ")
if mode.upper() == "E":
    mode = "E"
else:
    mode = "N"
print("Type hint anytime to get a hint you will have three hints.")
print("Type quit anytime to quit.\n\n\n")
mWords= words.copy()
wronguess= 0
vowels = ["a","e","i","o","u"]
guessedvowels=[]
consonants = []
hints = 3
win = True
def drawhangman():
    if wronguess==0:
        print("|-------")
    elif wronguess==1:
        print("|-------O")
    elif wronguess == 2:
        print("|-------0")
        print("|      /") 
    elif wronguess == 3:
        print("|-------0")
        print("|      /|")
    elif wronguess == 4:
        print("|-------O")
        print("|      /|\ ")
    elif wronguess == 5:
        print("|-------O")
        print("|      /|\ ")
        print("|      /")
    elif wronguess == 6:
        print("|-------O")
        print("|      /|\ ")
        print("|      /-\ ")
def replace(word):
    global consonants
    global guessedvowels
    fib = ""
    for i in word:
        if i not in vowels and i not in guessedvowels:
            fib += "_ "
            if i not in consonants:
              consonants.append(i)
        else:
            fib += i+ " "
    return fib       
def givehint(word):
    global consonants
    replace(word)
    hintchar = random.choice(consonants)
    print(hintchar)
    if hintchar not in guessedvowels:
      guessedvowels.append(hintchar)
      consonants.remove(hintchar)
    else:
        print("Sorry hint unavailable!")
    consonants = []    

def gameloop():
    global wronguess
    global vowels
    global words
    global mWords
    global guessedvowels
    global win
    global hints
    i=0
    while(i<len(words)):
        drawhangman()
        print("\n\n\n")
        if wronguess == 6:
            print("You lost the game!")
            return
        print(replace(words[i]))
        guess=input("Guess the word or a consonant! ")
        if len(guess) == 1:
            if guess in words[i] and guess not in vowels:
                guessedvowels.append(guess)
                if "_" not in replace(words[i]):
                    print(replace(words[i]))
                    guessedvowels = []
                    if mode == "E":
                        wronguess = 0
                    i+=1
                    print("Good job! ")
                    continue
                else:
                  continue
            else:
                wronguess += 1
                continue
        else:
            if guess.lower() == "quit":
                return
            elif guess.lower() == "hint" and hints > 0:
                givehint(words[i])
                hints-=1
                if "_" not in replace(words[i]):
                    drawhangman()
                    print("\n\n\n")
                    print(replace(words[i]))
                    print("Good job!")
                    i+=1
                    guessedvowels = []
                continue
            elif guess == words[i]:
                guessedvowels=[]
                print("Good job")
                if mode =="E":
                    wronguess=0
                i+=1
                continue
            else:
                wronguess += 1
                continue
    print("Yes, you won the game! ")
    return
gameloop()
