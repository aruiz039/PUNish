import discord
import aiohttp
import os

TOKEN = os.environ["DISCORD_TOKEN"]

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Pun?type=single"


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "PUNish" in message.content:
        async with aiohttp.ClientSession() as session:
            async with session.get(JOKE_API_URL) as response:
                if response.status == 200:
                    data = await response.json()
                    if not data.get("error"):
                        await message.channel.send(data["joke"])
                    else:
                        await message.channel.send("Couldn't fetch a pun right now.")
                else:
                    await message.channel.send("Failed to reach JokeAPI.")


client.run(TOKEN)
