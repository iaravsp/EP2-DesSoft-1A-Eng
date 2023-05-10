def define_posicoes(linha,coluna,orientacao,tamanho):
    lista = []
    x = linha
    y = coluna
    for i in range(tamanho):
        if orientacao == "vertical":
            lista.append([x,y])
            x += 1
        elif orientacao == "horizontal":
            lista.append([x,y])
            y+=1

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

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

#tamanho
embarcacoes = {
    "porta-aviões": 4,
    "navio-tanque": 3,
    "contratorpedeiro": 2,
    "submarino": 1
}
#qde
quantidade = {
    "porta-aviões": 1,
    "navio-tanque": 2,
    "contratorpedeiro": 3,
    "submarino": 4
}
frota = {}

for nome, tamanho in embarcacoes.items():
  i = 0
  while i < quantidade[nome]:
    print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(nome,tamanho))
    linha = int(input("Digite a linha: "))
    coluna = int(input("Digite a coluna: "))

    if nome != 'submarino':
      orientacao = int(input("Digite a orientação (1 - vertical, 2 - horizontal): "))

    if orientacao == 1:
          orientacao = 'vertical'
    elif orientacao == 2:
      orientacao = 'horizontal'
      

    while not posicao_valida(frota, linha, coluna, orientacao, tamanho):
      print("Esta posição não está válida!")
      print("Insira as informações referentes ao navio {0} que possui tamanho {1}".format(nome,tamanho))
      linha = int(input("Digite a linha: "))
      coluna = int(input("Digite a coluna: "))
      if nome != 'submarino':
        orientacao = int(input("Digite a orientação (1 - vertical, 2 - horizontal): "))

      if orientacao == 1:
          orientacao = 'vertical'
      elif orientacao == 2:
        orientacao = 'horizontal'
    else:
        #Caso a posição seja válida, você deve utilizar a funções define_posicoes e preenche_frota 
        # para popular o dicionário com as informações da frota do jogador.
        lista = define_posicoes(linha,coluna,orientacao,tamanho)
        frota = preenche_frota(frota,nome,linha,coluna,orientacao,tamanho)
    i+=1


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
total = 0
for i in frota_oponente.values():
    total+=1

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True

while jogando:
   print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
   perguntando = True
   posicoes_informadas = []
   while perguntando:
        linha = int(input("Jogador, qual linha deseja atacar?"))
        while linha not in range(0, 10):
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar?"))
            
        coluna = int(input("Jogador, qual coluna deseja atacar?"))
        while coluna not in range(0, 10):
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar?"))
            

        if [linha, coluna] not in posicoes_informadas:
            perguntando = False
            posicoes_informadas.append((linha, coluna))

   tabuleiro = faz_jogada(tabuleiro_oponente,linha,coluna)
   navios_afundados = afundados(frota_oponente,tabuleiro)
   if navios_afundados == 10:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False