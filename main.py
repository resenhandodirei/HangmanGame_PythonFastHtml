import random

words = ["java", "javascript"]
sorted_word = random.choice(words)

hidden_word = '-' * len(sorted_word)

guessed_letters = []
max_tries = 6

while True:
    print(hidden_word)

    letter = input('Type a letter ')

    if letter in guessed_letters:
        print('You already typed this letter. Try again, please!')
        continue
    guessed_letters.append(letter)

    if letter in sorted_word:
        list_hidden_word = list(hidden_word)
        for i in range(len(sorted_word)):
            if letter == sorted_word[i]:
                list_hidden_word[i] = letter
        hidden_word = ''.join(list_hidden_word)
    else:
        max_tries -= 1
        print(f'Letter does not exist in the word. You have {max_tries} tries left.')

    if hidden_word == sorted_word:
        print(f"Congratulations! You guessed the word '{sorted_word}'!")
        break
    elif max_tries == 0:
        print(f"You lost! The word was '{sorted_word}'.")
        break
