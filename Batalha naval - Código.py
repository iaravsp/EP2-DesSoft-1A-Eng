def define_posicoes(linha,coluna,orientacao,tamanho):
    lista = []
    for i in range(tamanho):
        if orientacao == "vertical":
            lista.append([linha,coluna])
            linha += 1
        elif orientacao == "horizontal":
            lista.append([linha,coluna])
            coluna+=1

    return lista

def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    frota1 = {}
    
    frotas = define_posicoes(linha,coluna,orientacao,tamanho)

    for itens in frota:
        frota1[nome] = itens + frotas
 
    return frota1
    