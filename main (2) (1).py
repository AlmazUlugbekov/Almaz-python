from os import system

first= round(int(input('Write the first number: ')))
second = round(int(input('Write the second number: ')))
operators = input('Choose operations: \n'
                  "1 - Multiplication \n"
                  "2 - Divide \n"
                  "3 - Substraction \n"
                  "4 - Addition \n"
                 "Write the operation: ")
if(operators == '4'):
    clearTerminal = system('cls')
    sum = first + second
    print(f'{first} + {second} = {sum}')
elif(operators == '3'):
    clearTerminal = system('cls')
    sum = first - second
    print(f'{first} - {second} = {sum}')
elif(operators == '1'):
    clearTerminal = system('cls')
    sum = first * second
    print(f'{first} * {second} = {sum}')
elif(operators == '2'):
    clearTerminal = system('cls')
    sum = first / second
    print(f'{first} / {second} = {sum}')
else:
    clearTerminal = system('cls')
    print('Error')
