import os

os.system('cls')
num = float (input('Digite um número: '))

# if num >= 1:
#     print(f'O número {num} é positivo')
# elif num == 0:
#     print(f'O número {num} não pode ser aceito')
# else:
#     print(f'O número {num} é negativo')

if num != 0:
    if num > 0:
        print(f'{num} Positivo')
    else:
        print(f'{num} Negativo')   
else:
    print('Não digite zero') 
    

