"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 3GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 40 India 🇮🇳 / per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 80 India 🇮🇳/ per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 120 India 🇮🇳/ per Month
	
	
	Pay Using Upi I'd ```adityakar052@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @Royaldwip"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Royaldwip")], 
        			[InlineKeyboardButton("Channel",url = "https://t.me/FoxPrimeBots"),
        			InlineKeyboardButton("Join",url = "https://t.me/WomBackup")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Price Rs 40 India 🇮🇳 / per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Price Rs 80 India 🇮🇳/ per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Price Rs 120 India 🇮🇳/ per Month
	
	
	Pay Using Upi I'd ```adityakar052@paytm```
	
	After Payment Send Screenshots Of 
        Payment To Admin @Royaldwip"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Royaldwip")], 
        			[InlineKeyboardButton("Channel",url = "https://t.me/FoxPrimeBots"),
        			InlineKeyboardButton("Join",url = "https://t.me/WomBackup")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
