from ttt_func import print_grid, get_choice, win_check

#empty grid (with nums for choices)
tttgrid = [' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' ', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', ' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' ']
turn = 1
win = 0



#start game
print("Welcome to Tic-Tac-Toe!\n")
print_grid(tttgrid)
print("")


while turn < 10:
    choice = get_choice()
    if tttgrid[choice] == 'X' or tttgrid[choice] == 'O':
        print("Make a valid choice.\n")
        choice = get_choice()
    if turn % 2 == 0:
        tttgrid[choice] = 'O'
    else:
        tttgrid[choice] = 'X'
    print_grid(tttgrid)
    print("")
    
    win = win_check(tttgrid)
    if win == 1 or win == 2:
        turn = 10
    else:
        turn += 1
        
if win == 1:
    print("Player 1 Wins. Congratulations!\n")
elif win == 2:
    print("Player 2 Wins. Congratulations!\n")
else:
    print("It's a tie! Try again later.\n")