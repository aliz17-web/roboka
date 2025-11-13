from roboka import Client, Update, WebhookUpdate
import asyncio

bot = Client("token")

rows = [
    {
        "buttons": [
            {
                "id": "100",
                "type": "Simple",
                "button_text": "Add Account"
            }
        ]
    },
    {
        "buttons": [
            {
                "id": "101",
                "type": "Simple",
                "button_text": "Edit Account"
            },
            {
                "id": "102",
                "type": "Simple",
                "button_text": "Remove Account"
            }
        ]
    }
]

@bot.on_message()
async def messages(update: Update):
	if update.text == "/start":
		await bot.create_inline_keypad(update.chat_id, "choose one", rows, message_id=update.message_id)

@bot.on_message_webhook("https://example.com/hook.php")
async def inlines(update: WebhookUpdate):
	await bot.send_text(update.chat_id, f"شما روی دکمه {update.text} کلیک کردید.")

asyncio.run(bot.run())
