
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

START_BUTTON = InlineKeyboardMarkup([[              
                 InlineKeyboardButton('• 𝙊𝙪𝙩𝙧𝙪𝙞𝙓 • ™', url=f"https://t.me/TeamOutruix")
                 ],
                 [
                 InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/{}t?startgroup=true")
                 ]]
                  )
