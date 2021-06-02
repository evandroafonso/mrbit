import time  # biblioteca responsável pelo temporizador.
from funcoes import bitcoin
from funcoes import ethereum
from funcoes import litecoin
from funcoes import apresentacao

# função responsável pela temporização do programa.
def temporizador():
    iniciar = (input('Pressione "enter" para iniciar e "q" para encerrar a cotação: '))
    # laço while para dar a possbilidade de finalização ou reinício do programa.
    while iniciar != 'q':
        for tempo in range(3):
            # funções abaixo apresentam a cotação das criptomoedas.
            bitcoin()
            ethereum()
            litecoin()
            print()
            # temporizador de 100 segundos para próxima atualização do sistema
            time.sleep(100)
            print('============================')
            print('ATENÇÂO! Cotação atualizada!')
            print('============================')
        iniciar = (input('Deseja continuar? Se sim, pressione "enter", se não pressione "q".'))

# funções responsáveis por iniciar o programa.
apresentacao()
temporizador()