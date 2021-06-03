# biblioteca responsável pelo temporizador.
import time
# biblioteca responsável por mostrar o horário.
from datetime import datetime
from funcoes import bitcoin
from funcoes import ethereum
from funcoes import litecoin
from funcoes import presentation




# função responsável pela temporização do programa.
def chronometer():
    iniciar = (input('Pressione "enter" para iniciar e "q" para encerrar a cotação: '))
    print()

    # laço while para dar a possbilidade de finalização ou reinício do programa.
    while iniciar != 'q':
        for tempo in range(5):
            # funções abaixo apresentam a cotação das criptomoedas.
            bitcoin()
            ethereum()
            litecoin()
            print()

            # verificação do número de repetição do programa.
            if tempo >= 4:
                iniciar = (input('Deseja continuar? Se sim, pressione "enter", se não pressione "q".'))
            else:
                # temporizador de 100 segundos para próxima atualização do sistema.
                time.sleep(93)
                print('-----------------------------------------------')
                print('ATENÇÂO! A cotação será atualizada em breve...')
                print('-----------------------------------------------')
                print()
                time.sleep(7)
                hour = datetime.now().strftime('%H:%M:%S')  # variável acumulua o horário atual.
                print('=================================')
                print('       COTAÇÃO ATUALIZADA!       ')
                print('Horário da última cotação {}'.format(hour))  # mostra o horário atual para o usuário.
                print('==================================')


# funções responsáveis por iniciar o programa.
presentation()
chronometer()
