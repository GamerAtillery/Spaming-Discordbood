from userCommands.methodTranslationTable import MethodTranslationTable
import discord

class MethodsCommands(MethodTranslationTable):
    def __init__(self, mainclass):
        self.mainclass = mainclass
        self.dCommandList = {}


    async def sendID(self, message:discord.Message):
        await message.channel.send("Your ID is: "+str(message.author.id))
    
    async def getHelp(self, message:discord.Message):
        await message.channel.send(self.mainclass.oMessageClass.getHelp())

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