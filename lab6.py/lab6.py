#Daniel Ferreira
#1)
def escreverNoArquivo(nome_arq:str,lista:list)-> str:
    """Uma função onde, se escreve determinados elementos dentro de uma lista e retorna a quantidade de caracteres. Também, os elementos dessa lista criada ficam um em cima do outro."""
    nome_arq = open("arq.txt",'r+')
    string = str(lista)
    nome_arq.writelines(lista)
    nome_arq.seek(0)
    return len(nome_arq.read())
