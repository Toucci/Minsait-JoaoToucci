#Instruções para criação do jogo

#criar um jogo de rpg de personagens e monstros
#primeira classe, ser vivo com atributos de pontos de vida e pontos de ataque
#criar duas classes derivadas desse ser vivo: Personagem e Monstro
#cada personagem vai ter pontos de vida e pontos de ataque
#atributo adicional nome para personagem
#atributo adicional tipo para monstro
#criar mais duas classes de monstros
#lobo, goblin
#lobo possui atributo força
#goblin possui atributo inteligencia
#atacar para lobo e goblin
#receber dano

#Criando a classe SerVivo
class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque
        self.morreu = False

#Método que faz o SerVivo atacar outro ser vivo   
    def atacar(self, dano, other):
        if not self.morreu: #Verifica se o SerVivo já está morto
            other.receber_dano(dano) # Chama o método 'receber_dano' do outro ser vivo
        else:
            print('o {} já está morto.'.format(self))

#Método que faz o SerVivo receber dano
    def receber_dano(self, dano):
        self.pontos_vida = self.pontos_vida - dano #Reduz os pontos de vida
    # Verifica se o SerVivo morreu
        if self.pontos_vida <= 0:
            print(f'{self} morreu.')
            self.morreu = True #Se essa condição for atingida, self.morreu vira True.
        else:
            print(f'{self} recebeu {dano} de dano e agora tem {self.pontos_vida} de vida.')

#Construtora feita para retornar a string do objeto(ao invés da memória)
    def __str__(self):
        #retorna o nome do personagem caso seja uma instância da classe Personagem
        if isinstance(self, Personagem): 
            return self.nome
        #retorna o tipo do monstro caso seja uma instância da classe Monstro
        elif isinstance(self, Monstro):
            return self.tipo
        #Se não pertencer nem a personagem, e nem a monstro, retornará Desconhecido.
        else:
            return 'Desconhecido'
                    

#Criando a classe Personagem(Que deriva de SerVivo)
class Personagem(SerVivo):
    def __init__(self, nome, pontos_de_vida, pontos_de_ataque):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome = nome #adicionando o atributo nome p/ personagem

#Criando a classe Monstro(Que deriva de SerVivo)
class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo #adicionando o atributo tipo p/ monstro

#Criando a classe Lobo(Que deriva de Monstro)
class Lobo(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, forca):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.forca = forca #adiciona o atributo força do lobo

#Criando a classe Goblin(Que deriva de Monstro)
class Goblin(Monstro):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, inteligencia):
        super().__init__(pontos_de_vida, pontos_de_ataque, tipo)
        self.inteligencia = inteligencia #adiciona o atributo inteligencia do goblin

#executando

heroi = Personagem("Gandalf", 100, 15)
lobo = Lobo(150, 10, 'lobo',8)
goblin = Goblin(100, 5, 'goblin',12)

heroi.atacar(100, goblin)
goblin.atacar(100, heroi)
