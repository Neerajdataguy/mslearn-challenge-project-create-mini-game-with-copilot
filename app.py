# write python code to accept a string and value of string should be 'rock', 'paper' or 'scissors'.
#  If any other value is entered, print 'Invalid input' and ask for value again from user
# if passed value is valid, then randomly select a value from 'rock', 'paper' or 'scissors' and print whether 
# user has won, lost or draw. If user wins, print 'You win', if user loses, print 'You lose' and if it is a draw, print 'It is a draw'
# Also ask user if he wants to play again. If user enters 'yes', repeat the process,
#  else display the score of user and computer and exit the game

import random
user_score = 0
computer_score = 0
while True:
    user = input("Enter 'rock', 'paper' or 'scissors': ")
    if user not in ['rock', 'paper', 'scissors']:
        print('Invalid input')
        continue
    computer = random.choice(['rock', 'paper', 'scissors'])
    if user == computer:
        print('It is a draw')
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        print('You win')
        user_score += 1
    else:
        print('You lose')
        computer_score += 1
    play_again = input('Do you want to play again? ')
    if play_again != 'yes':
        print(f'User score: {user_score}')
        print(f'Computer score: {computer_score}')
        break