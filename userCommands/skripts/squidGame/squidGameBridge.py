import discord
import random
import time
tab = "\t"
line = "\n"
class SquidGameBridge():

    descriptionBrighGame = ("one plat will hold you, the other will breaK under your weight, and you will fall in the depths\n\n")
    red = (":red_square:")
    green = (":green_square:")
    grey = (":blue_square:")

    outputMessage:discord.Message = None
    outputChannel = discord.DMChannel

    def __init__(self,  lUserID:list, iMode=2) -> None:
        self.startTime = time.time()
        self.l_steps = []
        self.l_killedMessages = []
        self.l_killedPlayer = []
        self.l_Player:list = lUserID
        self.iMode = iMode

    async def onStart(self, message:discord.Message):
        print("onStart bridgegame")
        if self.outputMessage == None:
            self.outputMessage:discord.Message = await message.channel.send(self.buildMessage())
            self.outputChannel = message.channel
        if str(message.author.id) in self.l_killedPlayer:
            await message.channel.send(f"<@{message.author.id}> You are already dead in this game.", delete_after=20)
            return
        self.l_Player.append(str(message.author.id))
        self.l_Player = list( dict.fromkeys(self.l_Player))

    def __buildNewLine(self, nr:int)->str:
        sLeftPlat = self.grey
        sRightPlat = self.grey
        if nr > len(self.l_steps):
            return f"{tab}{sLeftPlat} {sRightPlat} {str(nr)}. {line}"
        sCorrectPlat = self.l_steps[nr-1]
        sKillMessage = self.l_killedMessages[nr - 1]
        if sCorrectPlat == "l":
            sLeftPlat = self.green
        if sCorrectPlat == "r":
            sRightPlat = self.green
        if sKillMessage == "":
            return f"{tab}{sLeftPlat} {sRightPlat} {str(nr)}. {line}"
        if sCorrectPlat == "l":
            sRightPlat = self.red
        if sCorrectPlat == "r":
            sLeftPlat = self.red
        return f"{tab}{sLeftPlat} {sRightPlat} {str(nr)}. {sKillMessage}{line}"



    def __checkForCorrectPlat(self, inputPlat:str, player:discord.User)->tuple:
        if inputPlat == self.l_steps[len(self.l_steps) - 1]:
            self.l_killedMessages.append("")
            return (True, "")
        self.l_killedMessages.append(":skull_crossbones: RIP" + player.display_name)
        self.l_Player.remove(str(player.id))
        self.l_killedPlayer.append(str(player.id))
        if self.l_Player == []:
            return (False, f"game over your score was {len(self.l_steps) - 1}")
        return (True, "")




    def buildMessage(self, bFillUp=True)->str:

        startPlat = len(self.l_steps) - 5
        if startPlat < 1:
            startPlat = 1
        endPlat = startPlat + 8
        if not bFillUp:
            endPlat = len(self.l_steps) +1
        sMessage = self.descriptionBrighGame
        for p in range(startPlat, endPlat):
            sMessage = sMessage + self.__buildNewLine(p)
        sMessage = sMessage + "\n" + f"!l {self.grey}{self.grey} !r"
        return sMessage

    def getNextPlat(self, inputPlat:str)->str:
        lOptions = ["l", "r"]
        inputPlat = inputPlat.lower().replace("!", "")
        if inputPlat not in lOptions:
            return ""
        lOptions = lOptions + [inputPlat for _ in range(self.iMode)]
        if self.iMode > 0:
            lOptions.append(inputPlat)
        return random.choice(lOptions)

    async def nextStep(self, inputPlat:str, player:discord.User):
        print("nextStep")
        if not str(player.id) in self.l_Player:
            return True
        print("1")
        plat = self.getNextPlat(inputPlat)
        if plat == "":
            return True,
        self.l_steps.append(plat)
        print("2")
        bRunning, sMessageReturn = self.__checkForCorrectPlat(inputPlat, player)
        await self.outputMessage.edit(content=self.buildMessage(bRunning))
        if sMessageReturn != "":
            await self.outputChannel.send(sMessageReturn)
        return bRunning

if __name__ == '__main__':
    c = SquidGameBridge(lUserID=["niklas"], )
    c.l_steps = ["l", "r", "l"]
    c.l_killedMessages = ["", "", "killed"]
    print(c.buildMessage(False ))
    print(c.getNextPlat("l"))
    print(c.getNextPlat("r"))
    print(c.getNextPlat("l"))



