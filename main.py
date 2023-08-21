import random


# randomly picks word from list - change this later to accept a file with list of words
def pick_word():
    words = ['hello', 'camp', 'letter']
    # this was done bc I want to start with a list of words - change this when pulling from csv
    return [*str(random.choice(words))]


# takes the randomly picked word and asks user to guess letters or the whole word
def guess():
    word = pick_word()
    magic_word = "".join(word)
    count = 10
    print("Number of tries", count)
    print("Type 'exit' to end game")
    blanks = ['_'] * len(word)
    while count != 0:
        # win condition once all the blanks are letters
        if '_' not in blanks:
            print("Word:", "".join(blanks))
            print("YOU WIN!!!!")
            return
        print(*blanks)
        # validating input - exit, spamming
        while True:
            letter = input("Guess a letter or word: ").lower()
            if letter == 'exit':
                print("Thanks for playing!")
                return
            elif len(letter) > len(word):
                print("No Spamming.", letter, "is greater than the length of the guess word.")
            else:
                break
        # win condition for correctly inputted word or letter
        if letter == magic_word:
            print("Word:", magic_word)
            print("YOU WIN!!!!")
            return
        elif letter in word:
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

# Turn to pycharm and add animation of a hanging man
# Make it so user chooses number of tries and tie this with a point system
