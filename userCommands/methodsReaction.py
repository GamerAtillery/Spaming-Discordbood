from discord import channel
from .methodTranslationTable import MethodTranslationTable
from .skripts import *
import discord


class MethodsReaction(MethodTranslationTable):
    def __init__(self, mainclass) -> None:
        self.mainclass = mainclass

    async def reactionSquidGame(self, message:discord.Message):
        channelID = str(message.channel.id)
        if not channelID in self.oSquidGame.dOpenGamesBridge.keys():
            return
        bObserve = await self.oSquidGame.onMove(message)
        if not bObserve:

            self.stopObserve(channelID)