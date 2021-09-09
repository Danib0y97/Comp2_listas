#Daniel Ferreira
#1)
def escreverNoArquivo(nome_arq:str,lista:list)-> str:
    """Uma função onde, se escreve determinados elementos dentro de uma lista e retorna a quantidade de caracteres. Também, os elementos dessa lista criada ficam um em cima do outro."""
    nome_arq = open("arq.txt",'r+')
    string = str(lista)
    nome_arq.writelines(lista)
    nome_arq.seek(0)
    return len(nome_arq.read())

#2)
def retornarLista(strlist :str)-> list:
    texto = strlist.strip("[]")
    texto = texto.replace ("'", "")
    lista = texto.split(",")
    for indice in range(len(lista)):
     try:
        lista[indice] = float(lista[indice])
     except:
        pass

    return lista
        

#3)
def lerArquivo(nome_arq:str,lista:list) -> list:
    nome_arq = open("arq.txt",'r')
    nome_arq.writelines(lista)
    listalimpa = nome_arq.strip("\n")
    for indice in range(len(lista)):
        try:
         listalimpa[indice]=float(listalimpa[indice])
        except:
            listalimpa[indice]=str(listalimpa[indice])
            if "[" in listalimpa[indice]:
              listalimpa[indice]= retornarLista(listalimpa[indice])
        

    return listalimpa


      

