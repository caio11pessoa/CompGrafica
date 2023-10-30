# arquivo  que será usado para armazenar o código de rasterização
from segmentos_de_reta import Reta
def resultVariacaoEmX(reta= Reta):
    variacaoX = reta.p2[0] - reta.p1[0]
    variacaoY = reta.p2[1] - reta.p1[1]
    return (variacaoX > variacaoY, variacaoX, variacaoY)

def rasteriza(reta= Reta):
    varEmX, variacaoX, variacaoY = resultVariacaoEmX(reta)
    if(varEmX):
        # Variacao em X
        x = reta.p1[0]
        y = reta.p1[1]
        m = variacaoY/variacaoX
    else:
        print("2")
        m = variacaoY/variacaoX



    
rasteriza(Reta([1, 10], [200, 23]))