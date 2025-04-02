

class Pessoa:
    ano = 2025

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('hey')

# p1 = Pessoa('Joao', 53)
Pessoa.metodo_de_classe()
