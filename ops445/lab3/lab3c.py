#!/usr/bin/env python3

# Author ID: upandey3@myseneca.ca

def operate(number1, number2, operator):
    # Function to perform operations based on the operator
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == '__main__':
    # Testing the operate function
    print(operate(10, 5, 'add'))      # Expected output: 15
    print(operate(10, 5, 'subtract')) # Expected output: 5
    print(operate(10, 5, 'multiply')) # Expected output: 50
    print(operate(10, 5, 'divide'))   # Expected output: Error message
