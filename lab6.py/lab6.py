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
def lerArquivo(nome_arq):
    nome_arq = open("arq.txt",'r')

#criar uma lista com elemento (linhas)
#tirar o \n
#converter lista p/ float, string, lista

def f(nomeArq):

#Abrir arquivo pra leitura
# "-3.5\n9\n[12.0, '@9#', 9.8]\nab EE c\nk\n"
    arquivo=open(nome)
    
#criar uma lista com cada elemento(linhas)
#['-3.5\n', '9\n', "[12.0, '@9#', 9.8]\n",'ab EE c\n', 'k\n']
    
#tirar o \n
#['-3.5', '9','ab EE c', "[12.0, '@9#', 9.8]",, 'k']
    
#convertendo string p/ float ,string, lista
for indice in range(len(lista)):
    try:
        #converter pra número
        listalimpa[indice]=float(listalimpa[indice])
    except:
        #tirar as asp
 #tirar as aspas
        listalimpa[indice]=str(listalimpa[indice])

        if "[" in listalimpa[indice]:
        #converter lista
            listalimpa[indice]=retornarLista(listalimpa[indice])
        

return listalimpa


      

