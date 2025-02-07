# salario = int(input("Digite o salário: "))
# imposto = 27.
# while imposto > 0.:
#     imposto = input("Digite o imposto ou (s) para sair: ")
#     if not imposto:
#         imposto = 27.
#     elif imposto == 's':
#         print("Saíada realizada com SUCESSO!!!")
#         break
#     else:
#         imposto = float(imposto)
#     print("Valor real: {0}".format(salario - (salario * imposto * 0.01)))


# Sem gambiarra
salario = float(input("Digite o salário: "))

while True:
    imposto = input("Digite o imposto ou (s) para sair: ")

    if not imposto:  # Se pressionar Enter, usa o padrão 27%
        imposto = 27.0
    elif imposto.lower() == 's':  # Permite 'S' ou 's' para sair
        print("Saída realizada com SUCESSO!!!")
        break
    else:
        try:
            imposto = float(imposto)
        except ValueError:
            print("Erro: Digite um número válido!")
            continue

    print(f"Valor real: {salario - (salario * imposto * 0.01):.2f}")
