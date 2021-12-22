import discord
class MethodsUsercommand(dict):

    dCommandList:dict
    mainclass:discord.Client

    def __init__(self, mainclass) -> None:
        self.mainclass = mainclass
        self.dCommandList = {
            "!id":(self.sendID,"gibt die eigene UserID zurück"),
            "":""
        }
    
    async def sendID(self, message:discord.Message):
        await message.channel.send("Your ID is: "+str(message.author.id))
    
    async def getHelp(self, message:discord.Message):
        pass

#_____________________________________________________________________________________________________________________________________

    def __getitem__(self, key:str):
        return self.get(key)
    
    def get(self, key):
        if not key in self.dCommandList:
            return None
        return self.dCommandList[key][0]

    def __setitem__(self, key:str, value):
        raise Exception("function is not avaiable")
    
    def __str__(self):
        return str(self.dCommandList)


    def __len__(self):
        return len(self.dCommandList)

    def __iter__(self):
        return iter(self.dCommandList)

    def keys(self):
        return self.dCommandList.keys()

    def items(self):
        return self.dCommandList.items()

    def values(self):
        return self.dCommandList.values()