city = str(input('Insira o nome da cidade: '))
divide = city.lower().split()
have = 'santo' in divide[0]
print(have)