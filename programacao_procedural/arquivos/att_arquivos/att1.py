for _ in range(10):
    name = input('Digite seu nome: ')
    with open('abc.txt', 'a+') as file:
        file.write(name)
        file.seek(0)
        print(file.read(), sep=' ')