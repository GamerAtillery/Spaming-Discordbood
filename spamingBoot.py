import discord
import conf




class SpamingBoot(discord.Client):
    async def on_ready(self):
        print("ich habe mich eingeloggt.")

    async def on_message(self, message):
          pass

if __name__ == '__main__':
    client = SpamingBoot()
    client.run(conf.sAPIkey)