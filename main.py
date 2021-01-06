import discord
from dotenv import dotenv_values
from jumble_words import jumble_words

COMMAND_PREFIX = "$"
config = dotenv_values(".env")

client = discord.Client()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith(COMMAND_PREFIX):
        await message.channel.send(jumble_words(message.content[1:]))


client.run(config["DISCORD_TOKEN"])
