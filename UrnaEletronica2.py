#Objetivo: Trabalhar POO com o exemplo de uma urna eletrônica.
#Essa urna possuirá nome do candidato e o seu partido em questão.

#Criando a classe UrnaEletronica
class UrnaEletronica:
    def __init__(self):
        self.candidatos = [] #Definindo a lista candidatos, que será uma lista vazia de inicio.

    #Método criado para adicionar o candidato e partido na lista vazia de candidatos.
    def adiciona_candidato(self, nome_candidato, partido):
        self.candidatos.append({'Nome': nome_candidato, 'Partido': partido})

    #Método para visualizar todos os candidatos que estão inscritos na lista.
    def exibe_candidato(self):
        for item in self.candidatos:
            print('Candidato: %s - Partido: %s' % (item['Nome'], item['Partido']))

    #Método responsável por realizar a remoção do último candidato
    def remover_candidato(self):
        self.candidatos.pop()

    #Método feito para atualizar 
    def atualizar_candidato(self, indice_candidato, chave, valor):
        try: # Verifica se o índice passado é válido
            candidato = self.candidatos[indice_candidato] #Busca o candidato na lista de candidatos
            candidato[chave] = valor   # Atualiza a chave com o novo valor
        except IndexError: #Caso o índice seja inválido, exibe uma mensagem de erro
            print("Erro: índice de candidato inválido.")

#Testando o código

urna = UrnaEletronica()

urna.adiciona_candidato('Lula', 'PT')
urna.adiciona_candidato('Bolsonaro', 'Sem partido')
urna.adiciona_candidato('Marina Silva', 'Rede Sustentabilidade')
urna.adiciona_candidato('Ciro Gomes', 'PDT')
urna.exibe_candidato()
urna.atualizar_candidato(1,'Nome', 'Cabo Daciolo')
urna.atualizar_candidato(1,'Partido', 'PDT')
urna.exibe_candidato()

#O intuito era simular uma lista urna eletrônica, onde há candidatos e seus respectivos partidos.
#Nessa lista, poderíamos adicionar, remover, ou atualizar candidatos.

#Objetivo atingido. 
