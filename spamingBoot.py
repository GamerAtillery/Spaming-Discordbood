
import discord
import conf
import messageManagement
from keep_alive import keep_alive
from methodsUserCommand import MethodsUsercommand


class SpamingBoot(discord.Client):
    oMessageClass = messageManagement.MessageManagement()
    methodsUsercommand:MethodsUsercommand
    


    async def on_ready(self):
        print("ich habe mich eingeloggt.")
        self.methodsUsercommand = MethodsUsercommand(self)





    async def on_message(self, message:discord.Message):
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
