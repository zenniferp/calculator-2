"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
""" repeat forever:
        read input
        tokenize input
            if the first token is q:
                quit
            else:
                if the first index of the list is add:
                    call the add fn w the index 1 and index 2
                elif the first index = sub:
                    call the sub fn and do index 1 - index 2
                elif the first index = mul:
                    call the muliply fn using index 1 and index 2"""
def calculate_numbers():

    while True:        
        answer = input("Enter your string > ")
        tokens = answer.split(' ')
        operator = tokens[0]
        num1 = float(tokens[1])
        num2 = float(tokens[2])
        if operator == 'q':
            print("Game over")
            break
        else:
            if operator == 'add':
                add(num1, num2)
            elif operator == 'sub':
                subtract(num1, num2)


calculate_numbers()