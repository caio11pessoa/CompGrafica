# arquivo  que será usado para armazenar o código de rasterização
from segmentos_de_reta import Reta
def rasteriza(reta= Reta):
    variacaoX = reta.p2[0] - reta.p1[0]
    variacaoy = reta.p2[1] - reta.p1[1]

    if(variacaoX > variacaoy):
        print(variacaoX)
    else:
        print(variacaoy)

    print(reta.p1)
    
rasteriza(Reta([1, 1], [2, 2]))