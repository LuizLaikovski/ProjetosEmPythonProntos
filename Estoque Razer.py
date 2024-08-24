#deixa apenas os caracteres na string
def corrigir_entrada(texto_corrigir):
    produto = ''
    for caractere in texto_corrigir:
        if caractere.isalpha() or caractere.isspace():
            produto += caractere
    return produto


#retira os caracteres e caracteres especias de uma string, deixando apenas os numeros
def filtrar_numeros(string):
    numeros = ''.join(char for char in string if char.isdigit())
    return numeros


#Para adicionar as cores no console
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'



# Menu principal
def menu():
    print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} B E M V I N D O A O {Colors.GREEN}R A Z E R{Colors.RESET} {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}1{Colors.RESET} - Adicionar produtos {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}2{Colors.RESET} - Listar os produtos adicionados {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}3{Colors.RESET} - Remover produto {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}4{Colors.RESET} - Modificar o preço do produto {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}5{Colors.RESET} - Sair {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")



# Adicionar o produto
def add_prod(estoque):
    produto = str(input(f"{Colors.GREEN}|{Colors.RESET} Digite o nome do produto: "))
    produto = corrigir_entrada(produto)
    if produto == '':
        print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou números, digite apenas letras")
    else:
        print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
        quantidade = str(input(f"{Colors.GREEN}|{Colors.RESET} Digite a quantidade em estoque: "))
        quantidade = filtrar_numeros(quantidade)
        if quantidade == '':
            print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou caracteres, digite apenas numeros")
        else:
            quantidade = int(quantidade)
            print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
            preco = str(input(f"{Colors.GREEN}|{Colors.RESET} Digite o preço do produto: "))
            preco = filtrar_numeros(preco)
            if preco == '':
                print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou caracteres, digite apenas numeros")
            else:
                preco = int(preco)
                if produto in estoque: #verifica se o produto ja existe e atualiza sua quantidade
                    estoque[produto]["quantidade"] += quantidade
                else:
                    estoque[produto] = {"quantidade": quantidade, "preco": preco}



# Listar produtos
def listar_p(estoque):
    if not estoque:
        print(F"{Colors.GREEN}|{Colors.RESET} Nenhum produto no estoque.")
    else:
        for produto, info in estoque.items():
            print(f"{Colors.GREEN}| Produto{Colors.RESET}: {produto} | {Colors.GREEN}Quantidade{Colors.RESET}: {info['quantidade']} | {Colors.GREEN}Preço{Colors.RESET}: R${info['preco']:.2f}")
            #print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")



# Remover produtos
def excluir_p(estoque):
    produto = str(input(f"{Colors.GREEN}|{Colors.RESET} Digite o nome do produto que deseja remover: "))
    produto = corrigir_entrada(produto)
    if produto == '':
        print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou números, digite apenas letras")
    else:
        print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
        if produto in estoque:
            quantidade_remover = str(input(f"{Colors.GREEN}|{Colors.RESET} Digite a quantidade que deseja remover (0 ou um numero negativo para remover todas as unidades): "))
            quantidade_remover = filtrar_numeros(quantidade_remover)
            if quantidade_remover == '':
                print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou carcateres, digite apenas números")
            else:
                quantidade_remover = int(quantidade_remover)
                print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
                if quantidade_remover < 0:
                    del estoque[produto]
                    print(f"{Colors.GREEN}|{Colors.RESET} Todas as unidades do produto '{produto}' foram removidas.")
                elif quantidade_remover > estoque[produto]["quantidade"]:
                    del estoque[produto]
                    print(f"{Colors.GREEN}|{Colors.RESET} Todas as unidades do produto '{produto}' foram removidas.")
                elif quantidade_remover == estoque[produto]['quantidade']:
                    #estoque[produto]["quantidade"] -= quantidade_remover
                    del estoque[produto]
                    print(f"{Colors.GREEN}|{Colors.RESET} {quantidade_remover} unidades do produto '{produto}' foram removidas.")
                elif quantidade_remover > 0 and quantidade_remover < estoque[produto]['quantidade']: 
                    print('FUNCIONOU')
                    estoque[produto]["quantidade"] -= quantidade_remover
                else:
                    print(F"{Colors.GREEN}|{Colors.RESET} Produto não encontrado no estoque.")


        
# Modificar o preço do produto
def edit_preco(estoque):
    produto = input(F"{Colors.GREEN}|{Colors.RESET} Digite o nome do produto que deseja modificar o preço: ")
    produto = corrigir_entrada(produto)
    if produto == '':
        print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou números, digite apenas letras")
    else:
        print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
        if produto in estoque:
            novo_preco = str(input(F"{Colors.GREEN}|{Colors.RESET} Digite o novo preço: "))
            novo_preco = filtrar_numeros(novo_preco)
            if novo_preco == '':
                print(f"{Colors.GREEN}|{Colors.RESET} Você digitou caracteres especiais ou carcateres, digite apenas números")
            else:
                novo_preco = float(novo_preco)
                print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
                estoque[produto]["preco"] = novo_preco
                print(f"{Colors.GREEN}|{Colors.RESET} O preço do produto '{produto}' foi atualizado para R${novo_preco:.2f}.")
        else:
            print(F"{Colors.GREEN}|{Colors.RESET} Produto não encontrado no estoque.")



# Executa o programa
def controle_estoque():
    estoque = {}
    while True:
        menu()
        opcao = str(input(F"{Colors.GREEN}|{Colors.RESET} Escolha uma opção: "))
        print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")

        if opcao == "1":
            add_prod(estoque)
        elif opcao == "2":
            listar_p(estoque)
        elif opcao == "3":
            excluir_p(estoque)
        elif opcao == "4":
            edit_preco(estoque)
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("| Opção inválida. Escolha novamente.")
controle_estoque()
