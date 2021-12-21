import random
from typing import Mapping

class MessageManagement():
    dMessages = {}

    def __init__(self) -> None:
            with open("messages.csv", "r") as file:
                for zeile in file:
                    
                    l_zeile = zeile.split(";")
                    self.dMessages[l_zeile[0]] = l_zeile[1]

            file.close()
        

    def getRandomMessage(self, name:str):
        
        l = list(self.dMessages.items())
        message, time = random.choice(l)
        message = message.replace("&&name", name)
        try:
            time = int(time)
        except:
            print("error")
            time = 5
        return message, time
    
    def addMessage(self, message, disappear=5):
        message = message.replace("ä", "ae")
        message = message.replace("Ä", "Ae")
        message = message.replace("ö", "oe")
        message = message.replace("Ö", "OE")
        message = message.replace("ü", "ue")
        message = message.replace("Ü", "Ue")
        self.dMessages[message] = str(disappear)
        with open("messages.csv", "a") as file:
            file.write(f"{message};{disappear};\n")
            file.close()
    
    def getHelp(self):
        return '''
        !help -> Hilfe\n
        !spam @username -> spamt den User voll\n
        !addMessage "" -> fügt die Message hinzu\n
        !addLink "" -> fügt einen Link zur Liste hinzu
        !id -> gibt die Id des benutzers zurück
        
        '''


if __name__ == "__main__":
    m = MessageManagement()
    m.addMessage("test", 6)
    for i in range(5):
        me, t = m.getRandomMessage("Niklas")
        print(me, t)