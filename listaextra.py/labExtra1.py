#Daniel Ferreira
#1)
class Dinheiro():
    def __init__(self, valor, moeda):
        """comentar"""
        self.valor = valor
        self.moeda = moeda
        self.conversao = {"USD": 4.012,"EUR": 4.451,"JPY": 0.035}
        self.real = valor * self.conversao[moeda]
    
    def  valor_em(self, moeda): 
        if moeda == "BRL":
            return self.real
        else: 
            return self.real / self.conversao[moeda]  

    def __str__(self):
        return "{} BRL".format(self.real)    

#2) 
def BrexitEmployment(cpfs_sair_da_UE, CPFs_permanecer_na_UE, CPF_emprego, CPFs_desemprego):
    opiniao = cpfs_sair_da_UE.union(CPFs_permanecer_na_UE)
    percem_trab = (CPF_emprego.union(CPFs_permanecer_na_UE)/ opiniao) * 100
    percem_ntrab = (CPFs_desemprego.union(CPFs_permanecer_na_UE)/ opiniao) * 100
    npercem_trab = (CPF_emprego.union(cpfs_sair_da_UE)/ opiniao) * 100
    npercem_ntrab = (CPFs_desemprego.union(cpfs_sair_da_UE)/ opiniao) * 100
    return "YES : {:.2f}% trabalham, {:.2f}% estão desempregados\n NO: {:.2f}% trabalham, {:.2f}% estão desempregados".format(percem_trab, percem_ntrab, npercem_trab, npercem_ntrab) 
  
   
   
 