import discord
from discord.ext import commands
from generation import *

# Define intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create a bot instance with intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore messages from other bots

    mess = message.content.split(" ")

    
    if len(mess) == 3:
        try:
            risk = int(mess[1])
            number_words = int(mess[2])
        except ValueError:
            print("Invalid input. Please provide valid numbers.")
            return

        mes = generation(mess[0], risk, number_words)

        if mes:
            if isinstance(mes, str):
                await message.channel.send(mes)
            elif hasattr(mes, 'content'):
                await message.channel.send(mes.content)
            else:
                print("Invalid generation result.")
        else:
            print("Invalid generation result.")
    else:
        print("Bad message")
# Run the bot with the token obtained from the Discord Developer Portal
bot.run('MTE3NDQwMjA3OTQ4MjE4NzkwNw.G07l-c.TmilUzDWJaSndmQqUIyLPWPX7bwLTuHjxc4uLI')
