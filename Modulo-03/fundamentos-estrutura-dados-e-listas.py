#Fundamentos das Estruturas de Dados e listas
#Coleções

#Lista
#Ordenada e mutável; permite itens repetidos.
frutas = ["maçã", "banana", "uva"]
frutas.append("laranja") #Adiciona outro valor ao fim da lista
print(frutas)

#Tuplas
#Ordenada e imutável; permite itens repetidos.
coordenada = (10, 20)
print(coordenada[0])

#Conjunto ou Set
#Não mantém uma ordem fixa e não permite itens repetidos.
numeros = {1, 2, 2, 3}
print(numeros)

#Dicionario
#Armazena pares de chave e valor; as chaves são únicas.
pessoa = {"nome": "Ana", "idade": 30}
print(pessoa["nome"])
