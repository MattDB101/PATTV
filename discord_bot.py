import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import main 
import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is now running.")


@bot.tree.command(name='getkey', description='Gets the most recent stream key.')
async def getkey(interaction: discord.Interaction):
    try:
        streamkey = db.get_streamkey(main.username)
        await interaction.response.send_message(f'Here is your stream key: {streamkey}')
    except Exception as e:
        await interaction.response.send_message(f'Error: {e}')


async def start_bot():
    await bot.start(TOKEN)


if __name__ == "__main__":
    asyncio.run(start_bot())
