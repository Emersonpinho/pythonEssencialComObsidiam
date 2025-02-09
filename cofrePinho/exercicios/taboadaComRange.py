num = int(input('Digite um número para ver sua taboada: '))
cont = 0
for numero in range(11):
    print(f'{num} X {numero} = {num * cont}')
    cont += 1
