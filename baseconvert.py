# This code converts a number from one base to another.
# It works for any bases between 2 and 36. 
# The digits for 10 through 35 are represented by the lowercase alfabet,
# where a = 10, b = 11, ... , y = 34, z = 35
# If you want to work with higher bases than 36 you will have to add digits to the end of the "digits" string (1:st row in conv)
# The function conv takes three parameters
# The first is the number you what to convert (str)
# The second is the base of that number (int)
# The third is the base you what to convert to (int)
# Below the function is an example script of how to run the function in the terminal with a simple user interface 

def conv(number:str,inputb:int,outputb:int):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if number == '0':
        return '0'
    
    number10 = 0
    for i,char in enumerate(number):
        for j, digit in enumerate(digits):
            if char == digit:
                number10 +=  j * (inputb ** (len(number)-i-1))
                break

    output = ''
    while number10 > 0:
        for i,digit in enumerate(digits):
            if number10 % outputb == i:
                output = digit + output
                break     
        number10 = int((number10 - (number10 % outputb))/outputb)
    
    return output

# user inteface
import os

while True:
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    number = input('convert: ')
    inputb = int(input('from: '))
    outputb = int(input('to: '))
    print(conv(number,inputb,outputb))
    input()
    