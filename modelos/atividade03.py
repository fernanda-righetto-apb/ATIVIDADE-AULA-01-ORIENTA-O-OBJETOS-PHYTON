# ATIVIDADE AULA 03 ORIENTAÇÃO À OBJETOS

# QUESTÃO 1

class Pessoa:
    pessoas=[]

    def __init__(self,nome,idade, profissao):
        self._nome=nome
        self._idade=idade
        self._profissao=profissao

        Pessoa.pessoas.append(self)

    def __str__(self):
         return f'{self._nome} | {self._idade} | {self._profissao}'
    
    @classmethod
    def listar_pessoa(cls):
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome} | {pessoa._idade} | {pessoa._profissao}')
    
    @property
    def aniversario(self):
      self._idade += 1

    def saudacao(self):
       print(f'Saudação {self._profissao}! Uma nova jornada começa agora!')

pessoa_Marcela=Pessoa('Marcela',20,'Fisioterapeuta')
pessoa_Carlos=Pessoa('Carlos',35, 'Odonto')

pessoa_Marcela.aniversario
print(pessoa_Marcela)
pessoa_Marcela.saudacao()
print('')
pessoa_Carlos.aniversario
print(pessoa_Carlos)
pessoa_Carlos.saudacao()

print('')
print('')

#  QUESTÃO 2

class ContaBancaria:
    contas=[]

    def __init__(self,titular,saldo):
        self._titular=titular
        self._saldo=saldo
        self._ativo=False
    
        ContaBancaria.contas.append(self)

# QUESTÃO 3    

    def __str__(self):
         return f'{self._titular} | {self._saldo} '
    
    @classmethod
    def listar_titulares(cls):
        for contaBancaria in cls.contas:
            print(f'{contaBancaria._titular} | {contaBancaria._saldo} | {contaBancaria._ativo} ')

# titular_Lena=ContaBancaria('Lena',3000)
# titular_Wanda=ContaBancaria('Wanda',20000)

# ContaBancaria.listar_titulares()

# QUESTÃO 4
    
    # é um método de objeto
    def ativar_conta(self):
        self._ativo=not self._ativo

titular_Lena=ContaBancaria('Lena',3000)
titular_Wanda=ContaBancaria('Wanda',20000)

titular_Lena.ativar_conta()
titular_Wanda.ativar_conta()

ContaBancaria.listar_titulares()

print('')
print('')

# QUESTÃO 5

class ContaBancaria:

    def __init__(self,titular,saldo):
        self._titular=titular
        self._saldo=saldo
        self._ativo=False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo 
    
# QUESTÃO 6
    
titular_Armando=ContaBancaria('Armando', 3200)
print(titular_Armando.titular)

print('')
print('')

# QUESTÃO 7 

class ClienteBanco:
    clientes=[]

    def __init__(self,nome,idade, profissao,perfil,renda):
        self._nome=nome
        self._idade=idade
        self._profissao=profissao
        self._perfil=perfil
        self._renda=renda

        ClienteBanco.clientes.append(self)
    
    @classmethod
    def listar_clientes(cls):
        for clienteBanco in cls.clientes:
            print(f'{clienteBanco._nome} | {clienteBanco._idade} | {clienteBanco._profissao} | {clienteBanco._perfil} | {clienteBanco._renda}')

# cliente_A=ClienteBanco('A','65','Advogado','Ouro',42000)
# cliente_B=ClienteBanco('B','36','Psicólogo','Prata',15000)
# cliente_C=ClienteBanco('C','19','Auxiliar de Produção','Bronze',1420)

# ClienteBanco.listar_clientes()

# QUESTÃO 8

    @classmethod
    def cartao(cls):
        for contaBancaria in cls.clientes:
            if contaBancaria._perfil == 'Ouro':
                print('Parabéns! Vocês está apto para o novo cartão Gold Ultra com maiores benefícios e ganhará de bônus 10000 para concorrer a prêmios!')
            else:
                print('Que pena! Ainda não está apto para o programa do cartão Gold Ultra!')        

cliente_A=ClienteBanco('A','65','Advogado','Ouro',42000)
cliente_B=ClienteBanco('B','36','Psicólogo','Prata',15000)
cliente_C=ClienteBanco('C','19','Auxiliar de Produção','Bronze',1420)

ClienteBanco.listar_clientes()
print('')
ClienteBanco.cartao()