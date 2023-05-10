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


def posiciona_frota(frota):
  grid = []
  linhas = [0]*10
  for i in linhas:
    grid.append(([i*10])*10)

  for nome_navio in frota:
    
    for navio in frota[nome_navio]:
      
      i = 0
      while i < len(navio):
         
         linha = navio[i][0]
         coluna = navio[i][1]

         grid[linha][coluna] = 1
         
         i += 1

  return grid



def afundados(frota,tabuleiro):
    qnt_navios_afundados = 0
    for nome_navio in frota:
        for navio in frota[nome_navio]:
            i = 0
            navio_afundado = True

            while navio_afundado and i < len(navio):
                linha = navio[i][0]
                coluna = navio[i][1]
                if tabuleiro[linha][coluna] != 'X':
                    navio_afundado = False
                i += 1

            if navio_afundado:
                qnt_navios_afundados += 1

    return qnt_navios_afundados



def posicao_valida(dic, linha, coluna, orientacao, tamanho):
    resultado = define_posicoes(linha, coluna, orientacao, tamanho)
    
    for nome, navio in dic.items():
        for coordenada in resultado:
            for posicao in navio:
                if coordenada in posicao:
                    return False
    
    if orientacao == "horizontal":
        if coluna + tamanho > 10:
            return False
    elif orientacao == "vertical":
        if linha + tamanho > 10:
            return False
    
    return True