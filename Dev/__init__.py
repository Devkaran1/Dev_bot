from telethon import TelegramClient
import logging
import time


api_id = "1125689"
api_hash = "4772d1792ed194020a8fb06a91ffb8fa"
bot_token = "6179173139:AAEE-mQUeVpkbJyaxFiZ6EzWHNPW9tzDLH8"

bot = TelegramClient(("Dev_gurjar_bot"), api_id, api_hash).start(bot_token = bot_token)