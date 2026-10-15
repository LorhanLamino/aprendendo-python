#funçoes e procedimentos

# def imprimir_itens(lista):
#     for item in lista:
#         print(item)

# l1 = [1,2,3,4,5,6]
# imprimir_itens(l1)

# l2 = ["Lorhan","Kamile","Daniele","Anderson"]
# imprimir_itens(l2)

# l3 = [12, "Lorhan", 2026.2, True]
# imprimir_itens(l3)

def mostrar_inico_processamento(numero_pedido: int) -> None:
    """"
    Mostra na tela o inicio de processamento de um pedido.
    """
    print(f"iniciando processamento do pedido #{numero_pedido}...")

def calcular_total(preco: float, 
                   quantidade: int, 
                   desconto: float
                   ) -> float:
    """"
    Calcula o valor final de um item após aplicar um desconto.
    Args:
        preco: preco unitario do produto
        quantidade: quantidade comprada
        desconto: percentual de desconto em formato decimal

    Returns:
        Valor final da compra   
    """
    subtotal: float = preco * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto
    return total

def registrar_processamento(
        numero_pedido: int,
        valor: float
        ) -> None:
    """"
    Exibe uma confirmação do processamento pedido.

    Args:
        numero_predido: Identificador do pedido (id)
        valor: Valor final do produto
    """

    print(f"Pedido #{numero_pedido} processado com o valor de R${valor:.2f}")


numero_pedido: int = 1058
mostrar_inico_processamento(numero_pedido)

valor_final = calcular_total(
    preco=89.90,
    quantidade=3,
    desconto=0.10
)

registrar_processamento(numero_pedido, valor_final)