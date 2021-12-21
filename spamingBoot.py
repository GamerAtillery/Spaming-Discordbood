from re import M
import discord
import conf
import messageManagement


class SpamingBoot(discord.Client):
    oMessageClass = messageManagement.MessageManagement()

    async def on_ready(self):
        print("ich habe mich eingeloggt.")


    async def on_message(self, message:discord.Message):
        print(message.content)
        if message.author == client.user:
            return
        if(message.content.lower().startswith("!help")):
            await message.channel.send(self.oMessageClass.getHelp())
        if(message.content.lower().startswith("!id")):
            await message.channel.send("Your ID is: "+str(message.author.id))
        if (message.content.lower().startswith("!spam")):
            for iUserid in self.getid(message.content):
                try:
                    user:discord.User = await self.fetch_user(iUserid)
                    await self.spamToUser(user)
                except Exception as e:
                    print(e)

        if (message.content.lower().startswith("verständlich")):
            await message.author.send("Ich muss aufs Klo, kannst du mir bitte Klopapier bringen?")
        
        if (message.content.lower().startswith("!addmessage")):
            entry = str(message.content).split('"')[1]
            self.oMessageClass.addMessage(entry)
            await message.channel.send("message added")
        if (message.content.lower().startswith("!addlink")):
            entry = str(message.content).split('"')[1]
            self.oMessageClass.addMessage(entry, 0)
            await message.channel.send("message added")


    async def spamToUser(self, user:discord.User):
        for i in range(1, 20):
            message, time = self.oMessageClass.getRandomMessage(str(user.name))
            if time > 0:
                await user.send(message, delete_after=10.0)
            else:
                await user.send(message)
        return


    def getid(self, eingabe:str)->list[int]:
        lTags = []
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
                iPos = iPos + 1
            if bAdd == True and z.isdigit():
                lTags[iPos] = lTags[iPos] + z
        print(lTags)
        return lTags

        

if __name__ == '__main__': 
    client = SpamingBoot()
    client.run(conf.sAPIkey)
