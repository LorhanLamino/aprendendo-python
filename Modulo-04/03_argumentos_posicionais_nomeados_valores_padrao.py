
def cadastrar_produto(nome: str,
                      preco: float,
                      estoque: int
                      ) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R${preco:.2f}")
    print(f"Estoque: {estoque} unidades")

#Argumento posicional
cadastrar_produto("Teclado",150.0,20)
#nesse modo a ordem dos argumentos importa

#Argumentos Nomeados
cadastrar_produto(
    nome = "Teclado",
    preco= 200.00,
    estoque=30
)
#nesse modo a ordem nao importa
#Obs:. Posso ter primeiro posicionado e depois nomeado, mas se nomear nao posso mais ter posicionado

#Parametros com valores padrão
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

cadastrar_produto("Fone de Ouvido", 300.00, ativo=False)
#Neste caso o valor padrao seria o True, caso eu n digite o parametro ele ira me mostrar o valor True e estoque como 0
#Todo parametro com valor precisa estar depois dos parametros sem valor