from roboka import Client, Update
import asyncio

bot = Client("token")

@bot.on_message()
async def hello(update: Update):
    await bot.send_file(update.chat_id, "text", "fileName", "path.ogg", "Music", update.message_id)
    # در اینجا میتوانید دیسکریپشن، اسم فایل، و مسیر فایل رو وارد کنید.
asyncio.run(bot.run())
