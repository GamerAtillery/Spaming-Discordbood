import discord

class MethodTranslationTable(dict):
    dCommandList:dict
    mainclass:discord.Client

    def __init__(self, mainclass):
        self.mainclass = mainclass
        return

    def __getitem__(self, key:str):
        return self.get(key)

    def get(self, key):
        for command in self.dCommandList.keys():
            if key.lower().startswith(command.lower()):
                return self.dCommandList[command][0]
        return None

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