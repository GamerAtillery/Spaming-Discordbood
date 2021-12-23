
import discord
from discord.message import Message
import Database.conf as conf
import Database.messageManagement as messageManagement
from keep_alive import keep_alive
from userCommands import *


class SpamingBoot(discord.Client):
    oMessageClass = messageManagement.MessageManagement()
    methodsUsercommand:DictCommands
    methodsUserReactions:DictReaction
    


    async def on_ready(self):
        print("ich habe mich eingeloggt.")
        self.methodsUsercommand = DictCommands(self)
        self.methodsUserReactions = DictReaction(self)





    async def on_message(self, message:discord.Message):
        print(message.content)
        if message.author == client.user:
            return
        command = self.methodsUsercommand[str(message.content)]
        if command != None:
            try:
                await command(message)
            except Exception as e:
                print(e)



    async def getId(self, eingabe:str)->list:
        lTags = []
        lUsers = []
        sEingabe = str(eingabe)
        bAdd = False
        iPos = 0
        for z in list(sEingabe):
            if z == "<":
                bAdd = True
                
                lTags.append("")                
            if z == ">":
                bAdd = False
                lTags[iPos] = int(lTags[iPos])
                try:
                    lUsers.append(await self.fetch_user(lTags[iPos]))
                except Exception as e:
                    print(e)
                iPos = iPos + 1
            if bAdd == True and z.isdigit():
                lTags[iPos] = lTags[iPos] + z
            
        print(lTags)
        return lUsers

    async def clearChannel(self, message:discord.Message):
        if not isinstance(message.channel, discord.channel.DMChannel): #check's if message from dm
            await message.channel.send( 'You can use this command only in your direct message channel with me!\n')
            return
        await message.channel.send( 'Clearing messages...')
        msg:discord.Message
        async for msg in message.channel.history(limit=200):
            await msg.delete()
        
        

if __name__ == '__main__':
  if conf.sAPIkey == "":
    import os
    conf.sAPIkey = input("key:")
    os.system("clear")
    
  client = SpamingBoot()
  keep_alive()
    
  client.run(conf.sAPIkey)
