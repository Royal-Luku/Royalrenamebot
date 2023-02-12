import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"**Must Join :- <a href='https://t.me/Worldofmovies8'>WOM BW MOVIES</a>\nCreater :- <a href='https://t.me/Royaldwip'>Royal Dwip ⚝</a>\nLanguage :- English \nLibrary :- Pyrogram\nServer :- Heroku\nTotal Renamed File :- {total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} \n\n Thank you 🙏 For Your Support And Love ❤\n\n✅ Please Join :- <a href='https://t.me/foxprimebots'>Click</a>\n\n🥀 Keep Supporting Us ✨\n▬▬▬▬▬▬▬▬▬▬▬▬▬
**",quote=True)
