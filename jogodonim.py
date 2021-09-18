def userjoga(qtdpecas, maxpecas): # Recebe os dados da jogada do usuário e retorna o mesmo.
    print()
    userM = int(input('Quantas peças você vai tirar? '))
    print()
    print('__________________________________________')
    print()
    if userM <= 0:
        while userM <= 0:
            print()
            print('**** Escolha um número entre 1 e {}. ****'.format(maxpecas))
            userM = int(input('Quantas peças você vai tirar? '))
            print()
            print('__________________________________________')
            print()
        return userM
    if userM > maxpecas:
        while userM > maxpecas:
            print()
            print('**** Escolha um número entre 1 e {}. ****'.format(maxpecas))
            userM = int(input('Quantas peças você vai tirar? '))
            print()
            print('__________________________________________')
            print()
        return userM
    if userM > qtdpecas:
        while userM > qtdpecas:
            print()
            print('Sobraram apenas {} peças na mesa, tire um valor menor ou igual a esse'. format(qtdpecas))
            userM = int(input('Quantas peças você vai tirar? '))
            print()
            print('__________________________________________')
            print()
        return userM
    else:
        return userM

def pcjoga(qtdpecas, maxpecas): # Algorítimo da jogada do computador e retorna o valor da jogada.
    ncount = qtdpecas
    while ncount % (maxpecas + 1) != 0:
        ncount -= 1
    pcM = qtdpecas - ncount
    if pcM > maxpecas:
        return maxpecas
    else:
        return pcM

def main(): # Função principal onde os dados retornam.
    qtdpecas = int(input('Informe quantas peças serão colocadas na mesa: '))
    maxpecas = int(input('Qual será o máximo de peças que se pode retirar em uma jogada: '))
    while maxpecas >= (qtdpecas/2):
        print('# O número de peças retiradas por jogada não pode ser maior que a metade das quantidade total de peças na mesa. #')
        qtdpecas = int(input('Informe quantas peças serão colocadas na mesa: '))
        maxpecas = int(input('Qual será o máximo de peças que se pode retirar em uma jogada: '))
    if qtdpecas % (maxpecas + 1) == 0:
        print()
        print('**** Você começa! ****')
        print()
        variavelus = userjoga(qtdpecas, maxpecas)
        qtdpecas -= variavelus
        print()
        print('Você tirou {} peças.'.format(variavelus))
        if qtdpecas <= 0:
                print()
                print('### Você ganhou essa partida. ###')
                print('__________________________________________')
                ptpc = 0
                ptus = 1
                return ptpc, ptus
        print('Restam {} peças no tabuleiro.'.format(qtdpecas))
        print('__________________________________________')
        while qtdpecas > 0:
            variavelpc = pcjoga(qtdpecas, maxpecas)
            qtdpecas -= variavelpc
            print()
            print('O computador tirou {} peças.'.format(variavelpc))
            if qtdpecas <= 0:
                print()
                print('### O computador ganhou essa partida. ###')
                print('__________________________________________')
                ptpc = 1
                ptus = 0
                return ptpc, ptus
            print('Restam {} peças no tabuleiro.'.format(qtdpecas))
            print('__________________________________________')
                
            variavelus = userjoga(qtdpecas, maxpecas)
            qtdpecas -= variavelus
            print()
            print('Você tirou {} peças.'.format(variavelus))
            if qtdpecas <= 0:
                print()
                print('### Você ganhou essa partida. ###')
                print('__________________________________________')
                ptpc = 0
                ptus = 1
                return ptpc, ptus
            print('Restam {} peças no tabuleiro.'.format(qtdpecas))
            print('__________________________________________')
                
    else:
        print()
        print('**** Computador começa! ****')
        print()
        variavelpc = pcjoga(qtdpecas, maxpecas)
        qtdpecas -= variavelpc
        print()
        print('O computador tirou {} peças.'.format(variavelpc))
        if qtdpecas <= 0:
            print()
            print('### O computador ganhou essa partida. ###')
            print('__________________________________________')
            ptpc = 1
            ptus = 0
            return ptpc, ptus
        print('Restam {} peças no tabuleiro.'.format(qtdpecas))
        print('__________________________________________')
        while qtdpecas > 0:
            variavelus = userjoga(qtdpecas, maxpecas)
            qtdpecas -= variavelus
            print()
            print('Você tirou {} peças.'.format(variavelus))
            if qtdpecas <= 0:
                print()
                print('### Você ganhou essa partida. ###')
                print('__________________________________________')
                ptpc = 0
                ptus = 1
                return ptpc, ptus
            print('Restam {} peças no tabuleiro.'.format(qtdpecas))
            print('__________________________________________')
                
            variavelpc = pcjoga(qtdpecas, maxpecas)
            qtdpecas -= variavelpc
            print()
            print('O computador tirou {} peças.'.format(variavelpc))
            if qtdpecas <= 0:
                print()
                print('### O computador ganhou essa partida. ###')
                print('__________________________________________')
                ptpc = 1
                ptus = 0
                return ptpc, ptus
            print('Restam {} peças no tabuleiro.'.format(qtdpecas))
            print('__________________________________________')

