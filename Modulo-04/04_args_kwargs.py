# *args

def calcular_total_modo_raiz(
        valor1: float,
        valor2: float,
        valor3: float
) -> float:
    return valor1 + valor2 + valor3

total = calcular_total_modo_raiz(89.90, 200.0, 510.0)

print(total)

def calcular_total_(*valores) -> float:
    print(valores)
    return sum(valores)

total2 = calcular_total_(89.90, 200.0, 510.0, 10.0, 14.80, 56.20)
print(f"{total2:.2f}")
#chamamos de args pois reune os argumentos posicionais em formato de uma tupla

def calcular_total_pedido(*valores: float) -> float:
    #total = 0
    print(valores)
    # for valor in valores:
    #     total += valor

    return sum(valores)

total3 = calcular_total_pedido(
    120.0,
    89.90,
    45.50,
    199.90
)

print(f"Total do pedido: {total3:.2f}")

#parametros normais + *args
def registrar_pedido(
        numero_pedido: int,
        *produtos: str
) -> None:
    print(f"Pedido # {numero_pedido}")

    for produto in produtos:
        print(f"- {produto}")

registrar_pedido(
    1025,
    "Notebook",
    "Mouse",
    "Teclado"
)

# **kwargs

def cadastrar_documento(**dados)-> None:
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

cadastrar_documento(
    nome = "Lorhan",
    email = "lorhan-lamino@teste.com",
    cidade = "Santa Cruz"
)

# o args gera um tupla enquanto o kwargs gera um dicionario

#Parametros normais + kwargs

def cadastrar_cliente2(
        nome: str,
        email: str,
        **dados_adicionais
) -> None:
    print(f"Nome: {nome}")
    print(f"Email: {email}")

    for k, v in dados_adicionais.items():
        print(f"{k}: {v}")

cadastrar_cliente2(
    nome = "Lorhan",
    email = "lorhan-lamino@teste.com",
    cidade = "Santa Cruz",
    estado = "SP",
    profissao = "Analista de Dados"
)

# args e kwargs juntos

def registar_venda(
        cliente: str,
        *produtos: str,
        **dados_adicionais: str
) -> None:
    print(f"Cliente: {cliente}")

    print("\nProdutos")
    for produto in produtos:
        print(f"- {produto}")

    print("\nInformaçoes da Venda")
    for k, v in dados_adicionais.items():
        print(f"{k}: {v}")

registar_venda(
    "Lorhan",
    "Notebook",
    "Telefone",
    forma_pagamento = "pix",
    vendedor = "Zezin do Pneu",
    venda = True
)