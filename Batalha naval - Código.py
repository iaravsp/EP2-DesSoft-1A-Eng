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

def preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho):
    
    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    return frota


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
    