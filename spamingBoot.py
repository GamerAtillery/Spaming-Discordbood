from re import U
import discord
import conf




class SpamingBoot(discord.Client):
    async def on_ready(self):
        print("ich habe mich eingeloggt.")


    async def on_message(self, message:discord.Message):
        print(message.content)
        if message.author == client.user:
            return
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


    async def spamToUser(self, user:discord.User):
        if str(user.id) == "311838445301661696":
            for i in range(1, 20):
                await user.send("Chris we wanna see you on Rainbow again", delete_after=10.0)
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
