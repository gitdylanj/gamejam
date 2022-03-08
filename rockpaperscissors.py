import random
import sys

print("ROCK PAPER SCISSORS")
print('type for move: (r)ock, (p)aper, (s)cissors. Input "exit" to exit')
wins = 0
ties = 0
losses = 0
moves = [-1, 0, 1]

dict = {'r':  -1, 'p': 0, 's': -1, 'exit': 'exit'}

while True:
    print('__wins_=_' + str(wins) + '__losses_=_' + str(losses) + '__ties_=_' + str(ties) + '__')
    response = dict[input()] 
    comp_move = random.choice(moves)

    if response == 'exit':
        print('thanks for playing')
        sys.exit()
    elif response - comp_move == 1:
        print('you won')
        wins += 1
    elif response - comp_move == -2:
        print('you won')
        wins += 1
    elif response - comp_move == 0:
        print('you tied')
        ties += 1
    else:
        print('you lost')
        losses += 1