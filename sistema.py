print('{:=^48}'.format(' Eletronic | Loja de eletrônicos '))

estoque = []

while True:
    print('''
Menu de opções:
[1] Adicionar produto
[2] Atualizar produto
[3] Remover produto
[4] Visualizar estoque
[5] Sair do sistema''')
    opcao = input('Selecione a opção desejada: ')

    if opcao == '1':
        nome = str(input('Nome do produto: '))
        valor = float(input('Preço: R$'))
        quantidade_estoque = int(input('Quantidade em estoque: '))
        estoque.append({"nome": nome,
                        "valor": valor,
                        "quantidade_estoque": quantidade_estoque})
        print(f'Produto {nome} adicionado ao estoque')

    elif opcao == '2':
        nome = input('Digite o nome do produto para ser \
atualizado: ')
        for produto in estoque:
            if produto["nome"] == nome:
                valor = float(input('Digite o novo preço: R$'))
                quantidade_estoque = int(input('Nova quantidade no estoque: '))
                produto["valor"] = valor
                produto["quantidade_estoque"] = quantidade_estoque
                print(f'Produto {nome} atualizado.')
                break
        else:
            print(f'Produto {nome} não encontrado no estoque.')

    elif opcao == '3':
        nome = input('Digite o nome do produto para removê-lo: ')
        for produto in estoque:
            if produto["nome"] == nome:
                estoque.remove(produto)
                print(f'Produto {nome} removido do estoque.')
                break
        else:
            print(f'Produto {nome} em falta no estoque. Tente novamente!')

    elif opcao == '4':
        print('{:=^48}'.format('Estoque:'))
        for produto in estoque:
            print(f"Produto: {produto['nome']}\n\
Preço: R${produto['valor']}\n\
Quantidade em estoque: {produto['quantidade_estoque']}")
        print('{:=^48}'.format('=='))

    elif opcao == '5':
        print('Você saiu do sistema. Até logo...')
        break
    else:
        print('Opção inválida. Tente novamente.')
    
