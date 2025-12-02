from roboka import Client, Update
import asyncio
import os

bot = Client("توکن بات")
ADMIN_ID = "چت آیدی ادمین"
users = set()
waiting_for_broadcast = {}

if os.path.exists("users.txt"):
    with open("users.txt", "r") as f:
        for line in f:
            uid = line.strip()
            if uid:
                users.add(uid)

admin_keypad = [
    {
        "buttons": [
            {"id": "200", "type": "Simple", "button_text": "📢 پیام همگانی"}
        ]
    }
]

@bot.on_message()
async def on_message(update: Update):
    chat_id = update.chat_id
    text = update.text.strip()

    if chat_id not in users:
        users.add(chat_id)
        with open("users.txt", "a") as f:
            f.write(chat_id + "\n")

    if chat_id in waiting_for_broadcast and waiting_for_broadcast[chat_id]:
        msg = text
        waiting_for_broadcast[chat_id] = False
        await update.reply("✅ در حال ارسال پیام به همه کاربران...")
        sent = 0
        for uid in users:
            try:
                await bot.send_text(uid, msg)
                sent += 1
                await asyncio.sleep(0.05)
            except:
                pass
        await update.reply(f"📬 پیام به {sent} کاربر ارسال شد.")
        return

    if text == "/start":
        if chat_id == ADMIN_ID:
            await bot.create_keypad(chat_id, "👋 خوش آمدید ادمین!", admin_keypad)
        else:
            await update.reply("سلام")
        return

    if text == "📢 پیام همگانی":
        if chat_id != ADMIN_ID:
            await update.reply("🚫 فقط ادمین می‌تونه از این قابلیت استفاده کنه.")
            return
        waiting_for_broadcast[chat_id] = True
        await update.reply("📝 لطفاً پیام همگانی را بنویسید:")

asyncio.run(bot.run())
