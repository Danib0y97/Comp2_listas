
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
         return("Vagas totais:{}. Vagas livres:{}".format(self.vagas).format(self.vagas-len(self.alunos)))

#b)
    def __str__(self):
        """Retorna uma descrição de um objeto da classe"""
        return "{}\t{}\tmatricula {}".format(self.nome, (self.alunos), self.vagas)
