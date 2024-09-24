import os

os.system('cls')

p = float(input('Digite o peso: '))
a = float(input('Digite a altura: '))


imc = p / a ** 2

print(f'IMC: {imc}')

if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Sobrepeso')
else:
    print('Obesidade')
    
