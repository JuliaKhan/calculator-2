"""CLI application for a prefix-notation calculator.

Quit:       'q' or 'quit' exits the application
Add:        '+ num1 num2 ...' prints num1 + num2 + ...
Subtract:   '- num1 num2' prints num1 - num2
Multiply:   '* num1 num2 ...' prints num1 * num2 * ...
Divide:     '/ num1 num2' prints num1 / num2
Square:     'square num1' prints num1 ** 2
Cube:       'cube num1' prints num1 ** 3
Power:      'power num1 num2' prints num1 ** num2
Modulus:    'mod num1 num2' prints num1 % num2
"""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce    #for iterating + and * later

while True:                                     #begins REPL
    user_input = input("Enter your equation. ") #eg input:  + 1 2
    tokens = user_input.split(' ')              #tokenized: ['+', '1', '2']

    if tokens[0] == 'q' or tokens[0] == 'quit': #exit conditions
        print("Exiting calculator.")
        break

    elif tokens[0] == '+':  #checks first item of tokens for operation
        try:                #exception handling for non-float inputs
            operands = []   
            for num in tokens[1:]:
                operands.append(float(num)) #operands is a list of floats
            print(functools.reduce(add,operands)) #iterates the add function
        except:
            print("invalid operation")

    elif tokens[0] == '-':
        try:
            print(subtract(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")

    elif tokens[0] == '*':
        try:
            operands = []
            for num in tokens[1:]:
                operands.append(float(num))
            print(functools.reduce(multiply,operands))
        except:
            print("invalid operation")
    
    elif tokens[0] == '/':
        try:
            print(divide(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")

    elif tokens[0] == 'square':
        try:
            print(square(float(tokens[1])))
        except:
            print("invalid operation")

    elif tokens[0] == 'cube':
        try:
            print(cube(float(tokens[1])))
        except:
            print("invalid operation")

    elif tokens[0] == 'power':
        try:
            print(power(float(tokens[1]),float(tokens[2])))
        except:
            print("invalid operation")
    
    elif tokens[0] == 'mod':
        try:
            print(mod(float(tokens[1]),float (tokens[2])))
        except:
            print("invalid operation")

    else: print("invalid operation")  #exception handling for invalid operation
