# ATIVIDADE AULA 02 ORIENTAÇÃO À OBJETOS

# QUESTÃO 1
class Carro:
    modelo:''
    cor:''
    ano:''

carro_celta = Carro()
carro_celta.modelo = 'Celta'
carro_celta.cor = 'Prata'
carro_celta.ano = '2010'

print(vars(carro_celta))
print('')

# QUESTÃO 2
class Restaurante:
    nome:''
    categoria:''
    ativo:False
    ano_criacao:''
    localidade:''

restaurante_Chef = Restaurante()
restaurante_Chef.nome = 'Chef'
restaurante_Chef.categoria = 'Gourmet'
restaurante_Chef.ano_criacao = '1918'
restaurante_Chef.localidade = 'Champagnat'

print(vars(restaurante_Chef))
print('')


# QUESTÃO 3 | QUESTÃO 4
class Restaurante:

    restaurantes=[]

    def __init__(self,nome,categoria, ano_criacao,localidade):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        self.ano_criacao=ano_criacao
        self.localidade=localidade

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.ano_criacao} | {restaurante.localidade}')

restaurante_Dionisio=Restaurante('Dionisio', 'Frutos do Mar', '1988', 'Batel')

print(restaurante_Dionisio)
Restaurante.listar_restaurante()
print('')

# QUESTÃO 5

class Cliente:

    clientes=[]

    def __init__(self,nome,idade,pessoa,endereco):
        self.nome=nome
        self.pessoa=pessoa
        self.idade=idade
        self.endereco = endereco

        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.pessoa} | {self.endereco}'

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} | {cliente.pessoa} | {cliente.endereco}')

cliente_Luiza=Cliente('Luíza', '32', 'jurídica', 'Ecovile')

cliente_Vinicius=Cliente('Vinicius', '28', 'física', 'Cabral')

cliente_Amanda=Cliente('Amanda', '40', 'física', 'Bairro Novo')


Cliente.listar_clientes()



