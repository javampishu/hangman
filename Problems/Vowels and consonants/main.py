sequence = input()
vowels = 'aeiou'

for letter in sequence:
    if letter.isalpha():
        if letter in vowels:
            print('vowel')
        else:
            print('consonant')
    else:
        break
