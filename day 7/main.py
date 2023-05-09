
import hangman_art
import hangman_words
import random
from hangman_words import word_list
from hangman_art import logo, stages



word = random.choice(word_list)
word_length = len(word)
end_of_game = False

print(f'Pssst, the solution is {word}.')

display = []
for _ in range(word_length):
    display += "_"

lives = 6

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    n = 1
    if guess in display:
        print("you already found this letter")
    for position in range(word_length):
        letter = word[position]
        
        
        if letter == guess:
            display[position] = letter
    if guess not in word:
        print("wrong answer bud")
        lives = lives -1
        if lives == 0:
            print("no lives remaining u lose lol")
            end_of_game= True
    print (stages[lives])     
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
        
       
    
