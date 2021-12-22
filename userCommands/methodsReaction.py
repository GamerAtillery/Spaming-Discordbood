from userCommands.methodTranslationTable import *
import discord

class MethodsReaction(MethodTranslationTable):
    def __init__(self, mainclass):
        self.mainclass = mainclass
    