import random


def hangman():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "imbe", "jackfruit", "kiwi",
             "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine",
             "ugli", "vanilla", "watermelon", "ximenia", "yellow watermelon", "zucchini"]
    word = random.choice(words)
    word = word.lower()
    word_length = len(word)
    word_list = list(word)
    display = ["_"] * word_length
    display_string = " ".join(display)
    print(display_string)
    tries = 0
    max_tries = 6
    while tries < max_tries:
        letter = input("Enter a letter: ").lower()
        if not letter.isalpha() or len(letter) > 1:
            print("Please enter a single letter")
            continue
        if letter in word_list:
            for i in range(word_length):
                if word_list[i] == letter:
                    display[i] = letter
            display_string = " ".join(display)
            print(display_string)
            if "_" not in display:
                print("You win!")
                break
        else:
            tries += 1
            print("Wrong letter!")
            print("You have", max_tries - tries, "tries left")
    if tries == max_tries:
        print("You lose!")
        print("The word was", word)
    return


hangman()
