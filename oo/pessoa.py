class Pessoa:
    olhos = 3

    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar(self):
        return "Olá"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos: {cls.olhos}'

if __name__ == '__main__':
    douglas = Pessoa(nome="Douglas")
    edson = Pessoa(douglas, nome="Edson")

    for filho in edson.filhos:
        print(filho.nome)

    edson.sobrenome = "Souza de Almeida"
    print(douglas.__dict__)
    print(edson.__dict__)

    print(douglas.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())