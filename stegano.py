# Author: Pedro Bernini. 2020.

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
        print('Steganography message ready on clipboard!')
    else:
        print('API Bad Request!')

def decode(publicMessage):
    url = API + '?decode=' + publicMessage.replace(' ', '+')
    response = requests.get(url)
    if response.status_code == 200:
        clipboard.copy(response.content.decode('utf-8'))
        print('Unsteganography message ready on clipboard!')
    else:
        print('API Bad Request!')

def showCommands():
    print('Invalid command!')
    print('For Steganography: $ python stegano.py --encode "<public message>" "<private message>"')
    print('For Unsteganography: $ python stegano.py --decode "<public message>"')

try:
    if checkApi():
        try:
            if sys.argv[1] == '--encode':
                encode(sys.argv[2], sys.argv[3])
            elif sys.argv[1] == '--decode':
                decode(sys.argv[2])
            else:
                showCommands()
        except IndexError:
            showCommands()
    else:
        print('API Error. Try later!')
except:
    showCommands()


