import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from shared_state import application_state

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


async def alert_ban(bannedUser, newUser):
    try:
        channel = bot.get_channel(1266790214974705769)
        response = f"{bannedUser} has been Banned!\nNew account: https://www.twitch.tv/{newUser}"
        await channel.send(response)
    
    except Exception as e:
        print(e)


async def alert_live(username):
    try:
        channel = bot.get_channel(1266790214974705769)
        response = f"Someone just went live!\nhttps://www.twitch.tv/{username}"
        await channel.send(response)
    
    except Exception as e:
        print(e)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is now running.")


@bot.tree.command(name='getkey', description='Gets the most recent stream key.')
async def getkey(interaction):
    try:
        username = await application_state.get_username()  
        streamkey = await application_state.get_streamkey()
        print(f"current user: {username} {streamkey}")
        await interaction.response.send_message(f'Here is your stream key: {streamkey}')
    except Exception as e:
        await interaction.response.send_message(f'Error: {e}')


async def start_bot():
    await bot.start(TOKEN)