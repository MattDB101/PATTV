import db
import asyncio
import discord_bot
import ban_checker
from shared_state import application_state


async def check_ban():
    await asyncio.sleep(10)   
    i = 0
    while True:
        print(f"uptime: {i} hours.")
        i+=1
        username = await application_state.get_username()
        if ban_checker.check_user(username):
            db.set_banned(username)
            
            banned_account = username
            new_account, new_streamkey = db.get_acc()
            await application_state.set_user(new_account, new_streamkey)
            await discord_bot.alert_ban(banned_account, new_account)
        
        print("sleeping...")
        await asyncio.sleep(40)  # change to 3600 for 1hr    


async def main():
    if await application_state.get_username() == "":
            new_account, new_streamkey = db.get_acc()
            await application_state.set_user(new_account, new_streamkey)
            
    bot_task = asyncio.create_task(discord_bot.start_bot())
    ban_task = asyncio.create_task(check_ban())
    await asyncio.gather(bot_task, ban_task)

if __name__ == "__main__":
    asyncio.run(main())
