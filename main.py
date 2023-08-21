import random


def pick_word():
    words = ['hello', 'camp', 'letter']
    # this was done bc I want to start with a list of words - change this when pulling from csv
    return [*str(random.choice(words))]


def guess():
    word = pick_word()
    count = 10
    print("Number of tries", count)
    print("Type 'exit' to end game")
    blanks = ['_'] * len(word)
    while count != 0:
        if '_' not in blanks:
            print("Word:", "".join(blanks))
            print("YOU WIN!!!!")
            return
        print(*blanks)
        letter = input("Guess a letter: ").lower()
        if letter == 'exit':
            print("Thanks for playing!")
            return
        if letter in word:
            while letter in word:
                index = word.index(letter)
                blanks[index] = letter
                word[index] = '_'
            if '_' in blanks:
                print("CORRECT! (", count, "tries remaining)")
        else:
            count -= 1
            print("Sorry, wrong letter... (", count, "tries remaining)")
    print("No more tries left. You lose.")


guess()
