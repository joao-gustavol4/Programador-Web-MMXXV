def saudacao(nome): #Para criar uma função = primeiro digitamos "def" ,depois o nome da função
                    #e em seguida usamos () - que pode ter ou nao ter variaveis
                    #Outro nomeclatura para a variavel aqui é chamada de parametro
    print(f"Eae!, {nome}!") #"print" é o comando que imprime algo no terminal.

saudacao("João") #Aqui esta um exemplo sobre como ativar/chamar uma função = colocamos o nome dela
                #e fornecemos oque ela precisa.

def soma(a, b):
    resultado = a + b
    return resultado

total = soma(6, 9)
print(total)