num = int(input('Digite um número: '))
cont = 0 # contador
while cont <= 10: # enquanto o contador for menor ou igual a 10
    print(f'{num} x {cont} = {num * cont}') # numero que o usuário digito vezes o contador
    cont += 1 # contador recebe + 1 para não ficar em loop infinito