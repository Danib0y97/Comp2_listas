def escreverNoArquivo(nome_arq,lista):
    nome_arq = open("arq.txt",'r+')
    string = str(lista)
    nome_arq.writelines(lista)
    nome_arq.seek(0)
    return len(nome_arq.read())
