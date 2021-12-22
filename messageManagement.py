import random
from dataManagement import *

class MessageManagement():
    dMessages = {}
    dataManagement = DataManagement()

    def __init__(self) -> None:
            self.dMessages = self.dataManagement.getMessagesDict()
        

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
        return self.dataManagement.setMessage(message, disappear)
    
    def getHelp(self):
        return '''
        !help -> Hilfe
        !spam @username -> spamt den User voll
        !addMessage "" -> fügt die Message hinzu
        !addLink "" -> fügt einen Link zur Liste hinzu
        !id -> gibt die Id des benutzers zurück
        !nyancat @username -> NyanCaaaat
        !filldb -> filldb.csv
        '''


if __name__ == "__main__":
    m = MessageManagement()
    m.addMessage("test", 6)
    for i in range(5):
        me, t = m.getRandomMessage("Niklas")
        print(me, t)