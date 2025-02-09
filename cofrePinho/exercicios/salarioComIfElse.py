salario = int(input("Digite o seu Salário: "))
imposto = input("Digite o valor em % (Ex: 27.5): ")
if imposto == "":
    imposto = 27.5
else:
    imposto = float(imposto)

print(f"O valor real do seu salário é: {salario - (salario * (imposto * 0.01))}")