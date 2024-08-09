import asyncio
import ban_checker
import db
import discord_bot
from shared_state import application_state

async def check_ban():
    await asyncio.sleep(10)   
    
    while True:
        username = await application_state.get_username()
        if ban_checker.check_user(username):
            db.set_banned(username)
            banned_account = username
            new_account = db.get_acc()
            await application_state.set_username(new_account)
            await discord_bot.alert_ban(banned_account, new_account)
        
        print("sleeping...")
        await asyncio.sleep(30)  # change to 3600 for 1hr    

async def main():
    if await application_state.get_username() == "":
        await application_state.set_username(db.get_acc())
    bot_task = asyncio.create_task(discord_bot.start_bot())
    ban_task = asyncio.create_task(check_ban())
    await asyncio.gather(bot_task, ban_task)

if __name__ == "__main__":
    asyncio.run(main())
