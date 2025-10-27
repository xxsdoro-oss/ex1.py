import random

options = ('rock', 'paper', 'scissors')

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input('Enter a choice(rock, paper ,scissors): ')

    print(f'player:{player}')
    print(f'computer: {computer}')

    if player == computer:
        print('It\'s a tie!')
    elif player == 'rock' and computer == 'scissors':
        print('YOU WIN!')
    elif player == 'paper' and computer == 'rock':
        print('YOU WIN!')
    elif player == 'scissors' and computer == 'paper':
        print('YOU WIN!')
    else:
        print('You lose!')

    if not input('Play again?(y or n): ').lower() == 'y':
        running = False

print('Thanks for playing!')
