nome = str(input('Digite o seu nome completo: ')).strip()
print('Prazer em te conhecer {}.'.format(nome))
nome = nome.split()
print('O seu primero nome é {}.'.format(nome[0]))
print('O seu ultimo nome é: {}.'.format(nome[len(nome)-1]))