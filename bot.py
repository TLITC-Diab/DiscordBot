import discord

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        if message.content.
        await message.channel.send('Hello!')

client.run('NzY5NjM1NTk2OTAxMjg1OTE2.X5R5AQ.igJkJUQV9np2lG0zSlajp8vIAFY')
