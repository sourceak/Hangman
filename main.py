import random
import csv

# randomly picks word from a csv file
def pick_word():
    filename = "4000-words.csv"

    rows = []

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            rows.append(row)
    return random.choice(rows)


# takes the randomly picked word and asks user to guess letters or the whole word
def guess():
    # use two variables to work with word as a list and a string
    magic_word = pick_word()
    word = [char for string in magic_word for char in string]
    magic_word = (" ".join(magic_word))

    count = 10
    print("Number of tries", count)
    print("Type 'exit' to end game\n")
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
            print(f"Word: {magic_word}")
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
    print(f"The Magic Word is: {magic_word}")


guess()

# Turn to pycharm and add animation of a hanging man
# Add guessed letters box so user can see already guessed letters
# Make it so user chooses number of tries and tie this with a point system
