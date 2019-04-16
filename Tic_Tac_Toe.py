
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
flag = 0
index = []

print(index)

while flag!=2:

    # function returns the location coordinates to mark.
    def location(x):
        global board

        if x == 1:
            return 0, 0
        elif x == 2:
            return 0, 1
        elif x == 3:
            return 0, 2
        elif x == 4:
            return 1, 0
        elif x == 5:
            return 1, 1
        elif x == 6:
            return 1, 2
        elif x == 7:
            return 2, 0
        elif x == 8:
            return 2, 1
        elif x == 9:
            return 2, 2

    # function displays the updated board after every mark.
    def print_board(i, j, k):
        global board
        board[i][j]= k
        for i in range(3):
            print("\n")
            for j in range(3):
                print(board[i][j], end=" ")


    # function checks the winner after every mark.
    def check_Winner():
        global board
        global flag
        if board[0][0] == board[0][1] == board[0][2] != '_':
            print('\n',board[0][0] + " Won")
            replay()
        elif board[1][0] == board[1][1] == board[1][2] != '_':
            print('\n',board[1][0] + " won")
            replay()
        elif board[2][0] == board[2][1] == board[2][2] != '_':
            print('\n',board[2][0] + " won")
            replay()
        elif board[0][0] == board[1][0] == board[2][0] != '_':
            print('\n',board[0][0] + " won")
            replay()
        elif board[0][1] == board[1][1] == board[2][1] != '_':
            print('\n',board[0][1] + " won")
            replay()
        elif board[0][2] == board[1][2] == board[2][2] != '_':
            print('\n',board[0][2] + " won")
            replay()
        elif board[0][0] == board[1][1] == board[2][2] != '_':
            print('\n',board[0][0] + " won")
            replay()
        elif board[0][2] == board[1][1] == board[2][0] != '_':
            print('\n',board[0][2] + " won")
            replay()
        else:
            if no_of_blank_space() != 0:
                return
            else:
                print("\n The math was draw!!!")
                replay()


    # function returns the no of unmarked positions.
    def no_of_blank_space():
        space = 0
        for row in board:
            for col in row:
                if col == '_':
                    space += 1
        return space


    def user_input(mark):
        global index
        str = """\nEnter the location number to mark {0}
                1 2 3
                4 5 6
                7 8 9"""
        l = int(input(str.format(mark)))
        if l in index:
            l = int(input("\n location is used. Enter another location."))
        else:
            index.append(l)

        i, j = location(l)

        print_board(i, j, k=mark)
        check_Winner()


    def player1():
        user_input('O')
        global flag
        flag =1

    def player2():
        user_input('X')
        global flag
        flag = 0


    # function asks user to replay or exit.
    def replay():
        r= input("Do you want to play again? y/n").lower()
        if r=='n':
            exit()
        elif r=='y':
            global flag, index, board
            board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
            flag = 0
            index = []
            player1()

        else:
            r= input("Wrong input. Please re-enter").lower()


    if flag==0:
        player1()
    elif flag==1:
        player2()
