# Write your code here
import random

word_list = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(word_list)
signs = (len(correct_word)) * "-"
user_word = ''
tries = 0
faults = ''

print("H A N G M A N")

user_start = input('Type "play" to play the game, "exit" to quit: ')
if user_start == "play":
    while tries < 8:
        print()
        print(signs)
        user_letter = input("Input a letter: ")
        counter = 0
        if len(user_letter) != 1:
            print("You should input a single letter")
        elif 'a' <= user_letter <= 'z':
            if (user_letter in correct_word) and (user_letter not in signs):
                for i in correct_word:
                    if user_letter == i:
                        signs = signs[:counter] + i + signs[counter+1:]
                    counter += 1
            elif (user_letter in correct_word and user_letter in signs) or user_letter in faults:
                print("You already typed this letter")
            else:
                tries += 1
                faults = faults + user_letter
                print("No such letter in the word")
        else:
            print("It is not an ASCII lowercase letter")

        if signs == correct_word:
            print("You guessed the word!")
            print("You survived!")
            break

    if signs != correct_word:
        print("You are hanged!")



