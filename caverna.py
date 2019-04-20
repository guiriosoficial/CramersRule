import time
import sys

print('OLÁ!')
time.sleep(1)
print('\nVOCE ESTÁ ENTRANDO NA')
time.sleep(1)
print('''
 _____       ___   _     _   _____   _____    __   _       ___
/  ___|     /   | | |   / / | ____| |  _  \  |  \ | |     /   |
| |        / /| | | |  / /  | |__   | |_| |  |   \| |    / /| |
| |       / / | | | | / /   |  __|  |  _  /  | |\   |   / / | |
| |___   / /  | | | |/ /    | |___  | | \ \  | | \  |  / /  | |
\_____| /_/   |_| |___/     |_____| |_|  \_\ |_|  \_| /_/   |_|
 \n''')

time.sleep(1)
print('Você exagerou de mais ontem a noite...')
time.sleep(1)
print('e agora acordar em uma caverna')
time.sleep(1)
print('Seu objetivo é sair da caverna!')


print('*18 horas atras...*')
print('tririririrm... triririririm')
print('tririririrm... triririririm')
print('*(Isto é um telefone)')


ans = input('- Hey cara, aqui é o Alan, vai ter despedida de solteiro do Doug, vamos lá?: (NAO/sim)\n- ').lower()

yes = ['sim', 's', 'si']
no = ['nao', 'n', 'na']
count = 1

def firstTry():
    ans = input('- Você vai ou não: (NAO/sim)\n- ')
    count += 1
def secondTry():
    ans = input('- Responde caramba: (NAO/sim)\n- ')
    count += 1
def refuse():
    print('- AAAGRR, TA BOM, TCHAU!')
    sys.exit()

while True:
    if ans in yes:
        print('- Beleza, até logo.')
        break
    elif ans in no:
        refuse()
    elif count == 1:
        firstTry()
    elif count == 2:
        secondTry()
    else:
        refuse()

time.sleep(1)
print('*Horas mais tarde*')


print('fim')


# while True:
#      comando = input('Insira uma ação: ')
#      if comando = 'SIM'
