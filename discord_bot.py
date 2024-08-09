import db
from shared_state import application_state
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands


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


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is now running.")


@bot.tree.command(name='getkey', description='Gets the most recent stream key.')
async def getkey(interaction):
    try:
        username = await application_state.get_username()  
        print(f"current user: {username}")
        streamkey = db.get_streamkey(username)
        await interaction.response.send_message(f'Here is your stream key: {streamkey}')
    except Exception as e:
        await interaction.response.send_message(f'Error: {e}')


async def start_bot():
    await bot.start(TOKEN)