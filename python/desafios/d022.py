name = input('Seu nome: ').strip()
print('Em maiúsculo: {}'.format(name.upper()))
print('Em minúsculo: {}'.format(name.lower()))
print('Quantidade de letras: {}'.format(len(name) - name.count(' ')))
print('Quantidade de letras do primeiro nome: {}'.format(len(name.split()[0])))