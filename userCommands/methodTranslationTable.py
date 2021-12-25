import discord
from userCommands.skripts import *
from .skripts import *
class MethodTranslationTable(dict):
    lObservedChannels = []
    dCommandList:dict
    mainclass:discord.Client
    spamCommands:SpamCommands
    oSquidGame = (SquidGame())

    def __init__(self, mainclass):
        self.mainclass = mainclass
        self.spamCommands = SpamCommands(mainclass)
        return

    def observe(self, channelID:str):
        self.lObservedChannels.append(channelID)
        self.lObservedChannels = list( dict.fromkeys(self.lObservedChannels) )

    def stopObserve(self, channelID:str):
        try:
            self.lObservedChannels.remove(str(channelID))
        except Exception as e:
            print(str(e) + channelID)


    def __getitem__(self, key:str):
        if not key.startswith("!"):
            return None
        return self.get(key)

    def get(self, key, channelID="*"):
        for command in self.dCommandList.keys():
            if key.lower().startswith(command.lower()):
                return self.dCommandList[command]
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