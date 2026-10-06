#Try/Except
#Existem varias formas de utilizar o except
#Testando se caso o usuario digitasse o numero da nota como texto, por exemplo, dois.
try:
    nota_prova = int(input("Digite a nota da prova:"))
    print(nota_prova)
    print(type(nota_prova))
#except:    
    #print("Algo está errado!")
#except ValueError:
    #print("Voce precisa digitar um numero inteiro!")
except Exception as e:
    print (e)