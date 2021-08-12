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
def piano(notas:str)-> list:
    """Essa função faz com que o usuário insira as notas desejadas e terá de retorno a frequência dessas notas."""
    dic_freq = {"C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494}
    dicValorNotas = {1: -2, 2: -1, 3: 0, 4: 1, 5: 2}
    notas_totais = len(notas)//2
    count1 = 0
    count2 = 2
    frequenciasdalista = []
    for x in range(0, notas_totais):
        notaAtual = notas[count1:count2]
        frequenciasdalista.append(dic_freq[notaAtual[0]]*(pow(2, dicValorNotas[int(notaAtual[1])])))
        count1+=2
        count2+=2
    return frequenciasdalista



#3)
def rezistor(faixa_um:str, faixa_dois:str, faixa_tres:str)-> int:
    """O usuário, chama a função introduzindo suas cores desejadas e a função retorna o valor esperado"""
    dicValores = {"preto": 0, "marrom": 1, "vermelho": 2, "laranja": 3, "amarelo": 4}
    valor = ((dicValores[faixa_um]*10+dicValores[faixa_dois]))*pow(10, dicValores[faixa_tres])
    return valor
 