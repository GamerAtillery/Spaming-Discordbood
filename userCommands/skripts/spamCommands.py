import random
import discord
from discord import user
from discord import channel
import asyncio
class SpamCommands():
    lCatHeads = [":cat:",":scream_cat:",":joy_cat:",":smile_cat:"]

    lFailMessage = [
        "failed to hack user, the firewal was too hot",
        "your computer virus got lost on the way through the internet to",
        "layer 8 error, you can't hack ",
        "snip snap cable off, Error when hacking ",
    ]

    def __init__(self, mainclass) -> None:
        self.mainclass = mainclass
    
    async def spamNyanCatVideo(self, user:discord.User):
        for i in range (1, 10):
          await asyncio.sleep(1)
          await user.send("https://youtu.be/QH2-TGUlwu4")
    
    async def spamNyanCatText(self, user:discord.User, messageToUser="", bVideo=True):
        for line in self.getNyanCatList(messageToUser):
            await asyncio.sleep(1)
            await user.send(line)
        if bVideo:
            await asyncio.sleep(1)
            await user.send("https://youtu.be/QH2-TGUlwu4")
        return
    
    async def NyanCatMessage(self, user:discord.User, messageToUser="", bVideo=True, delete_after=5):
        sMessage = "\n".join(self.getNyanCatList(messageToUser))
        await user.send(sMessage, delete_after=delete_after)
        if bVideo:
            await user.send("https://youtu.be/QH2-TGUlwu4")
    
    def getNyanCatList(self, messageToUser = "")->list:
        sRainbow = ":rainbow_flag:"
        iRainbows = 1
        operator = 1
        sCatHead = random.choice(self.lCatHeads)
        l_linesNyanCatList = []
        while(iRainbows > 0):
            sZeile = ""
            for _ in range(iRainbows):
                sZeile = sZeile + sRainbow
                l_linesNyanCatList.append(sZeile + messageToUser + sCatHead)
            iRainbows = iRainbows + operator
            if iRainbows >= 5:
                operator = -1

        return l_linesNyanCatList
        
    
    def getRandomFailMessageHacking(self):
        return random.choice(self.lFailMessage)
    
    async def onHackingNyanCatText(self, user:discord.User, message:discord.Message):
        iRate = random.randint(0,10)
        iRate = 10
        iAttacks = 20
        sStartMessage = ":space_invader: try hacking " + user.name + "....."
        outputMessage:discord.Message = await message.channel.send(sStartMessage)
        
        key = self.mainclass.oUserClass.setNewStopKey(str(user.id), "hacking")
        if key == "":
            await outputMessage.edit(content = ":shield: failed to hack user, can't connect to " + user.name + f" Successrate(-1000/{iAttacks}) **don't try it again!** :police_officer:")
            return
        if iRate <9:
            await  outputMessage.edit(content =":lock: "+ self.getRandomFailMessageHacking() + user.name + f" Successrate(0/{iAttacks})")
            self.mainclass.oUserClass.onStop(str(message.author.id))
            return
        await user.send(":construction: you got hacked by " + message.author.display_name + "\n write `!stop` to stop the hack")
        for succes in range(iAttacks):
            await asyncio.sleep(1)
            if not self.mainclass.oUserClass.checkForStop(str(user.id), key):
                await  outputMessage.edit(content =f":space_invader: success to hack {user.name} :computer: ! Successrate({succes}/{iAttacks})")
                return
            await self.NyanCatMessage(user, "!stop", False)
            if succes%5 == 0:
                await  outputMessage.edit(content = sStartMessage + f"({succes}/{iAttacks})",)
            if not self.mainclass.oUserClass.checkForStop(str(user.id), key):
                await outputMessage.edit(content =f":space_invader: success to hack {user.name} :computer: ! Successrate({succes}/{iAttacks})")
                return
        await  outputMessage.edit(content =f":space_invader: success to hack {user.name} :computer: ! Successrate({succes + 1}/{iAttacks})")
        await user.send("the attack overrolled the complete system you was to late")
        self.mainclass.oUserClass.onStop(str(message.author.id), tempLock=True)

        

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