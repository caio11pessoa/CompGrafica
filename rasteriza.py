# arquivo  que será usado para armazenar o código de rasterização
from segmentos_de_reta import Reta
def resultVariacaoEmX(reta= Reta):
    variacaoX = reta.p2[0] - reta.p1[0]
    variacaoy = reta.p2[1] - reta.p1[1]
    return variacaoX > variacaoy

    return 
def rasteriza(reta= Reta):
    if(resultVariacaoEmX(reta)):
        print("1")
    else:
        print("2")

    print(reta.p1)
    
rasteriza(Reta([1, 10], [200, 23]))