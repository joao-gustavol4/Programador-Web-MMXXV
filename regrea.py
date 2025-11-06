soma = 0
n = 0
while True: 
    entrada = int(input(f'Digite o {n + 1} valor '))
    if entrada == 0:
        break
    
    else:
        soma += entrada
        n += 1

resultadoacb = soma/n
print(resultadoacb)
print(soma)
print(n)

    