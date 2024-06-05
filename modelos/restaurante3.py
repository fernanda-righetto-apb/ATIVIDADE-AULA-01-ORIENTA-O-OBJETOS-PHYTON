# 1 criar um decorator @property

class Restaurante:
    restaurantes=[]
   
    def __init__(self,nome,categoria):
        # inicial de cada palavra em maiúsculo - title()
        self._nome=nome.title()
        self._categoria=categoria.upper()
        #  _ -> o underline é um modificador - protege atributo mas não inviabiliza que o modifique externamente
        self._ativo=False

        Restaurante.restaurantes.append(self)

    # criou método especial que já existe, estamos invocando pra dentro da classe, ele passa a ta disponível pra classe Restaurante
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    # 4 criar um método para listar os restaurantes
    
    # chamando/caracterizndo, o método listar restaruante é um método de classe | Método de classe
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')

    # sinalizador
    # site pra símbolos - cool symbols (primeiro link)
    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    # é um método de objeto
    def alternar_estado(self):
        self._ativo=not self._ativo

# 2 criação de objetos
restaurante_praca=Restaurante('praça', 'Gourmet')
restaurante_praca._nome='biqueira'
restaurante_praca.alternar_estado()

restaurante_pizza=Restaurante('pizza express', 'Italiana')





# 5 consumindo o método listar_restaurantes
Restaurante.listar_restaurantes()



