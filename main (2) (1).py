from os import system

a = round(int(input('Write the first number: ')))
b = round(int(input('Write the second number: ')))
operators = input('Choose operations: \n'
                  "1 - Multiplication \n"
                  "2 - Divide \n"
                  "3 - Substraction \n"
                  "4 - Addition \n"
                 "Write the operation: ")
if(operators == '4'):
    _ = system('cls')
    sum = a + b
    print(f'{a} + {b} = {sum}')
elif(operators == '3'):
    _ = system('cls')
    sum = a - b
    print(f'{a} - {b} = {sum}')
elif(operators == '1'):
    _ = system('cls')
    sum = a * b
    print(f'{a} * {b} = {sum}')
elif(operators == '2'):
    _ = system('cls')
    sum = a / b
    print(f'{a} / {b} = {sum}')
else:
    _ = system('cls')
    print('Error')
