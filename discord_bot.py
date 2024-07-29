import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands
import main 
import db

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)

# !!! DON'T FORGET TO RE-ADD THE BOT TO THE SERVER AFTER MAKING CHANGES!!! #


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} is now running.")


@bot.tree.command(name='getkey', description='Gets the most recent stream key.')
async def getkey(interaction: discord.Interaction):
    streamkey = db.get_streamkey(main.username)
    await interaction.response.send_message(f'Heres your stream key: {streamkey}')


# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     if not message.content:
#         print("Message was empty because intents were not enabled properly")
#         return

#     if not message.content.startswith('/'):
#         await send_message(message, message.content)
        
#     await bot.process_commands(message)

# async def send_message(message, user_message):
#     is_private = user_message.startswith('?')
#     if is_private:
#         user_message = user_message[1:]

#     try:
#         if user_message.lower() == "hello":
#             response = "Hello!"
#         if response:
#             if is_private:
#                 await message.author.send(response)
#             else:
#                 await message.channel.send(response)
                
#     except Exception as e:
        # print(e)


bot.run(TOKEN)