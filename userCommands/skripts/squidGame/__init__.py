import discord
from .squidGameBridge import SquidGameBridge
import asyncio

class SquidGame():
    bRunningGames = False

    dOpenGamesBridge:dict = {}


    def __init__(self):
        pass

    async def onStartBrighGame(self, message:discord.Message, lUserIDs=[]):
        print("start bridgegame")
        if not str(message.channel.id) in self.dOpenGamesBridge.keys():
            if "-hard" in str(message.content):
                game:SquidGameBridge = SquidGameBridge(lUserID=lUserIDs, iMode=2)
            else:
                game:SquidGameBridge = SquidGameBridge(lUserID=lUserIDs)
            await game.onStart(message)
            self.dOpenGamesBridge[str(message.channel.id)] = game
            self.bRunningGames = True

        return True

    async def onMove(self, message:discord.Message)->bool:
        if str(message.channel.id) in self.dOpenGamesBridge.keys():
            bRunning = await self.dOpenGamesBridge[str(message.channel.id)].nextStep(message.content[1], message.author)
            if not bRunning:
                del self.dOpenGamesBridge[str(message.channel.id)]
                self.bRunningGames = not len(self.dOpenGamesBridge) > 0
                return False
            print(f"{self.bRunningGames=}")
        return True

    async def deleteMessage(self,message:discord.Message):
        try:
            if str(message.content).lower() in ["!r", "!l"]:
                await message.delete()
        except Exception as e:
            pass


    def checkIsRunning(self, channelID:str):
        print("checkIsRunning")
        print(f"{self.bRunningGames=}")
        #if not self.bRunningGames:
            #return False
        if channelID in self.dOpenGamesBridge.keys():
            return True