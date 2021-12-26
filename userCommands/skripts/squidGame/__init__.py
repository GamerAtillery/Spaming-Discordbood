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
                game:SquidGameBridge = SquidGameBridge(lUserID=lUserIDs, iMode=0)
            else:
                game:SquidGameBridge = SquidGameBridge(lUserID=lUserIDs)
            await game.onStart(message)
            self.dOpenGamesBridge[str(message.channel.id)] = game
            self.bRunningGames = True

        return True

    async def _onMove(self, message:discord.Message)->bool:
        print("_onMove")
        for a in list(str(message.content).lower()):
            if not a in ["l", "r", "!"]:
                return True
            bRunning = await self.dOpenGamesBridge[str(message.channel.id)].nextStep(a, message.author)
            if not bRunning:
                del self.dOpenGamesBridge[str(message.channel.id)]
                self.bRunningGames = not len(self.dOpenGamesBridge) > 0
                return False
        return True

    async def onMove(self, message:discord.Message)->bool:
        if str(message.channel.id) in self.dOpenGamesBridge.keys():
            return await self._onMove(message)

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