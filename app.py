# 3 - importar o arquivo que contenha a classe restaurante
from modelos.restaurante4 import Restaurante
import os

# 4 - criar um objeto(instância de Restaurante)
restaurante_praca=Restaurante('praça','gourmet')
restaurante_mexicano=Restaurante('mexican food','mexicana')
restaurante_japones=Restaurante('japa','japonesa')

# # alternar estado de um restaurante
# restaurante_japones.alternar_estado()2

# criando avaliações para o restaurante praça
restaurante_praca.receber_avaliacao('Albino',8)
restaurante_praca.receber_avaliacao('Berenice',5.5)



# 2 - criando a chamada da função de entrada
def main():
    # 5 inserir  uma ação dentro do main
    os.system('cls')
    Restaurante.exibir_nome_do_programa()
    Restaurante.exibir_opcoes()
    Restaurante.escolher_opcao()
    # Restaurante.listar_restaurantes()

if __name__ =='__main__':
    main()




# elimina sequencia de identificação de erros
    # pass