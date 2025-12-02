from roboka import Client, Update
import asyncio

bot = Client("token")

@bot.on_message()
async def hello(update: Update):
    await update.reply('<s>strike</s>, <b>bold</b>, <i>italic</i>, <span class="tg-spoiler">spoiler</span>, <u>underline</u>, <code>mono</code>, <a href="https://example.com">link</a>')

asyncio.run(bot.run())
