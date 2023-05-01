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