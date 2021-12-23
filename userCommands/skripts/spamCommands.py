import random
import discord
class SpamCommands():
    lCatHeads = [":cat:",":scream_cat:",":joy_cat:",":smile_cat:"]

    def __init__(self, mainclass) -> None:
        self.mainclass = mainclass
    
    async def spamNyanCat(self, user:discord.User):
        for i in range (1, 10):
          await user.send("https://youtu.be/QH2-TGUlwu4")
    
    async def spamNyanCatText(self, user:discord.User, zeilen=8):
        sRainbow = ":rainbow_flag:"
        iRainbows = 1
        operator = 1
        sCatHead = random.choice(self.lCatHeads)
        for _ in range(zeilen):
            sZeile = ""
            for _ in range(iRainbows):
                sZeile = sZeile + sRainbow
            await user.send(sZeile + sCatHead, delete_after=5)
            iRainbows = iRainbows + operator
            if iRainbows >= 5:
                operator = -1
            if iRainbows <= 1:
                operator = 1
                sCatHead = random.choice(self.lCatHeads)
        await user.send("https://youtu.be/QH2-TGUlwu4")
        return

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