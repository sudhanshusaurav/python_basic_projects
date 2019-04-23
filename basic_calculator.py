import re

run = True
result = 0


def user_input():
    global result
    global run
    if result == 0:
        user_input = input("Enter an expression.")
        exp = user_input
    else:
        user_input = input()
        exp = str(result)+user_input

    if user_input == 'q':
        print('quit')
        run = False
    else:
        exp = re.sub("[A-Z a-z,]","",exp)
        calculate(exp)


def calculate(exp):
    global result
    result = eval(exp)
    output(result)


def output(res):
    print(res,end="")
    user_input()


while run:
    print("Enter 'q' to quit the calculator.")
    user_input()


