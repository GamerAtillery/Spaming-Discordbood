from userCommands.methodTranslationTable import MethodTranslationTable
from userCommands.skripts import *
import discord


class MethodsCommands(MethodTranslationTable):
    def __init__(self, mainclass):
        super().__init__(mainclass)
        self.dCommandList = {}



    async def NyanCat(self, message:discord.Message):
        for user in await self.mainclass.getId(message.content):
            try:
                if str(message.content).startswith("!nyancat-text"):
                    await self.spamCommands.spamNyanCatText(user)
                else:
                    await self.spamCommands.spamNyanCat(user)
            except Exception as e:
                print(e)

    async def Spam(self, message:discord.Message):
        for user in await self.mainclass.getId(message.content):
            try:
                await self.spamCommands.spamToUser(user)
            except Exception as e:
                print(e)



    async def AddMessage(self, message: discord.Message):
        entry = str(message.content).split('"')[1]
        self.mainclass.oMessageClass.addMessage(entry)
        await message.channel.send("message added")

    async def AddLink(self, message: discord.Message):
        entry = str(message.content).split('"')[1]
        self.mainclass.oMessageClass.addMessage(entry, 0)
        await message.channel.send("message added")
    
    async def showAllSpamMessages(self, message: discord.Message, link=True, sMessages=True):
        for messageitem, delay  in self.mainclass.oMessageClass.dMessages.items():
            delay = int(delay)
            #print(f"delay ={delay} type delay{type(delay)} messageitem={messageitem} {self.mainclass.oMessageClass.dMessages}")
            if delay > 0 and sMessages:
                await message.channel.send(messageitem )
                continue
            if delay == 0 and link:
                await message.channel.send(messageitem)    
                continue       
        return
    
    async def showSpamMessagesText(self, message: discord.Message):
        await self.showAllSpamMessages(message, link=False)
    
    async def showSpamMessagesLink(self, message: discord.Message):
        await self.showAllSpamMessages(message, sMessages=False)


    async def onPenis(self, message: discord.Message):
        if str(message.content).startswith("!penis-growing"):
            import random
            r = random.randint(1, 10)
            for length in range(0, r):
                await message.channel.send(Penis.sizedPenis(length), delete_after=5.0)
        elif str(message.content == "!penis"):
            await message.channel.send(Penis.generateMessage(str(message.author.display_name)))





