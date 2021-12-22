import random
class Penis():
    lMessages = [
        "what for a monster",
        "doc we need a loupe! I can't detect anything",
        "are you sure you are not a girl?",

    ]
    
    def generatePenis()->str:
        rlength = random.randint(0,10)
        return Penis.sizedPenis(rlength)
        
    
    def generateMessage(username:str):
        message = "size maschine\n" + username + "'s penis:"
        r = random.randint(0,30)
        print(r)
        if  r < 29:
            return message + Penis.generatePenis()
        return message + "\n" + random.choice(Penis.lMessages)
    
    def sizedPenis(size:int)->str:
        sPenis = "\n8"
        for _ in range(size):
            sPenis = sPenis + "="
        sPenis = sPenis + ">"
        return sPenis

if __name__ == "__main__":
    print(Penis.generatePenis())
    print(Penis.generateMessage("niklas"))
