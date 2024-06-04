#  phyton é totalmente identado
# 1 criar uma classe restaurante usando construtor

class Restaurante:
    restaurantes=[]
    # __init__ => um dos métodos que faz forçada pra ser construído o método construtor
    # self => elemento de identificação, daí o nome e a categoria pertecem a esse objeto a ser criado, self faz referencia aos atributos que fazem parte daquele objeto especificamente
    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False

        Restaurante.restaurantes.append(self)

    # criou método especial que já existe, estamos invocando pra dentro da classe, ele passa a ta disponível pra classe Restaurante
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    # 4 criar um método para listar os restaurantes
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# 2 criação de objetos
restaurante_praca=Restaurante('Praça', 'Gourmet')

restaurante_pizza=Restaurante('Pizza Express', 'Italiana')

# array = list
# restaurantes=[restaurante_praca,restaurante_pizza]

# 3 consumindo os objetos
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))
# print('')

# métodos disponíveis para o objeto restaurante - instância da classe restaurante
#  abre infraestrutra do objeto e atributos presentes = dir
# print(dir(restaurante_praca))
# print('')
#  abre valores presentes = vars

# print(restaurante_praca)
# print(restaurante_pizza)
# print('')

# 5 consumindo o método listar_restaurantes
Restaurante.listar_restaurantes()