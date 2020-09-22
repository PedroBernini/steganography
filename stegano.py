import requests
import sys
import clipboard

API = 'https://neatnik.net/steganographr/api'

def checkApi():
    response = requests.get(API)
    if response.status_code == 200:
        return True
    return False

def encode(publicMessage, privateMessage):
    url = API + '?public=' + publicMessage.replace(' ', '+') + '&private=' + privateMessage.replace(' ', '+')
    response = requests.get(url)
    if response.status_code == 200:
        clipboard.copy(response.content.decode('utf-8'))
        print('Mensagem esteganografada pronta na área de transferência!')
    else:
        print('API Bad Request!')

def decode(publicMessage):
    url = API + '?decode=' + publicMessage.replace(' ', '+')
    response = requests.get(url)
    if response.status_code == 200:
        clipboard.copy(response.content.decode('utf-8'))
        print('Mensagem desteganografada pronta na área de transferência!')
    else:
        print('API Bad Request!')

def showCommands():
    print('Para esteganografar: $ python stegano.py encode "<mensagem publica>" "<mensagem privada>"')
    print('Para destaganografar: $ python stegano.py decode "<mensagem publica>"')

try:
    if checkApi():
        try:
            if sys.argv[1] == 'encode':
                encode(sys.argv[2], sys.argv[3])
            elif sys.argv[1] == 'decode':
                decode(sys.argv[2])
            else:
                print('Comando inválido!')
                showCommands()
        except IndexError:
            print('Parâmetros inválidos!')
            showCommands()
    else:
        print('Problemas com a API. Tente mais tarde!')
except:
    print('Comando inválido!')
    showCommands()


