"""
This is just a simple tic tac toe game.
"""
def instruction():
    """Print instructions for tic tac toe."""
    print("""\
This is a Tic Tac Toe game.
Player 1 will be 'x' and player 2 will be 'o'.
The position to place on the board will be as follows:
        1|2|3
        -----
        4|5|6
        -----
        7|8|9
""")
    
def printBoard(board):
    """Prints the board for tic tac toe. Assumes that the board has exactly 9 elements.

    eg. o| |x
        -----
         |x|
        -----
         |o|o
    """
    print(board[0], board[1], board[2], sep='|')
    print("-----")
    print(board[3], board[4], board[5], sep='|')
    print("-----")
    print(board[6], board[7], board[8], sep='|')
    
def update_state(player, position, board):
    """Updates player's move on board. Does not assume if it is valid. Modifies `board`.
    """
    if player == 1:
        board[position-1] = 'x'
    elif player == 2:
        board[position-1] = 'o'

def isValidMove(tile, board):
    """Checks whether the player had made a valid move ie. 0 < tile <= 9 and the tile had not been occupied."""
    try:
        tile = int(tile)
    except ValueError:
        return False
    return tile > 0 and tile <= 9 and board[tile-1] == ' '

def isAWin(board):
    """Determines whether the board is a winning state ie. 3 in a row."""
    #Check horizontal
    if ((board[0] != ' ' and board[0] == board[1] == board[2])
        or (board[3] != ' ' and board[3] == board[4] == board[5])
        or (board[6] != ' ' and board[6] == board[7] == board[8])):
        return True

    #Check vertical
    if ((board[0] != ' ' and board[0] == board[3] == board[6])
        or (board[1] != ' ' and board[1] == board[4] == board[7])
        or (board[2] != ' ' and board[2] == board[5] == board[8])):
        return True

    #Check diagonal
    if ((board[0] != ' ' and board[0] == board[4] == board[8])
        or (board[2] != ' ' and board[2] == board[4] == board[6])):
        return True

    return False

def main():
    """Runs the game."""
    instruction()
    board = [' ',' ',' ',
             ' ',' ',' ',
             ' ',' ',' ']
    player = 1
    while True:
        printBoard(board)
        player_move = input("Player %d's move: " % player)
        while not isValidMove(player_move, board):
            player_move = input("That's not a valid move. Enter again: ")
        player_move = int(player_move)
        update_state(player, player_move, board)
        if (isAWin(board)):
            print("Player %d wins! Congratulations!" % player)
            break
        if ' ' not in board:
            print("It's a tie!")
            break
        if player == 1:
            player = 2
        elif player == 2:
            player = 1
        

if __name__ == '__main__':
    main()
