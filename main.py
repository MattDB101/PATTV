import db
import asyncio
import discord_bot
import ban_checker
import live_checker
from shared_state import application_state


async def check_ban():
    await asyncio.sleep(10)   
    i = 0
    try:
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
            
            print("sleeping ban check...")
            await asyncio.sleep(3600) # change to 3600 for 1hr    
    except Exception as e:
        print(f"Unexpected error in check_ban: {e}")


async def check_live():
    await asyncio.sleep(10)   
    try:
        while True:
            username = await application_state.get_username()
            was_live = await application_state.get_live()
            is_live = live_checker.check_user(username) 
            
            if not is_live:
                await application_state.set_live(False)
            
            if is_live and not(was_live):
                await application_state.set_live(True)
                print(f"{username} just went live!")
                await discord_bot.alert_live(username)
                            
            print("sleeping live check...")
            await asyncio.sleep(600)  
    except Exception as e:
        print(f"Unexpected error in check_live: {e}")


async def main():
    if await application_state.get_username() == "":
            new_account, new_streamkey = db.get_acc()
            await application_state.set_user(new_account, new_streamkey)
            
    bot_task = asyncio.create_task(discord_bot.start_bot())
    live_task = asyncio.create_task(check_live())
    ban_task = asyncio.create_task(check_ban())
    await asyncio.gather(bot_task, live_task, ban_task)

if __name__ == "__main__":
    asyncio.run(main())
