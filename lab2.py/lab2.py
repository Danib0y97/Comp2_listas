from datetime import date

class Disciplina:
    """Classe representa o conceito de uma disciplina na UFRJ"""
    def __init__(self, nome, vagas = 0):
        """Cria um objeto da classe com atributos nome, vagas, alunos"""
        self.nome = nome
        self.vagas = vagas
        self.alunos = [] # self.alunos é um atributo global criado automaticamente

    def __add__(self, other):
        """Junta duas disciplinas se o nome delas for idêntico"""
        if self.nome == other.nome:
            return Disciplina(self.nome, self.vagas + other.vagas)
        else:
            print("Não foi possível juntar as turmas")
    
    def inscreverAluno(self, aluno):
        """Inscreve um objeto da classe Aluno na disciplina se tiver
        vagas livres ou o Aluno não for ainda inscrito na disciplina"""
        if len(self.alunos) < self.vagas and aluno not in self.alunos:
            self.alunos.append(aluno)
        elif aluno in self.alunos:
            print("aluno {} já está inscrito na disciplina".format(aluno.nome))
        else:
            print("Vagas esgotadas")
#1)a)    
    def consultarVagas(self):
        """Retorna a quantidade total de vagas e as vagas disponíveis"""
        return("Vagas totais:{}. Vagas livres:{}".format(self.vagas).format(self.vagas-len(self.alunos)))

#b)
    def __str__(self):
        """Retorna uma descrição de um objeto da classe ao chamar print("código da disciplina")"""
        return "{}, alunos inscritos: \t {} \t Vagas totais:{}. Vagas livres: {}".format(self.nome, self.alunos, self.vagas, self.vagas-len(self.alunos))
#Questão 2
#a)

class Pessoa: 
    def __init__(self, nome, dataNascimento,nomeDeMae, nomeDePai ):
        """Cria um objeto da classe Pessoa com atributos nome, dataNascimento , nomeDeMae, nomeDePai"""
        self.nome = nome
        self.dataNascimento = dataNascimento       
        self.nomeDeMae = nomeDeMae
        self.nomeDePai = nomeDePai     
 #b)
    def idade(self, data):
        """Retorna a idade da Pessoa"""
        data = date.today().strftime("%d/%m/%Y")
        return (data - self.dataNascimento) 
#c)
    def __str__(self):
        """Retorna uma descrição de um objeto da classe ao chamar print("Pessoa1")"""
        return "Nome: {}, idade: {}, mae: {}, pai: {}".format(self.nome, self.idade, self.nomeDeMae,  self.nomeDePai)    

