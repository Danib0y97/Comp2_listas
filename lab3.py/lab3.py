# Daniel Ferreira

class VeiculoAutomotor():
    def __init__(self, dono, placa, combustivel):
        self.dono = dono
        self.placa = placa
        self.combustivel = combustivel

    def __str__(self):
        return "Dono: {}, placa: {}, combustível: {}".format(self.dono, self.placa,self.combustivel)
#1)a)
class Automovel(VeiculoAutomotor):
    def __init__(self, dono:str , placa:str , combustivel:str, lugares:int, portas:int, ano:int):     
      """Construindo um construtor com os objetos que um Automovel possui."""
      super.__init__( dono, placa, combustivel)
      self.lugares = lugares 
      self.portas = portas 
      self.ano = ano  
#b)    
    def __str__(self:object) -> (str):
       return "Dono: {}, placa: {}, combustível: {}, lugares : {}, portas: {}, ano: {}".format(self.dono, self.placa,self.combustivel, self.lugares, self.portas,self.ano)

#c)    
    def trocarDono(self:object, novodono:str):
        """Caso o usuário deseja, poderá trocar o nome do dono do veículo"""
        self.dono = novodono

#2)a)
class Caminhao(VeiculoAutomotor):
    def __init__(self, dono:str , placa:str , combustivel:str, cargaMax:int):
     """Construindo um construtor com os objetos que um Caminhão possui"""
     super.__init__( dono, placa, combustivel)
     self.cargaMax = cargaMax  
#b)
    def __str__(self:object) -> (str):
       return "Dono: {}, placa: {}, combustível: {}, carga máxima: : {} toneladas".format(self.dono, self.placa,self.combustivel, self.cargaMax)




