# IF
nota = 7

if nota >= 9:
    print("Excelente")
elif nota >= 6:
    print("Aprovado")
else:
    print("Reprovado")

# IF com operadores logicos
idade = 20
tem_ingresso = True
esta_bloqueado = False

if idade >= 18 and tem_ingresso and not esta_bloqueado:
    print("Pode entrar")
elif idade >= 18 or tem_ingresso:
    print("Precisa verificar os dados")
else:
    print("Não pode entrar")

# Match Case
dia = 2

match dia:
    case 1:
        print("Segunda-feira")
    case 2:
        print("Terça-feira")
    case 3:
        print("Quarta-feira")
    case _:
        print("Outro dia")