from roboka import Client
# pip install -U roboka

bot = Client("YOUR-TOKEN")

for update in bot.on_message():
	if update.text == "/start":
		update.reply("hello from roboka.")
