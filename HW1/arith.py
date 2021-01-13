#!/usr/bin/env python

import re
import sys


class Stack:

    def __init__(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]  # last element of stack
        else:
            return None  # stack's empty

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        return self.stack == []


def isNumber(string):
    return bool(re.match(r'-?\d+', string))


def parse(inputStmt):
    oper = {}                   # precedence of each operator
    oper["+"] = 1
    oper["*"] = 2
    oper["-"] = 1
    pfForm = []                 # storing the postfix notation
    operations = Stack()        # storing the operators

    tokens = inputStmt.split()
    if not isNumber(tokens[0]):     # check for invalid entries
        return print("Error: Didn't detect a number at start of input. Detected: ", tokens[0])

    elif not isNumber(tokens[-1]):     # check for invalid entries
        return print("Error: Didn't detect a number at the end of input. Detected: ", tokens[-1])

    else:
        for t in tokens:
            if isNumber(t):
                pfForm.append(t)    # put number onto the postfix list

            else:
                # regulate order of postfix notation when operator is detected
                while (not operations.isEmpty()) and (oper[operations.peek()] >= oper[t]):
                    pfForm.append(operations.pop())
                operations.push(t)

    while (not operations.isEmpty()):
        # put the rest of the operations left into postfix list
        pfForm.append(operations.pop())

    return eval(" ".join(pfForm))


def eval(pfe):
    oper = Stack()
    tokens = pfe.split()

    for tok in tokens:
        if isNumber(tok):
            # if token is a number push it into the operation stack
            oper.push(int(tok))

        else:
            # if token is an operator, pop previous 2 numbers from stack
            num2, num1 = oper.pop(), oper.pop()

            # calculate the 2 numbers popped with operator
            # push calculation back into stack for next operator
            oper.push(calc(tok, num1, num2))

    return oper.pop()


def calc(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "*":
        return num1 * num2
    else:
        return num1 - num2


if __name__ == '__main__':
    for line in sys.stdin:
        print(parse(line))
