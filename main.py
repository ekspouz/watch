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
    nickname = f"đģBđĨđ¨đ đ đđĢđđēđŋâ {current_time.strftime('%H:%M')}"
    client.update_profile(first_name=nickname, bio=f"đ¯đ˛đĩđŋđđđŋđđđļđđ˛đ_đŧđŗđŗđļđ°đļđŽđšī¸ đ¨âđģ ruziyev.uz đ tg://settings đēđŋ â {current_time.strftime('%H:%M')}")
    client.invoke(pyrogram.raw.functions.account.UpdateStatus(offline=False))
    time.sleep(30)

client.stop()
