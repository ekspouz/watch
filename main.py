import pytz
import datetime, time
from pyrogram import Client
import pyrogram

api_id = 1974187
api_hash = '3eb81ff38259f080151388a53a99fb4f'
client = Client('my_account', api_id, api_hash)

client.start()

while True:
    tz = pytz.timezone('Asia/Tashkent')
    current_time = datetime.datetime.now(tz)
    nickname = f"💻B𝐥𝐨𝐠𝐠𝐞𝐫🎓🇺🇿⚝ {current_time.strftime('%H:%M')}"
    client.update_profile(first_name=nickname, bio=f"𝗯𝗲𝗵𝗿𝘂𝘇𝗿𝘂𝘇𝗶𝘆𝗲𝘃_𝗼𝗳𝗳𝗶𝗰𝗶𝗮𝗹️ 👨‍💻 ruziyev.uz 🌐 tg://settings 🇺🇿 ⚝ {current_time.strftime('%H:%M')}")
    client.invoke(pyrogram.raw.functions.account.UpdateStatus(offline=False))
    time.sleep(30)

client.stop()
