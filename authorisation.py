from re import T
import discord

class Authorisation():
    lChannel12Names = ["commands"]
    lChannel12IDs = []

    async def checkForAuth0(message:discord.Message,)->bool:
        if isinstance(message.channel, discord.channel.DMChannel):
            return True
        await message.channel.send("sorry, this command is private only!\n Pleace send this command in private Message again.", delete_after=10.0)
        await message.delete(delay=11)

    async def checkForAuth12(message:discord.Message,):
        if isinstance(message.channel, discord.channel.DMChannel):
            return True
        if message.channel.name in Authorisation.lChannel12Names:
            return True
        if str(message.channel.id) in Authorisation.lChannel12IDs:
            return True
        await message.channel.send("sorry, you can't send this command here!\n Pleace send this command in private Message or command-channel again.", delete_after=10.0)
        await message.delete(delay=11)



    async def checkChannelAuth(message:discord.Message, authValue:int)->bool:
        if authValue == 0:
            return await Authorisation.checkForAuth0(message)
        if authValue > 0 and authValue <3:
            return await Authorisation.checkForAuth12(message)
        return True;

