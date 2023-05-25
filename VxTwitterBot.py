import discord
import re
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    twitter_regex = r"(https?://twitter\.com/[^\s]+)"
    matches = re.findall(twitter_regex, message.content)
    if matches:
        for match in matches:
            new_content = message.content.replace(match, match.replace("twitter.com", "vxtwitter.com"))
        await message.delete()
        await message.channel.send(f'{new_content}')


bot.run("YOUR_BOT_TOKEN")
