# 1 criar uma classe restaurante
# tipada dinamicamente, dependendo do tipo de dado que vc guarda
class Restaurante:
    nome=''
    categoria=''
    ativo=False

# 2 criação de objetos
restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'


restaurante_pizza=Restaurante()

# array = list
restaurantes=[restaurante_praca,restaurante_pizza]

# métodos disponíveis para o objeto restaurante - instância da classe restaurante
#  abre infraestrutra do objeto e atributos presetnes = dir
print(dir(restaurante_praca))
print('')
#  abre valores presentes = vars
print(vars(restaurante_praca))

# QUESTÃO 1 

restaurante_praca.categoria = 'Italiana'
print(restaurante_praca.categoria)

# QUESTÃO 2

nome_restaurante = restaurante_praca.nome
print(nome_restaurante)


# QUESTÃO 3

print('Restaurante está ativo') if restaurante_praca.ativo == True  else print('Restaurante está inativo')

# QUESTÃO 4

categoria = Restaurante.categoria
print(categoria)

# QUESTÃO 5

restaurante_praca.nome = 'Bistrô'
print(vars(restaurante_praca))

# QUESTÃO 6

restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'

print(vars(restaurante_pizza))

# QUESTÃO 7

print(True) if restaurante_pizza.categoria == 'Fast Food' else print(False)

# QUESTÃO 8

restaurante_pizza.ativo = True

print(vars(restaurante_pizza))

# QUESTÃO 9 

print(vars(restaurante_praca))


# CORREÇÃO
#  - QUESTÃO 1
restaurante_praca.categoria ='Italiana'
print(restaurante_praca.categoria)
print('')
#  - QUESTÃO 2
nome_restaurante = restaurante_praca.nome
print(nome_restaurante)
print('')
#  - QUESTÃO 3
if restaurante_praca.ativo:
    print('O restaurante está ativo')
else:
    print('O restaurante está inativo')    
print('')    
#  - QUESTÃO 4
categoria = Restaurante.categoria
print(categoria)  
print('')  
#  - QUESTÃO 5
restaurante_praca.nome = 'Bistrô'
print(restaurante_praca.nome)
print('')
#  - QUESTÃO 6
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
print(vars(restaurante_pizza))
print('')
#  - QUESTÃO 7
if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food')
else:
    print('A categoria não é Fast Food')
print('')    
#  - QUESTÃO 8
restaurante_pizza.ativo = True
print(restaurante_pizza.ativo)
print('')
#  - QUESTÃO 9
print(f'Nome: {restaurante_praca.nome} e Categoria: {restaurante_praca.categoria}')