def batalha(user1, user2): # Batalha entre dois usuários
    print('__________________________________________')
    print()
    qtdpecas = int(input('{}, informe quantas peças terão sobre a mesa: '.format(user1)))
    maxpecas = int(input('{}, informe qual o número máximo de peças que se pode tirar por partida: '.format(user2)))
    print()
    print('__________________________________________')
    while maxpecas >= (qtdpecas/2):
        print('__________________________________________')
        print()
        print('# O número de peças retiradas por jogada não pode ser maior que a metade das quantidade total de peças na mesa. #')
        print()
        qtdpecas = int(input('{}, informe quantas peças terão sobre a mesa: '.format(user1)))
        maxpecas = int(input('{}, informe qual o número máximo de peças que se pode tirar por partida: '.format(user2)))
        print()
    print()
    print('**** {} começa! ****'.format(user1))
    print()
    us1 = userjoga(qtdpecas, maxpecas)
    qtdpecas -= us1
    print()
    print('{} tirou {} peças.'.format(user1,us1))
    if qtdpecas <= 0:
            print()
            print('### {} ganhou essa partida. ###'.format(user1))
            print('__________________________________________')
            ptus2 = 0
            ptus1 = 1
            return user1, user2, ptus1, ptus2
    
    print('__________________________________________')
    while qtdpecas > 0:
        print()
        print('---> É a vez de {}.'.format(user2))
        print()
        print('Restam {} peças no tabuleiro.'.format(qtdpecas))
        us2 = userjoga(qtdpecas, maxpecas)
        qtdpecas -= us2
        print()
        print('{} tirou {} peças.'.format(user2,us2))
        if qtdpecas <= 0:
            print()
            print('### {} ganhou essa partida. ###'.format(user2))
            print('__________________________________________')
            ptus2 = 1
            ptus1 = 0
            return user1, user2, ptus1, ptus2
        
        print('__________________________________________')
        print()
        print('---> É a vez de {}.'.format(user1))
        print() 
        print('Restam {} peças no tabuleiro.'.format(qtdpecas))
        us1 = userjoga(qtdpecas, maxpecas)
        qtdpecas -= us1
        print()
        print('{} tirou {} peças.'.format(user1,us1))
        if qtdpecas <= 0:
            print()
            print('### {} ganhou essa partida. ###'.format(user1))
            print('__________________________________________')
            ptus2 = 0
            ptus1 = 1
            return user1, user2, ptus1, ptus2
        print('Restam {} peças no tabuleiro.'.format(qtdpecas))
        print('__________________________________________')

def campeonato(): # Chama a função main() 3 vezes e guarda os dados dos ganhadores.
    rodada = 0
    totalpontospc = 0
    totalpontosuser = 0
    partida = 1
    while rodada < 3:
        print()
        print('        **** PARTIDA {} de 3 ****'.format(partida))
        print()
        i = main()
        rodada += 1
        totalpontospc += i[0]
        totalpontosuser += i[1]
        partida += 1
    print()
    print('#######################################')
    print('#         O CAMPEONATO ACABOU!        #')
    print('#                                     #')
    if totalpontospc > totalpontosuser:
        print('#         O computador ganhou!        #')
        print('#                                     #')
        print('#  Placar: Você |{}| X |{}| Computador  #'.format(totalpontosuser, totalpontospc))
        print('#######################################')
        print()
    else:
        print('#             Você ganhou!            #')
        print('#                                     #')
        print('#  Placar: Você |{}| X |{}| Computador  #'.format(totalpontosuser, totalpontospc))
        print('#######################################')
        print()
                
