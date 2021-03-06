import random
from .dataManagement import DataManagement

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
        self.dMessages[message] = disappear
        return self.dataManagement.setMessage(message, disappear)
    


if __name__ == "__main__":
    m = MessageManagement()
    m.addMessage("test", 6)
    for i in range(5):
        me, t = m.getRandomMessage("Niklas")
        print(me, t)