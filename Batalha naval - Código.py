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
      print(frota[nome_navio][0])
      while i < len(grid):
         grid[frota[nome_navio][navio]] = 1
    
    return grid
  


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
