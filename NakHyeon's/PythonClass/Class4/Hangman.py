import random

default_words = ["python", "java", "ruby", "javascript", "csharp", "swift", "kotlin", "php", "html", "css"]
cheat_mode = False

def add_word(new_word):
    default_words.append(new_word)
    print("Word added")


def remove_word(rm_word):
    if rm_word in default_words:
        default_words.remove(rm_word)
        print("Word removed")
    else:
        print("Word not found")


def play_game():
    game_word = random.choice(default_words)
    print("Word selected")
    if cheat_mode:
        print("Cheat mode enabled")
        print("Word:", game_word)
    left_attempts = 7
    guessed_letters = []
    while left_attempts > 0:
        print("Guessed letters: ", end="")
        for letter in guessed_letters:
            print(letter, end=" ")
        print()
        print("Word: ", end="")
        for letter in game_word:
            if letter in guessed_letters:
                print(letter, end="")
            else:
                print("_", end="")
        print()
        if "_" not in [letter if letter in guessed_letters else "_" for letter in game_word]:
            print("You won!")
            break
        print("Attempts left: ", left_attempts)
        letter = input("Enter a letter: ").strip()
        if len(letter) != 1:
            print("Invalid input")
            continue
        if letter in guessed_letters:
            print("Letter already guessed")
            continue
        guessed_letters.append(letter)
        if letter not in game_word:
            left_attempts -= 1
    if left_attempts == 0:
        print("You lost! The word was:", game_word)


while True:
    command = input("command: ").strip().lower()
    if command.startswith("quit"):
        exit(1)
    elif command.startswith("start"):
        print("Game started")
        play_game()
    elif command.startswith("help"):
        print("Type 'start' to start the game")
    elif command.startswith("add"):
        print("Adding a new word")
        word = input("Enter the word: ").strip()
        add_word(word)
    elif command.startswith("remove"):
        print("Removing a word")
        word = input("Enter the word: ").strip()
        remove_word(word)
    elif command.startswith("sudo"):
        cheat_mode = True
    elif command.startswith("dosu"):
        cheat_mode = False
    else:
        print("Unknown command")
