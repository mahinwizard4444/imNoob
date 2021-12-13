# import asyncio
# import logging
# import logging.config
#
# from pyrogram import Client, __version__, idle
# from pyrogram.raw.all import layer
# from database.ia_filterdb import Media
# from database.users_chats_db import db
# from info import LOG_STR
# from utils import temp
#
# from bot import Bot
#
#
# # async def main():
# #     await app.run()
# #     b_users, b_chats = await db.get_banned()
# #     temp.BANNED_USERS = b_users
# #     temp.BANNED_CHATS = b_chats
# #     await Media.ensure_indexes()
# #     me = await app.get_me()
# #     temp.ME = me.id
# #     temp.U_NAME = me.username
# #     temp.B_NAME = me.first_name
# #     # app.username = '@' + me.username
# #     logging.info(f"{me.first_name} with for Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
# #     logging.info(LOG_STR)
# #     logging.info(f"@{me.username} Has Started Running...🏃💨💨")
# #     print(f"\n[INFO] - {me.first_name} Bot Started !")
# #     await idle()
# #     logging.info(f"{me.first_name} Stopping")
# #     print(f"\n[INFO] - {me.first_name} Bot Stopped !")
# #     await app.stop()
#
#
# if __name__ == '__main__':
#     await asyncio.get_event_loop().run_until_complete(Bot)
# (©)𝙐𝙁𝙎 𝘽𝙤𝙩𝙯

# from bot import Bot
#
# Bot().run()
