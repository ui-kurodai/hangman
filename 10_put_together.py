#hang_man_game

def hangman(word):
    wrong = 0
    stages = ['',
              '________        ',
              '|               ',
              '|       |       ',
              '|       0       ',
              '|      /|\      ',
              '|      / \      ',
              '|               ',
              ]
    #init
    rletters = list(word)
    board = ['_']*len(word)
    win = False
    print('Welcome to hangman')

    while wrong < len(stages) - 1:
        print('\n')
        msg = 'guess a letter in the word'
        char = input(msg)
        
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[:e]))

        if '_' not in board:
            print('you win')
            print(' '.join(board))
            win = True
            break
    if not win:
            print('\n'.join(stages[:wrong+1]))
            print('you lose! The answer is {}.'.format(word))

'_________________'

import random

word_list = ['word', 'world', 'wonder', 'whether']
word_index = random.randint(0,4)
hangman(word_list[word_index])

    
