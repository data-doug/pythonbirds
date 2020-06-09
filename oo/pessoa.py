class Pessoa:

    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return "Olá"

if __name__ == '__main__':
    douglas = Pessoa(nome="Douglas")
    edson = Pessoa(douglas, nome="Edson")

    for filho in edson.filhos:
        print(filho.nome)

    edson.sobrenome = "Souza de Almeida"
    print(douglas.__dict__)
    print(edson.__dict__)