import check_ban
import db
import time
#import discord_bot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

global username
username = ""
db.create_table()
# discord_bot.bot.run(TOKEN)
if username == "" :
         username = db.get_acc()

# while True:
#     if check_ban.check_user(username):
#         db.set_banned(username)
#         username = db.get_acc()
    
#     print("sleeping...")
#     time.sleep(3600) # 1hr