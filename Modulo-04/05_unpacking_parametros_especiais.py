# print("\nInformações de Venda")
# for k, v in dados_adicionais.items():
#     print(f"{k.capitalize()}: {v}")


def cadastrar_produto(
        nome: str,
        preco: float,
        estoque: int =0,
        ativo: bool = True
) -> None:
        print(f"Produto: {nome}")
        print(f"Preço: R${preco:.2f}")
        print(f"Estoque: {estoque}")
        print(f"Ativo: {ativo}")

# Unpacking (desempacotar) com *
produto = ["Teclado", 4500.00, 120]
cadastrar_produto(*produto)
#lembre-se que a posição dos arguemtos importam

# Unpacking (desempacotar) com **
produtos3 = {
        "nome": "Mouse",
        "preco": 4500,
        "estoque": 8
}
cadastrar_produto(**produtos3)
#desse formato posso desempacotar meu dicionario

#Obs: apenas 1 * asteristico desempacota argumento posicional e 2 * desempacote argumentos nomeados
#Para desempacotar dicionario, as chaves dele precisam ter os mesmos nomes dos parametros


# / - Parametros somente posicionais
def calcular_desconto(
                preco: float,
                desconto: float,
                /
) -> float:
        return preco - (preco * desconto)
#quando coloco barra tudo que aparece antes deve ser passado como argumento posicional

def registrar_vendas2(
          codigo : int,
          /,
          cliente: str      
) -> None:
        print(codigo)
        print(cliente)

#Nessa função o codigo é obrigatoriamente posicional enquanto cliente pode ser posicional ou nomeado
registrar_vendas2(500,"Lorhan") 
#ou
registrar_vendas2(500,cliente="Lorhan")

# * - Parametros somente nomeados
def exportar_relatorio(
                nome_arq: str,
                *,
                incluir_cabecario: bool,
                compactar: bool
) -> None:
        print(nome_arq)
        print(incluir_cabecario)
        print(compactar)

exportar_relatorio("vendas.csv", incluir_cabecario=True, compactar=True)
#Tudo que vem depois do asteristico é preciso ser nomeado

#Obs: podemos ter tanto a / quanto o * juntos nos argumentos de uma função.
