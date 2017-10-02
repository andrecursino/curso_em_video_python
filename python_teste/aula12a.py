nome = str(input('Qual seu nome? '))
if nome == 'André':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome ébom popular no Brasil.')
else:
    print('Seu nome é bom normal.')
print('Tenha um bom dia, {}.'.format(nome))