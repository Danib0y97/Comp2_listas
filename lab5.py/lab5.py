#Daniel Ferreira 

def absoluto(n:int) -> int:
    """Essa função verifica primeiramente se o número é positivo. Caso não seja, converte ele para positivo e o retorna. Se a pessoa não escrever um núemro, aparecerá um TypeError e um ValueError, informando o erro."""
    try:
        if n < 0:
            n * -1 
        return int(n)
    except ValueError:
            print("ValueError para '%s'." %(n))
            return None
    except TypeError:
            type(object) == type('')
            print("TypeError para <class '%s '>." %type)
            return None


#2)
#a)
class loja():  
    def __init__(self, nome:str, produtos:dict):
        """função das classes construtores."""
        self.nome = nome
        self.produtos = produtos
        
     
 #b)   
    def adicionarProduto(self, categoria:str, marca:str): 
        """Aqui, adicionamos a marca na categoria do produto e caso ele não exista, nos tratamos esse erro atualizando a categoria."""
        try:
           self.produtos[categoria].add(marca)
        
           
        except:
            self.produtos[categoria].update(marca)
            

#c)
    def verCategoria(categoria:str) -> str:
        """Caso a categoria não exista, será exibida uma mensagem."""
        try:
            return categoria
        except TypeError:
                print("Categoria {} não catalogada.".format(categoria))

#d)
    def removerMarca(self, marca:str):
        """Removemos o produto que desejamos."""
        self.produtos.discard(marca)



        

            
        


