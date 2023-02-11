import os
import random 
import hangman_words
import hangman_art


print(hangman_art.logo)
print('\n\t\tWelcome to the Hangman game\n')

language = int(input('Choose words language. 1 for english, 2 for ukrainian: '))
if language == 1:
  word_list = hangman_words.word_list_en
else:
  word_list = hangman_words.word_list_ua

chosen_word = random.choice(word_list)
display = ['_' for letter in chosen_word]
end_of_game = False
lives = len(hangman_art.stages)


while not end_of_game:
  guess = input("\nGuess a letter: ").lower()

  os.system('cls')
  
  if guess in display:
    print('\nYou already guessed this letter.')
  
  for position in range(0, len(chosen_word)):
    if chosen_word[position] == guess:
      display[position] = guess
  
  print(*display) 
  
  if guess not in chosen_word:
    print(f"\nYou guessed letter {guess}, that`s not in the word. You lose a life.")
    
    lives -= 1

    if lives == 0:
      end_of_game = True
      print('\nYou lose.')
    
    print(hangman_art.stages[lives])
    

  if '_' not in display:
    end_of_game = True
    print('\nYou win!')