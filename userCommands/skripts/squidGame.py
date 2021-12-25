import discord
from discord import channel
from discord.message import Message

class Game():
    
    def __init__(self, sChannelId:str, outputMessage, sUserID) -> None:
        sUserID = str(sUserID)
        self.lPlayer = [sUserID]
        

class SquidGame():
    red = (":red_square:")
    green = (":green_square:")
    grey = (":grey_square:")
    descriptionBrighGame = ("one plat will hold you, the other will breaK under your weight, and you will fall in the depths")


    def __init__(self):
        pass
    
    async def onStartBrighGame(self, message:discord.Message):
        message.channel.send(self.descriptionBrighGame)
        return
