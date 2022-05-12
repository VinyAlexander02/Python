d1 = {'chave1': 'Vinicius', 'chave2': 'Alexander'}
print(d1, type(d1))

#MOstrando Chave e Valor
d2 = {
    'chave1': 'Valor',
    'chave2': 'Outro Valor',
    'chave3': 'Tupla'
}

for k, v in d2.items():
    print(k, v)