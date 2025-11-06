'''
def area(r):
    resultado = (r**2) * 3.14
    return resultado

print("Digite um valor de raio para calcularmos a área do círculo")

x = int(input())
y = area(x)
print(y)
'''

'''
def aplicar_desconto(preco,  percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

print(aplicar_desconto(300, 30))
'''

def conversao(C):
    resultado = (1.8 * C) + 32
    return resultado

print("Digite o valor da temperatura em Celsius")
x = int(input())
y = conversao(x)
print(y)

