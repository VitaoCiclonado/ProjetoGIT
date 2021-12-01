lista_brinquedo = []

def main():

    while True:
        print("\n -----RIR FELIZ BRINQUEDOS----- \n")
        print("")
        print('1 - Cadastrar nome do brinquedo')
        print('2 - Ver a quantidade de estoque')
        print('3 - Retirar um brinquedo do estoque')
        print('0 - Finalizar programa')

        op = int(input("\n Escolha uma opçao: "))

        if op == 1:
            cadastro()
        elif op == 2:
            estoque()
        elif op == 3:
            retirar()
        elif op == 0:
            return 0
       
def cadastro():
    print('\n [CADASTRO DE BRINQUEDO]\n')
    nome = str(input('Digite o nome do brinquedo: '))
    lista_brinquedo.append(nome)
    return 

def estoque():
    print('\n [ESTOQUE DE BRINQUEDO]\n')
    num = len(lista_brinquedo)
    print(f'Há {num} brinquedos no estoque\n')

    for i in range(num):
        print(f'Brinquedo nº{i+1}: {lista_brinquedo[i]}')

def retirar():
    print('\n[RETIRADA DE BRINQUEDO]\n')
    num = len(lista_brinquedo)
    for i in range(num):
        print(f'Brinquedo nº{i+1}: {lista_brinquedo[i]}')

    if num < 1:
        print('Estoque está vazio!')
    else:
        escolha = int(input('\nQual brinquedo será removido? digite um número: '))
        lista_brinquedo.pop(escolha-1)

main()