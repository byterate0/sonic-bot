import os
import re

import discord
from dotenv import load_dotenv

# interger :)
TARGET_CHANNEL_ID = 1450283496445710426

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

# .env

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    raise ValueError("No Discord token available in .env!")
print(f"Loaded token: {TOKEN[:5]}...")


def normalize_text(text):
    stylized_map = {
        "Ａ": "A",
        "Ｂ": "B",
        "Ｃ": "C",
        "Ｄ": "D",
        "Ｅ": "E",
        "Ｆ": "F",
        "Ｇ": "G",
        "Ｈ": "H",
        "Ｉ": "I",
        "Ｊ": "J",
        "Ｋ": "K",
        "Ｌ": "L",
        "Ｍ": "M",
        "Ｎ": "N",
        "Ｏ": "O",
        "Ｐ": "P",
        "Ｑ": "Q",
        "Ｒ": "R",
        "Ｓ": "S",
        "Ｔ": "T",
        "Ｕ": "U",
        "Ｖ": "V",
        "Ｗ": "W",
        "Ｘ": "X",
        "Ｙ": "Y",
        "Ｚ": "Z",
        "ａ": "a",
        "ｂ": "b",
        "ｃ": "c",
        "ｄ": "d",
        "ｅ": "e",
        "ｆ": "f",
        "ｇ": "g",
        "ｈ": "h",
        "ｉ": "i",
        "ｊ": "j",
        "ｋ": "k",
        "ｌ": "l",
        "ｍ": "m",
        "ｎ": "n",
        "ｏ": "o",
        "ｐ": "p",
        "ｑ": "q",
        "ｒ": "r",
        "ｓ": "s",
        "ｔ": "t",
        "ｕ": "u",
        "ｖ": "v",
        "ｗ": "w",
        "ｘ": "x",
        "ｙ": "y",
        "ｚ": "z",
    }
    normalized = "".join(stylized_map.get(c, c) for c in text)
    return normalized.lower()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # detect uppercase or stylized uppercase in any message
    if re.search(r"[Ａ-ＺA-Z]", message.content):
        print(f"Detected uppercase in message: {message.content}")
        normalized = normalize_text(message.content)
        print(f"Normalized: {normalized}")

        # send only to the target channel, regardless of where the message was sent
        output_channel = client.get_channel(TARGET_CHANNEL_ID)
        if output_channel:
            await output_channel.send(f" {normalized}")
        else:
            print("Output channel not found! Can you lock the fuck in?")


client.run(TOKEN)
