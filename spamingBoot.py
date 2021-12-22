
import discord
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

        

if __name__ == '__main__':
  if conf.sAPIkey == "":
    import os
    conf.sAPIkey = input("key:")
    os.system("clear")
    
  client = SpamingBoot()
  keep_alive()
    
  client.run(conf.sAPIkey)
