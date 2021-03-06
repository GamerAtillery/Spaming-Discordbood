import discord
from discord.message import Message
import Database.conf as conf
import Database.messageManagement as messageManagement
import Database.userManagement as userManagement
from keep_alive import keep_alive
from userCommands import *
from authorisation import Authorisation


class SpamingBoot(discord.Client):
    oMessageClass = messageManagement.MessageManagement()
    oUserClass = userManagement.UserManagement()
    methodsUsercommand:DictCommands
    methodsUserReactions:DictReaction
    bMuted = False
    sServerID = conf.sServerID
    


    async def on_ready(self):
        print("ich habe mich eingeloggt.")
        self.methodsUsercommand = DictCommands(self)
        self.methodsUserReactions = DictReaction(self)





    async def on_message(self, message:discord.Message):
        if self.bMuted:
            if isinstance(message.channel, discord.channel.DMChannel) and str(message.content).lower().startswith("!dev-server"):
                pass
            else:
                return            
        print(message.content)
        if message.author == client.user:
            return
        tulpelCommand = self.methodsUsercommand[str(message.content)]
        if tulpelCommand == None:
            tulpelCommand = self.methodsUserReactions.get(str(message.content),str(message.channel.id))
        if tulpelCommand == None:
            return
        if not await Authorisation.checkChannelAuth(message, tulpelCommand[2]):
            return
        self.oUserClass.checkForTempLock(str(message.author.id))
        try:
            await tulpelCommand[0](message)
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
            try:
                await msg.delete()
            except Exception as e:
                print(e)
        
        

if __name__ == '__main__':
  if conf.sAPIkey == "":
    import os
    conf.sAPIkey = input("key:")
    os.system("clear")
    
  client = SpamingBoot()
  if conf.bWebOn:
     keep_alive()
    
  client.run(conf.sAPIkey)
