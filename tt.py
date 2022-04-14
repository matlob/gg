from telethon.events import StopPropagation
from telethon.sync import TelegramClient, events
import asyncio
import time

api_id = 14475649
api_hash = "8a92afffeb0571bbe1a9fa4e91087e6d"
Done_Coins = 0
Group = "kllllllwowo"
with TelegramClient('session', api_id, api_hash) as client:
  client.send_message(Group, "راتب")
  client.send_message(Group, "بخشيش")
  for i in range(2000):
     time.sleep(600)
     client.send_message(Group, "راتب")
     time.sleep(0.2)
     client.send_message(Group, "بخشيش")
