import asyncio
import check_ban
import db
import discord_bot  # Import the bot module

global username
username = ""
db.create_table()

async def start():
    global username
    if username == "":
        username = db.get_acc()

    while True:
        if check_ban.check_user(username):
            db.set_banned(username)
            username = db.get_acc()

        print("sleeping...")
        await asyncio.sleep(100)  # change to 3600 for 1hr

async def main():
    bot_task = asyncio.create_task(discord_bot.start_bot())
    main_task = asyncio.create_task(start())
    await asyncio.gather(bot_task, main_task)

if __name__ == "__main__":
    asyncio.run(main())
