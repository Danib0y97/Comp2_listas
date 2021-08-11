#Daniel Ferreira 
#1)
def contatos(lista:list) -> dict:
    """Recebe uma lista de  dicionários na entrada, junta os dados com suas chaves retornando todos os dados em um único dicionário."""    
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
#def piano(notas: str) -> list:











#3)
def rezistor(faixa_um:str, faixa_dois:str, faixa_tres:str)-> int:
    """O usuário, chama a função introduzindo suas cores desejadas e a função retorna o valor esperado"""
    dicValores = {"preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3, "amarelo": 4}
    valor = ((dicValores[faixa_um]*10+dicValores[faixa_dois]))*pow(10, dicValores[faixa_tres])
    return valor
 