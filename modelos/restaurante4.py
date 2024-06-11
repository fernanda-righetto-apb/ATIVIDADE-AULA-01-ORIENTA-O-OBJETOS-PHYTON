# 1 tornando o projeto aderente ao padrão de mercado

# import da classe avaliação


from modelos.avaliacao import Avaliacao

import os

class Restaurante:
    restaurantes=[]

    def main():
        os.system('cls')
        Restaurante.exibir_nome_do_programa()
        Restaurante.exibir_opcoes()
        Restaurante.escolher_opcao()

    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._avaliacao=[]
        self._ativo=False

        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'    

    def exibir_nome_do_programa():
        print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼')

    def exibir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Listar restaurantes')
        print('3. Alterar estado do restaurante')
        print('4. Avaliar restaurante')
        print('5. Sair\n')
    
    def voltar_menu_principal():
        input('Digite uma tecla para voltar ao menu principal')
        Restaurante.main()
    
    def opcao_invalida():
        print('Opção inválida\n')
        Restaurante.voltar_menu_principal()    

    def cadastrar_novo_restaurante():
        Restaurante.exibir_subtitulo('CADASTRO DE NOVOS RESTAURANTES')

        nome_do_restaurante=input('Digite o nome do restaurante que você quer cadastrar: ')
        categoria =input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
        # criar formato do dicionário pra daí apendar
        # dados_do_restaurante = {nome_do_restaurante,categoria}
        dados_do_restaurante = Restaurante(nome_do_restaurante,categoria)
        dados_do_restaurante
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
        Restaurante.voltar_menu_principal()    

    def registrar_avaliacao():
        Restaurante.exibir_subtitulo('CADASTRO DE AVALIAÇÕES')

        nome_do_restaurante = input('Digite o nome do restaurante que você quer cadastrar a avaliação: ')
    
        for restaurante in Restaurante.restaurantes:
            if nome_do_restaurante == restaurante._nome:
                nota_avaliacao = float(input(f'Digite um número de 0 a 10 que deseja avaliar o restaurante {nome_do_restaurante}: '))
                restaurante.receber_avaliacao(None, nota_avaliacao)  # Assuming you haven't implemented 'cliente' yet
                mensagem = f'Avaliação adicionada ao restaurante {nome_do_restaurante} com sucesso.'
                print(mensagem)
                break
        else:
            print(f'O restaurante {nome_do_restaurante} não foi encontrado')

        Restaurante.voltar_menu_principal()



    @classmethod
    def listar_restaurantes(cls):
        Restaurante.exibir_subtitulo('LISTANDO RESTAURANTES\n')

        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliações'.ljust(20)} | {'Status'.ljust(20)}')
        for restaurante in cls.restaurantes:
            nome_do_restaurante=restaurante._nome
            categoria=restaurante._categoria
            ativo='Ativado' if restaurante._ativo else 'Desativado'
            print(f'{nome_do_restaurante.ljust(20)} | {categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {ativo}')
        
        Restaurante.voltar_menu_principal()

    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    
    @classmethod
    def alternar_estado(cls):
        # self._ativo=not self._ativo
        Restaurante.exibir_subtitulo('Alterando estado do restaurante')
        nome_do_restaurante=input('Digite o nome do restaurante que deseja alterar o estado: ')
        restaurante_encontrado = False

        for restaurante in cls.restaurantes:
            if nome_do_restaurante==restaurante._nome:
                restaurante_encontrado=True
                # not é inversão
                restaurante._ativo=not restaurante._ativo
                mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante._ativo else f'O restaurante  {nome_do_restaurante} foi desativado com sucesso'
                print(mensagem)
        if not restaurante_encontrado:
                print(f'O restaurante {nome_do_restaurante} não foi encontrado')

        Restaurante.voltar_menu_principal()     

    # criando um método para receber as avaliações 
    def receber_avaliacao(self,cliente,nota):
        avaliacao=Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)    

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_de_notas,1)
        return media
    
    def exibir_subtitulo(texto):
        os.system('cls')
        # len é o lenght no JS - largura - multiplique por quanto der o do texto
        linha='*'*(len(texto))
        print(linha)
        print(texto)
        print(linha)
        print()
    
    def escolher_opcao():
        try:
            opcao_escolhida=int(input("Escolha uma opção: "))
            
            if opcao_escolhida==1:
                # print('Você escolheu cadastrar um restaurante')
                Restaurante.cadastrar_novo_restaurante()
            elif opcao_escolhida==2:
                # print('Você escolheu listar os restaurantes')
                Restaurante.listar_restaurantes()
            elif opcao_escolhida==3:
                # print('ativar restaurante')
                Restaurante.alternar_estado()
            elif opcao_escolhida==4:
                Restaurante.registrar_avaliacao()    
            else:
                Restaurante.finalizar_app()
        except:
            Restaurante.opcao_invalida()
    
    def finalizar_app():
        Restaurante.exibir_subtitulo('Finalizar app')
    
    

# restaurante_praca=Restaurante('praça', 'Gourmet')
# restaurante_praca._nome='biqueira'
# restaurante_praca.alternar_estado()

# restaurante_pizza=Restaurante('pizza express', 'Italiana')





# 5 consumindo o método listar_restaurantes
# Restaurante.listar_restaurantes()



