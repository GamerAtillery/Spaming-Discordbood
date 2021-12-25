import discord
from discord import channel
from discord.message import Message
import random

class Game():
    descriptionBrighGame = ("one plat will hold you, the other will breaK under your weight, and you will fall in the depths")
    red = (":red_square:")
    green = (":green_square:")
    grey = (":grey_square:")
    score = 0

    def __init__(self, outputMessage:discord.Message, sUserID, iMode=0) -> None:
        self.l_steps = []
        sUserID = str(sUserID)
        self.lPlayer = [sUserID]
        self.outputMessage:discord.Message = outputMessage
        self.iMode = iMode

    def buildMessage(self)->str:

        return ""

    def nextStep(self,):
        pass

        

class SquidGame():


    lOpenGames = []
    lchannels = []


    def __init__(self):
        pass
    
    async def onStartBrighGame(self, message:discord.Message):
        outputMessage = message.channel.send(self.descriptionBrighGame)
        return
