import random
import discord
from discord import user
from discord import channel
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
    
    async def spamNyanCat(self, user:discord.User):
        for i in range (1, 10):
          await user.send("https://youtu.be/QH2-TGUlwu4")
    
    async def spamNyanCatText(self, user:discord.User, messageToUser="", bVideo=True):
        for line in self.getNyanCatList(messageToUser):
            await user.send(line)
        if bVideo:
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
        await message.channel.send(":space_invader: try hacking " + user.name + ".....")
        iAttacks = 20
        iRate = 10
        key = self.mainclass.oUserClass.setNewStopKey(str(user.id), "hacking")
        if key == "":
            await message.channel.send(":shield: failed to hack user, can't connect to " + user.name + f" Successrate(-1000/{iAttacks}) **don't try it again!** :police_officer:")
            return
        if iRate <10:
            await message.channel.send(":lock: failed to hack user, the firewal was too hot " + user.name + f" Successrate(0/{iAttacks})")
            return
        for succes in range(iAttacks):
            if not self.mainclass.oUserClass.checkForStop(str(user.id), key):
                await message.channel.send(f":space_invader: success to hack {user.name} :computer: ! Successrate({succes}/{iAttacks})")
                return
            await self.NyanCatMessage(user, "!stop", False)
            await message.channel.send(f"({succes}/{iAttacks})", delete_after=5)
        await message.channel.send(f":space_invader: success to hack {user.name} :computer: ! Successrate({succes}/{iAttacks})")
        self.mainclass.oUserClass.aktivateKey(str(message.author.id))

        

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