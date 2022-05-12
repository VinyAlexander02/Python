clientes = {
    'c1': {
        'nome': 'Vinícius',
        'sobrenome': 'Moreira',
    },
    'c2': {
        'nome': 'Mariana',
        'sobrenome': 'Ribeiro',
    },
    'c3': {
        'nome': 'Silvana',
        'sobrenome': 'Moreira',
    },
}



for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t {dados_k} = {dados_v}')