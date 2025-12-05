from roboka import Client, Update
import asyncio

bot = Client("token")

@bot.on_message()
async def hello(update: Update):
    await update.reply("~~strike~~, **bold**, __italic__, ||spoiler||, ==underline==, `mono`, [link](example.com), ××quote××")

asyncio.run(bot.run())
