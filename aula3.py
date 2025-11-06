'''
def idade(x):
    if x >= 18:
        print("Pode ser preso")
    else:
        print("Ainda ta safe")

print("Digite a sua idade")

z = int(input())
y = idade(z)
print(y)
'''

'''
def nota(n):
    if n >= 7:
        print("Passou de ano")
    else:
        print("Repetiu o quinto ano")

print("Digite a nota")

a = int(input())
b = nota(a)
print(b)
'''

def temp(x):
    if x >= 25:
        print("Ta quente")
    elif x >= 15:
        print("Ta suave")
    else:
        print("TA FRIO")
    
print("Digite a temperatura ambiente")

y = int(input())
z = temp(y)
print(z)
