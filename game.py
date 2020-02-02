import random
def display_board():
    """
                    This function displays the board
                    Date:02/02/2020
                    Created By:Alekhyo
                    Input:None
                    Output:board
    """

    print("  {one}  |  {two}  |  {three} \n -------------\n  {four}  |  {five}  |  {six} \n -------------\n  {seven}  |  {eight}  |  {nine}".format(one=board[0],two=board[1],three=board[2],four=board[3],five=board[4],six=board[5],seven=board[6],eight=board[7],nine=board[8]))

def clear_board():
    """
                        This function clears the board
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:None
                        Output:Empty board
    """
    for i in range(0,len(board)):
        board[i]=''

def verify_marker(player):
    """
                        This function verifies illegal marker
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:'X' or 'O'
                        Output:'X' or 'O'
    """
    marker = input("Player {} Choose your marker X or O:".format(player))
    marker=marker.upper()
    if marker=='X' or marker=='O':
        pass
    else:
        print("This is not a correct marker")
        marker=verify_marker(player)
    return marker


def remember_marker(rem,marker,player):
    """
                        This function checks whether the current player is not using opponent's marker
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:dictionary,integer,integer
                        Output:True/False
    """

    if rem['Player {}'.format(player)]==marker:
        return True
    else:
        return False

def player_choice(player):
    """
                        This function verifies correct position,marker entered by the user
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:None
                        Output:'X'/'O',integer(0-9),integer(1-2)
    """

    position = int(input("Player {} Enter your position: (1-9) \n".format(player)))
    marker = verify_marker(player)
    return marker,position,player

def place_marker(marker,position,player):
    """
                        This function places the marker in the desired position
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:None
                        Output:Empty board
    """

    board[position - 1] = marker
    return marker,player

def space_check(position):
    """
                        This function checks the desired position is empty or not
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:Integer number (0-9)
                        Output:True/False
    """
    if board[position-1]=='':
        return True
    else:
        return False

def full_board_check():
    """
                        This function checks if all the positions is filled or not
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:None
                        Output:True/False
    """
    if '' in board:
        return True
    else:
        return False

def win_check(marker):
    """
                        This function checks whether the player won or not
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:'X' or 'O'
                        Output:1/0
    """
    l=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
    flag=0
    for i in l:
        for j in i:
            if marker in board[j-1]:
                flag=1
            else:
                flag=0
                break

        if flag == 1:
            return 1
            break
        else:
            pass

def player_input(player):
    """
                        This function takes the user's input
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:integer
                        Output:None
    """
    count=1
    win=0
    player_num=player
    while(count<9):
        if player_num==1:
            if full_board_check()==True:
                marker,position,player=player_choice(2)
                if space_check(position)==True:
                    if remember_marker(rem,marker,player)==True:
                        marker,player=place_marker(marker,position,2)
                        display_board()
                        win=win_check(marker)
                        if win==1:
                            print("Player 2 WON the game")
                            break
                        else:
                            win=0
                            player_num=2
                            count=count+1
                    else:
                        print("This is not your marker\n")
                        player_input(player_num)
                else:
                    print("This position is filled \n")
                    player_input(player_num)
            else:

                print("It's a TIE")

        else:
            if full_board_check()==True:
                marker,position,player=player_choice(1)
                if space_check(position)==True:
                    if remember_marker(rem,marker,player)==True:
                        marker,player=place_marker(marker,position,1)
                        display_board()
                        win=win_check(marker)
                        if win==1:
                            print("Player 1 WON the game")
                            break
                        else:
                            win=0
                            player_num=1
                            count=count+1
                    else:
                        print("This is not your marker \n")
                        player_input(player_num)

                else:
                    print("This position is filled\n")
                    player_input(player_num)
            else:
                print("It's a TIE")

def choose_first(rem):
    """
                        This function randomly chooses which player will go first
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:dictionary
                        Output:Player 1/ Player 2
    """
    a=1
    b=2
    print("Welcome to Tic Tac Toe!!!!\n")
    player = random.randint(a, b)
    print("Player {} will go first \n".format(player))
    marker,position,player=player_choice(player)
    marker,player=place_marker(marker,position,player)

    rem['Player {}'.format(player)] = marker
    if player == 1:
        if marker == 'X':
            rem['Player 2'] = 'O'
        else:
            rem['Player 2'] = 'X'
    else:
        if marker == 'X':
            rem['Player 1'] = 'O'
        else:
            rem['Player 1'] = 'X'

    display_board()
    return player


def replay():
    """
                        This function used restart the game
                        Date:02/02/2020
                        Created By:Alekhyo
                        Input:None
                        Output:Board
    """
    answer='Yes'
    while(answer=='Yes'):
        clear_board()
        player=choose_first(rem)
        player_input(player)
        print("-"*48)
        print("Do you want to play again? Yes or No")
        answer=input()

rem={}
board=['', '', '', '', '', '', '', '', '']
replay()