#!/usr/bin/env python3

import operator
import random
def eat_my_carat(a, b):
    return a ** b

def talk(a, b):
    return "hi student"

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': eat_my_carat,
    'talk': talk,
    
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            if token == 'random':
                token = random.randint(0,1000)
            else:
                token = int(token)
            
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print("Result: ", result)

if __name__ == '__main__':
    main()
