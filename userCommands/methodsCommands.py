from userCommands.methodTranslationTable import MethodTranslationTable
from userCommands.skripts import *
import discord

class MethodsCommands(MethodTranslationTable):
    def __init__(self, mainclass):
        self.mainclass = mainclass
        self.dCommandList = {}


    async def sendID(self, message:discord.Message):
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

    async def fillDB(self, message:discord.Message):
        result = self.mainclass.oMessageClass.dataManagement.fillDatabaseFromCSV()
        await message.channel.send(result)

    async def NyanCat(self, message:discord.Message):
        for user in await self.mainclass.getId(message.content):
            try:
                await self.spamNyanCat(user)
            except Exception as e:
                print(e)

    async def Spam(self, message:discord.Message):
        for user in await self.mainclass.getId(message.content):
            try:
                await self.spamToUser(user)
            except Exception as e:
                print(e)


    async def spamNyanCat(self, user:discord.User):
        for i in range (1, 10):
          await user.send("https://youtu.be/QH2-TGUlwu4")

    async def spamToUser(self, user: discord.User):
        for i in range(1, 20):
            message, time = self.mainclass.oMessageClass.getRandomMessage(str(user.name))
            if time > 0:
                await user.send(message, delete_after=10.0)
            else:
                await user.send(message)
        if str(user.name) == "Sheller2003":
            await user.send("https://youtu.be/NRduatRzkfc?t=8")
        if str(user.name) == "54Garde":
            await user.send("https://youtu.be/rhvF2_JkDhQ")
        return


    async def AddMessage(self, message: discord.Message):
        entry = str(message.content).split('"')[1]
        self.mainclass.oMessageClass.addMessage(entry)
        await message.channel.send("message added")

    async def AddLink(self, message: discord.Message):
        entry = str(message.content).split('"')[1]
        self.mainclass.oMessageClass.addMessage(entry, 0)
        await message.channel.send("message added")
    
    async def onPenisGrowing(self, message: discord.Message):
        import random
        r = random.randint(1,10)
        for length in range(0, r):
            await message.channel.send( Penis.sizedPenis(length), delete_after=5.0)
     
    async def onPenis(self, message: discord.Message):
        await message.channel.send(Penis.generateMessage(str(message.author.display_name)))
    
    async def showAllSpamMessages(self, message: discord.Message, link=True, sMessages=True):
        for messageitem, delay  in self.mainclass.oMessageClass.dMessages.items():
            delay = int(delay)
            print(f"delay ={delay} type delay{type(delay)} messageitem={messageitem} {self.mainclass.oMessageClass.dMessages}")
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
