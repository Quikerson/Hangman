import random
from words import words
from Hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words) #randomly choses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 8

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        #' '.join(['a', 'b', 'cd'])  --> 'a b cd'
        print("------------")
        print("--------------")
        print("----------------")
        print('You have', lives, 'lives left and you have used these letters', ' '.join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #Takes away a life if wrong
                print('Letter is not in word')
    
        elif user_letter in used_letters:
            print('You have already guessed that word. Please try again')

        else:
            print('You did type an invalid character')

        print("----------------")
        print("--------------")
        print("------------")

    #Gets here when len(word_letters) == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was', word)
    else:
        print('you guessed the word', word, '!!!')
    print("------------")
    print("--------------")
    print("----------------")

if __name__ == '__main__':
    hangman()
