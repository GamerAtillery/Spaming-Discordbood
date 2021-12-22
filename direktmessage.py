import discord
import Database.conf as conf




class SpamingBoot(discord.Client):
    async def on_ready(self):
        print(self.user)

    async def on_message(self, message):
          pass



if __name__ == '__main__':
    client = SpamingBoot()
    client.run(conf.sAPIkey)