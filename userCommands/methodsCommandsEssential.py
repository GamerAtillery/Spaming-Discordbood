from userCommands.methodTranslationTable import MethodTranslationTable
from userCommands.skripts import *

import discord

class MethodsCommandsEssential(MethodTranslationTable):
    def __init__(self, mainclass):
        super().__init__(mainclass)
        self.dCommandList = {}
    
    async def sendID(self, message:discord.Message):
        sMessage = str(message.content).lower()
        if sMessage.startswith("!id-channel"):
            await message.channel.send("channel-id: "+str(message.channel.id))
            return
        if sMessage.startswith("!id-user"):
            print(self.mainclass.getId(message.content))
            for user in await self.mainclass.getId(str(message.content)):
                await message.channel.send(f"{user.name}:{user.id}")
            return
        await message.channel.send("Your ID is: "+str(message.author.id))

    
    async def getHelp(self, message:discord.Message):
        if "-all" in str(message.content):
            bAll = True
        else:
            bAll = False
        sMessage = ""
        for key, command in self.dCommandList.items():
            description:str = command[1]
            if description.startswith("->"):
                sMessage = sMessage + "\n" + key +" "+description
            elif(bAll):
                sMessage = sMessage + "\n" + key +" ->"+ description
        await message.channel.send(sMessage)