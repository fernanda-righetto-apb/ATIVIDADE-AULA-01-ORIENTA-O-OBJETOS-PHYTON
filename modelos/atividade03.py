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


print(pessoa_Marcela)
pessoa_Marcela.aniversario
print('')
print(pessoa_Marcela)
pessoa_Marcela.saudacao()
print('')
print(pessoa_Carlos)
pessoa_Carlos.aniversario
print('')
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
                print(f'Prezado {contaBancaria._nome}, parabéns! Por seu perfil ser {contaBancaria._perfil}, você está apto para o novo cartão Gold Ultra com maiores benefícios e ganhará de bônus 10000 para concorrer a prêmios!')
            else:
                print(f'Prezado {contaBancaria._nome}, que pena! Por seu perfil ser {contaBancaria._perfil}, ainda não está apto para o programa do cartão Gold Ultra!')        

cliente_A=ClienteBanco('A','65','Advogado','Ouro',42000)
cliente_B=ClienteBanco('B','36','Psicólogo','Prata',15000)
cliente_C=ClienteBanco('C','19','Auxiliar de Produção','Bronze',1420)

ClienteBanco.listar_clientes()
print('')
ClienteBanco.cartao()

print('')
print('')

# CORREÇÃO ATIVIDADE03

# QUESTÃO 01 
class Pessoa:
    def __init__(self,nome,idade,profissao):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    # @property
    def saudacao(self):
        if self.profissao:
            print(f'Olá, sou {self.nome}! Trabalho como {self.profissao}.') 
        else:
            print(f'Olá, sou {self.nome}')             

    def aniversario(self):
        self.idade+=1

pessoa1=Pessoa('Aparício',99,'Programador')
print(pessoa1)
print('')
pessoa1.aniversario()
print(pessoa1)
print('')
pessoa1.saudacao()
print('')

# QUESTÃO 2
class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular=titular
        self.saldo=saldo
        self._ativo=False #atributo protegido

# QUESTÃO 3
    def __str__(self):
        return f'Conta de: {self.titular} - Saldo: R${self.saldo}'

# conta1=ContaBancaria('Nathan',3000.00)
# conta2=ContaBancaria('Joe',2.00)

# print(conta1)
# print('')
# print(conta2)

# QUESTÃO 4
    @classmethod
    def ativar_conta(cls,conta):
        conta._ativo = True

# conta3=ContaBancaria('Arina',3.58)
# print(f'Antes de ativar: Conta ativa? {conta3._ativo}')
# ContaBancaria.ativar_conta(conta3)
# print(f'Depois de ativar: Conta ativa? {conta3._ativo}')

# QUESTÃO 5

class ContaBancariaPythonica:
    def __init__(self,titular,saldo):
        self._titular=titular
        self._saldo=saldo
        self._ativo=False

    # aparencia de apresentação
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

# conta4=ContaBancariaPythonica('Josefino',1500.03)
# print(f'Titular da conta4 é: {conta4.titular}')

# QUESTÃO 7

class ClienteBanco:
    def __init__(self,nome,idade,profissao,endereco,telefone):
        self.nome=nome
        self.idade=idade
        self.profissao=profissao
        self.endereco=endereco
        self.telefone=telefone

# cliente1=ClienteBanco('João',30,'médico','Rua A','3696-6969')
# cliente2=ClienteBanco('Caio',19,'mecânico','Rua B','3696-6960')
# cliente3=ClienteBanco('Vitor',23,'programador','Rua C','3696-6965')

# QUESTÃO 8 

    @classmethod
    def criar_conta(cls,titular,saldo_inicial):
        conta=ClienteBanco(titular,saldo_inicial)
        return conta

conta_cliente1=ClienteBanco.criar_conta('Tertúlia,9999.99')
print(f'Conta de {conta_cliente1.titular} com saldo de R${conta_cliente1.saldo_inicial}')        
