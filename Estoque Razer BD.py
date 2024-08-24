import mysql.connector


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='razer',
)
cursor = conexao.cursor()


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
    print(f"{Colors.GREEN}|{Colors.RESET}                                   B E M    V I N D O    A O {Colors.GREEN}   R A Z E R                                   {Colors.RESET} {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}1{Colors.RESET} - Adicionar produtos {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}2{Colors.RESET} - Listar os produtos adicionados {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}3{Colors.RESET} - Modificar algum produto {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}4{Colors.RESET} - Remover produtos {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}5{Colors.RESET} - Sair {Colors.GREEN}|{Colors.RESET}")
    print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")

def creat():
    nome = str(input('Digite o nome do produto que deseja inserir no estoque: '))
    q = int(input('Digite a quantidade que terá em estoque: '))
    p = float(input('Digite o preço do produto: '))
    comando = f'INSERT INTO produtos (nome_produtos, quantidade_estoque, preco) VALUES ("{nome}", "{q}", "{p}")'
    cursor.execute(comando)
    conexao.commit()


def read():
    try:
        comando = 'SELECT * FROM produtos'
        cursor.execute(comando)
        resultados = cursor.fetchall()
        if resultados:
            print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
            print(f"{Colors.GREEN}|{Colors.RESET} {Colors.GREEN}{'ID':<5} {'Nome':<40} {'Quantidade':<25} {'Preço':<10}{Colors.RESET}")
            print(f"{Colors.GREEN}|{Colors.RESET}============================================================================================================={Colors.GREEN}|{Colors.RESET}")
            for row in resultados:
                print(f"{Colors.GREEN}|{Colors.RESET} {row[0]:<5} {row[1]:<40} {row[2]:<25} R${row[3]:<10}")
        else:
            print(f"{Colors.YELLOW}Nenhum produto encontrado.{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}Erro ao listar os produtos: {e}{Colors.RESET}")


def update():
    op = int(input('Deseja editar o nome(1), quantidade em estoque(2) ou preço(3):  '))
    if op == 1:
        nome = str(input('Digite o nome que deseja editar: '))
        nomen = str(input('Digite o novo nome: '))
        comando = f'UPDATE produtos SET nome_produtos = "{nomen}" WHERE nome_produtos = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
    elif op == 2:
        nome = str(input('Digite o nome do produto que deseja editar a quantidade em estoque: '))
        qn = int(input('Digte a nova quantidade em estoque: '))
        comando = f'UPDATE produtos SET quantidade_estoque = {qn} WHERE nome_produtos = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
    elif op == 3:
        nome = str(input('Digite o nome do produto que deseja editar o preço: '))
        pn = float(input('Digite o novo preço: '))
        comando = f'UPDATE produtos SET preco = {pn} WHERE nome_produtos = "{nome}"'
        cursor.execute(comando)
        conexao.commit()
    else:
        print('Este produto não existe na tabela.')



def delete():
    nome = str(input('Digite o produto que deseja remover do estoque: '))
    comando = f'DELETE FROM produtos WHERE nome_produtos = ("{nome}")'
    cursor.execute(comando)
    conexao.commit()

while True:
    menu()
    op = int(input(f'{Colors.GREEN}| >> {Colors.RESET}'))
    if op == 1:
        creat()
    elif op == 2:
        read()
    elif op == 3:
        update()
    elif op == 4:
        delete()
    elif op == 5:
        print('Você está saindo do estoque, obrigado por usar-lo')
        break
    else:
        print('Digitou algo errado')


cursor.close()
conexao.close()