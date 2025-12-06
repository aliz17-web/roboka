from roboka import Client, Update
import asyncio

bot = Client("token")

@bot.on_message()
async def hello(update: Update):
    await bot.send_file(update.chat_id, "text", "fileName", "index.html", "File", update.message_id)
asyncio.run(bot.run())
