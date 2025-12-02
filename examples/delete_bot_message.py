from roboka import Client, Update
import asyncio
import time

bot = Client("token")

@bot.on_message()
async def hello(update: Update):
    sent = await bot.send_text(update.chat_id, "test", update.message_id)
    msg_id = sent["data"]["message_id"]
    time.sleep(3) # تاخیر در پاک کردن پیام
    await bot.delete_message(update.chat_id, msg_id)
    await bot.send_text(update.chat_id, "پیام قبلی ربات حذف شد.")

asyncio.run(bot.run())
