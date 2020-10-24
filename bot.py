import discord
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$spam'):
        for i in range(1,6):
            await message.channel.send('Hello!')

client.run('TOKEN')