def campeonatousers(): # Entrada da area multi-player.
    print()
    print('**** Bem vindo a batalha dos usuários. ****')
    print()
    print('1 - Campeonato')
    print('2 - Partida única')
    print()
    select = int(input('Digite aqui: '))
    print()
    
    if select == 2:
        print()
        print('########################################')
        print('#                                      #')
        print('# *** INICIANDO UMA PARTIDA ÚNICA  *** #')
        print('#                                      #')
        print('########################################')
        print()
        user1 = input('Digite o nome do primeiro jogador: ')
        user2 = input('Digite o nome do segundo jogador: ')
        batalha(user1,user2)
        return
    if select == 1:
        print()
        print('########################################')
        print('#                                      #')
        print('#    *** INICIANDO UM CAMPEONATO ***   #')
        print('#                                      #')
        print('########################################')
        print()
        user1 = input('Digite o nome do primeiro jogador: ')
        user2 = input('Digite o nome do segundo jogador: ')
        rodada = 0
        totalpontosus1 = 0
        totalpontosus2 = 0
        partida = 1
        while rodada < 3:
            print()
            print('        **** PARTIDA {} de 3 ****'.format(partida))
            i = batalha(user1, user2)
            rodada += 1
            totalpontosus1 += i[2]
            totalpontosus2 += i[3]
            user1 = i[0]
            user2 = i[1]
            partida += 1
        print()
        print('#######################################')
        print('#         O CAMPEONATO ACABOU!        #')
        print('#                                     #')
        if totalpontosus1 > totalpontosus2:
            print('#             {} ganhou!               #'.format(user1))
            print('#                                     #')
            print('#        Placar: {} |{}| X |{}| {}        #'.format(user1, totalpontosus1, totalpontosus2, user2))
            print('#######################################')
            print()
        else:
            print('#             {} ganhou!               #'.format(user2))
            print('#                                     #')
            print('#        Placar: {} |{}| X |{}| {}        #'.format(user1, totalpontosus1, totalpontosus2, user2))
            print('#######################################')
            print()

def inicio(): # Chamada do inicio do jogo, entrada de dados e informações ao usuário
    print('0 - Regras do jogo')
    print('1 - Partida única')
    print('2 - Campeonato')
    print('3 - Batalha entre dois usuários')
    print()
    select = int(input('Digite aqui: '))
    if select == 0:
        print()
        print('#####################################################################################')
        print('#                                                                                   #')
        print('# |O jogo funciona da seguinte forma: você informará no começo do jogo quantas      #') 
        print('#  peças terão sobre a mesa e qual o limite máximo de peças que cada jogador        #')
        print('#  poderá retirar a cada rodada. Quem tirar a última peça da mesa ganha a partida.| #')
        print('#                                                                                   #')
        print('#                         | Preparado? Vamos lá! |                                  #')
        print('#                                                                                   #')
        print('#####################################################################################')
        print()
        print('1 - Partida única')
        print('2 - Campeonato')
        print('3 - Batalha entre dois usuários')
        print()
        select = int(input('Digite aqui: '))
    if select == 3:
        print()
        print('########################################')
        print('#                                      #')
        print('#     *** INICIANDO UMA BATALHA ***    #')
        print('#                                      #')
        print('########################################')
        print()
        campeonatousers()
        reboot = input('Deseja jogar novamente? [s/n]: ')
        if reboot == "s":
            inicio()
    
    if select == 2:
        print()
        print('########################################')
        print('#                                      #')
        print('#    *** INICIANDO UM CAMPEONATO ***   #')
        print('#                                      #')
        print('########################################')
        print()
        campeonato()
        reboot = input('Deseja jogar novamente? [s/n]: ')
        if reboot == "s":
            inicio()
        
    if select == 1:
        print()
        print('########################################')
        print('#                                      #')
        print('# *** INICIANDO UMA PARTIDA ÚNICA  *** #')
        print('#                                      #')
        print('########################################')
        print()
        main()
        reboot = input('Deseja jogar novamente? [s/n]: ')
        if reboot == "s":
            inicio()

def boasvindas(): # Tela de boas vindas.
    print()
    print('#######################################')
    print('#                                     #')
    print('#       Bem vindo ao jogo do NIM.     #')
    print('#                                     #')
    print('#######################################')
    print()
    print('**** Digite o número referente a sua opção ****')
    print()
    inicio()
boasvindas()
