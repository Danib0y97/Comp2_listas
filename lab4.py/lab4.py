#Daniel Ferreira 
#1)
def contatos(lista:list) -> dict:
    """Recebe uma lista de dicionários, retornando um dicionário."""    
    nomes = []
    if type(lista[0]) != dict:
        return None
    
    for dicio in lista:
        for nome  in list(dicio.keys()):    
            if nome not in nomes:
                nomes += [nome]
                nomes += list(dicio.keys())   
                agenda = dict.fromkeys(nomes)
    
        for nome in agenda:
            agenda[nome] = []

        #abrindo o dicionário
        for dicio in lista:
            #Olhando um nome de cada vez
             for nome in nomes: 
                #verificando o nome no dicionário
                if nome in dicio:
                    #Caso o nome esteja, adicione ao lado
                    numero_do_contato=dicio.get(nome)
                    agenda[nome]+= [numero_do_contato]   	


        return agenda       	
      
#contatos(lista)

#2)
def piano(notas: str) -> list:
    
