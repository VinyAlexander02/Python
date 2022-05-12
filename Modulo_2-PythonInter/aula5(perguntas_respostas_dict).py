""""
Sistemas de perguntas e respostas com dicionário
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 3 x 3',
        'respostas': {'a': '3', 'b': '6', 'c': '9',},
        'resposta_certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 5 x 4',
        'respostas': {'a': '3', 'b': '6', 'c': '20',},
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 10 x 10',
        'respostas': {'a': '10', 'b': '50', 'c': '100',},
        'resposta_certa': 'c'
    },
}

respostas_certas = 0

for pk, pv in perguntas.items():
    print( f'{pk}: {pv["pergunta"]}')
    
    print('Escolha uma das opções abaixo: ')
    for rk, rv in pv['respostas'].items():
        print(f'({rk}): {rv}')
        
    resposta_usuario = input('Digite sua resposta: ')
    
    if resposta_usuario == pv['resposta_certa']:
        print('Você Acertou. Parabéns!')
        respostas_certas += 1
    else: 
        print('Você errou!')
    print()
    
qtde_perguntas = len(perguntas)
porcentagem_acerto =  respostas_certas / qtde_perguntas * 100
print(f'A sua porcentagem de acertos é de {porcentagem_acerto:.2f}%')