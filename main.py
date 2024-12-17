import os


lista = []
os.system('cls')
while True:
    print('Selecione uma opção')
    opcao = input('[I] Inserir, [A] Apagar, [L] Listar: ').upper()

    if opcao == 'I':
        try:
            valor = input('Oque voce quer adicionar na lista?')
            if valor in lista:
                print('não pode')
            else:
                lista.append(valor)
        except Exception() as e:
            print(e)

    elif opcao == 'A':
        try:
            indice_str = input('Insira o indice doque voce quer remover da lista: ')
            indice = int(indice_str)
            del lista[indice +1]
        except:
            print('algo deu errado')

    elif opcao == 'L':
        if len(lista) == 0:
            print('nada para listar')
        else:
            for i, valor in enumerate(lista):
                print(i +1,valor)

    else:
        print('por favor, selecione uma opção existente.')