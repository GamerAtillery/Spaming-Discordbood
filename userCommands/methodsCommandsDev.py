from userCommands.methodTranslationTable import MethodTranslationTable
from userCommands.skripts import *

import discord

class MethodsCommandsDev(MethodTranslationTable):
    def __init__(self, mainclass):
        super().__init__(mainclass)
        self.dCommandList = {}
    
    async def onDev(self, message:discord.Message):
        sMessage = str(message.content).lower()
        if sMessage.startswith("!dev-server="):
            await self.onChangeServer(message)
            return
        if sMessage.startswith("!dev-server"):
            await self.onServerStatus(message)
            return
        if sMessage.startswith("!dev-filldb"):
            await self.dev_fillDB(message)
            return
        if sMessage.startswith("!dev-help"):
            return
            
    

    async def onChangeServer(self, message:discord.Message):
        lMessage = str(message.content).split("=")
        sActiveServer = lMessage[1].replace(" ","")
        if sActiveServer == "":
            return
        if sActiveServer == "*" or sActiveServer == self.mainclass.sServerID:
            self.mainclass.bMuted = False
            await message.channel.send("server: "+ self.mainclass.sServerID + " is unmuted now")
            return
        if self.mainclass.sServerID != sActiveServer:
            self.mainclass.bMuted = True
            await message.channel.send("server: " + self.mainclass.sServerID + " is muted")
            return

    
    async def onServerStatus(self, message:discord.Message):
        return
    
    async def dev_fillDB(self, message:discord.Message):
        result = self.mainclass.oMessageClass.dataManagement.fillDatabaseFromCSV()
        await message.channel.send(result)
    

    
    async def onRun(self, message:discord.Message):
        return
    

        

        
