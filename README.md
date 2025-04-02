# PROGRAMAÇÃO ORIENTADA A OBJETOS

### CLASSE
São moldes para criar novos objetos/instâncias.

### __dict__ e vars
Exibe os valores da instância.

### @classmethod
O @classmethod é útil quando você precisa de um método que altere ou acesse o estado de uma classe, em vez de um método de instância.

```python
@classmethod
def metodo_de_classe(cls):
    print('hey')

Pessoa.metodo_de_classe()
```

### @staticmethod
O uso de @staticmethod é útil quando você tem uma função que realiza alguma operação relacionada à classe, mas que não precisa acessar ou modificar o estado da instância.

```python
class ContaBancaria:
    @staticmethod
    def calcular_juros(saldo, taxa):
        return saldo * taxa

# Chamando o método estático sem precisar de uma instância
juros = ContaBancaria.calcular_juros(1000, 0.05)
```

### @property
O método @property em Python é um decorador que permite definir métodos como propriedades, ou seja, ele permite que você acesse métodos como se fossem atributos, sem precisar chamá-los explicitamente com parênteses.

### @setter
O @setter é usado em conjunto com o @property para definir um método responsável por modificar o valor de um atributo de forma controlada. O @setter permite que você altere a lógica de como o valor de um atributo é definido, garantindo que ele atenda a certas condições antes de ser modificado.

```python
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    @property
    def preco(self):
        # Getter: Retorna o preço
        return self._preco

    @preco.setter
    def preco(self, valor):
        # Setter: Valida se o preço é maior que zero antes de definir
        if valor < 0:
            raise ValueError("O preço não pode ser negativo.")
        self._preco = valor
```

### super()
O método super() em Python é usado para chamar métodos de uma classe base (ou superclasse) de dentro de uma classe derivada (ou subclasse).


### Mixin
Um mixin é geralmente uma classe pequena e especializada que fornece métodos adicionais para outras classes.

### CLASSE ABSTRATA - ABC, abstractmethod
ABC são usadas como contratos para a definição de novas classes.
@abstractmethods são métodos que não tem corpo.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Cachorro(Animal):
    
    def fazer_som(self):
        print("Au Au!")
    
    def mover(self):
        print("Correndo")

# Tentando instanciar a classe Animal causaria erro:
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods fazer_som, mover

# Podemos instanciar a classe Cachorro, que implementa os métodos abstratos:
cachorro = Cachorro()
cachorro.fazer_som()  # Saída: Au Au!
cachorro.mover()      # Saída: Correndo
```

### POLIMORFISMO
Permite que métodos com o mesmo nome se comportem de maneiras diferentes dependendo do objeto que os chama.

### ENUM
A biblioteca enum permite criar classes enumeradas, onde cada item da enumeração é associado a um valor único.

```python
from enum import Enum

class DiaSemana(Enum):
    SEGUNDA = 1
    TERCA = 2
    QUARTA = 3
    QUINTA = 4
    SEXTA = 5
    SABADO = 6
    DOMINGO = 7

# Acessando um valor pelo nome
print(DiaSemana.SEGUNDA)  # Saída: DiaSemana.SEGUNDA

# Acessando o valor associado a um nome
print(DiaSemana.SEGUNDA.value)  # Saída: 1

# Acessando o nome associado a um valor
print(DiaSemana(1))  # Saída: DiaSemana.SEGUNDA
```

### @dataclasses
O módulo dataclasses fornece um decorador e funções para criar métodos como
__init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
usuário.
Em resumo: dataclasses são syntax sugar para criar classes normais.

```python
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 30)
    p2 = Pessoa('Luiz', 30)
    print(p1 == p2)
```
