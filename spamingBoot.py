import discord
import conf




class SpamingBoot(discord.Client):
    async def on_ready(self):
        user = await self.fetch_user(295212845828931584)
        await user.send("es klappt")
        print(user)
        print("ich habe mich eingeloggt.")
        for i in range(5):
            try:
                print(next(self.get_all_members()))
            except:
                break

    async def on_message(self, message:discord.Message):
        print(message.content)
        if(message.content.lower().startswith("!id")):
            await message.channel.send("Your ID is: "+str(message.author.id))
        if (message.content.lower().startswith("!spam")):
            iUserid = self.getid(message.content)
            user:discord.User = await self.fetch_user(iUserid)
            user.send()




    def getid(eingabe:str)->int:
        return 295212845828931584
        

if __name__ == '__main__': 
    client = SpamingBoot()
    client.run(conf.sAPIkey)