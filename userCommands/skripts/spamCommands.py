import discord
class SpamCommands():

    def __init__(self, mainclass) -> None:
        self.mainclass = mainclass
    
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