import filmes
import series
import os

def menu():
    while True:
        os.system('cls')
        print('1. Procurar filme')
        print('2. Procurar serie')
        print('0. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nome_do_filme = input('Digite o nome do filme:')
            filmes.procurar_filme(nome_do_filme)
            input(f'Pressione Enter para continuar...\n')
        elif opcao == '2':
            nome_da_serie = input('Digite o nome da serie:')
            series.procurar_series(nome_da_serie)
            input(f'Pressione Enter para continuar...\n')
        elif opcao == '0':
            break  
        else:
            print('Opção inválida. Volte ao menu')

if __name__ == "__main__":
    menu()

   





    