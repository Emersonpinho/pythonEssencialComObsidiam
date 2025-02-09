impostos = ['MEI', 'Simples']

for imposto in impostos:
    if imposto.startswith("S"):
       continue

    print(imposto)