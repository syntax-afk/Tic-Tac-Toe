import math

board = [" " for _ in range(9)]

def print_board(): #prints the tic tac toe board
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(b): #winning combinations
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins: #checking if any winning combination is met 
        a,b1,c = combo
        if b[a] == b[b1] == b[c] and b[a] != " ":
            return b[a]
  
    if " " not in b: #if there are no empty spaces and no winner, it's a draw
        return "draw"

    return None


def minimax(b, depth, is_maximizing): # returns the best score using minimax for the current board state
    result = check_winner(b)

    if result == "O":# ai wins → highest score
        return 1
    elif result == "X":# player wins → lowest score
        return -1
    elif result == "draw":
        return 0

    if is_maximizing:  # AI tries to maximize the score
        best_score = -math.inf  # start from lowest possible value

        for i in range(9): # check all board positions
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)  # simulate opponent's move
                b[i] = " "
                best_score = max(score, best_score)

        return best_score  

    else:
        best_score = math.inf #will try to minimize the score for player

        for i in range(9): 
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best_score = min(score, best_score)

        return best_score


def ai_move():
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def player_move():
    while True:
        try:
            choice = int(input("Choose position (1-9): ")) - 1
            if board[choice] == " ":
                board[choice] = "X"
                break
            else:
                print("Spot taken!")
        except:
            print("Invalid input!")


def main():
    print("Tic Tac Toe")
    print("You are X | AI is O")

    while True:
        print_board()
        player_move()

        if check_winner(board):
            break

        ai_move()

        if check_winner(board):
            break

    print_board()
    result = check_winner(board)

    if result == "X":
        print("You win!")
    elif result == "O":
        print("AI wins!")
    else:
        print("It's a draw!")


main()