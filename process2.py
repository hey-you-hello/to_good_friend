import logging
logging.disable(logging.CRITICAL)

import discord
from discord.ext import commands
import asyncio
import sys
from datetime import datetime
from rich.console import Console
from rich.text import Text
from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

session = PromptSession()
# ===== rich 初始化 =====

console = Console()
highlight_words = ["♡", "幹", "雜魚", "可愛"]

def pretty_print(author: str, msg: str):
    color = "cyan" if author == "你" else "magenta"
    time = datetime.now().strftime("[%H:%M]")
    text = Text(f"{time} {author}：{msg}", style=color)
    text.highlight_words(highlight_words, style="bold red")
    console.print(text)

# ===== Discord 初始化 =====
if sys.platform.startswith('win'):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)

channel_id = 1372877371471826946
start_msg = '他開啟留言功能'

@bot.event
async def on_ready():
    print(f'你上線了!!!')
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(start_msg)
        
        bot.loop.create_task(console_input_task(channel))  
    else:
        print("❌ 找不到頻道")

async def console_input_task(channel):
    re = []
    loop = asyncio.get_event_loop()

    async for ms in channel.history(limit=1000):
        re.append(f"{ms.author}: {ms.content}")
    re.reverse()
    
    for n in re:
        if start_msg in n or n.strip() == '':
            continue
        author, msg = n.split(":", 1)
        author = author.strip()
        msg = msg.strip()
        display_name = "你" if author == '留言#9166' else "他"
        pretty_print(display_name, msg)
    print('按Ctrl+c結束，打字即可輸入')
    while True:
        msg = await loop.run_in_executor(None, input, "")
        pretty_print("你", msg)

        # 小彩蛋機制
        if msg == "♡":
            await channel.send("你也太可愛了吧ww♡♡♡")
        else:
            await channel.send(msg)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    pretty_print("他", message.content)

@bot.command()
async def read_history(ctx):
    messages = []
    async for msg in ctx.channel.history(limit=50):  
        messages.append(f"{msg.author}: {msg.content}")
    await ctx.send("我看到這些訊息了：\n" + "\n".join(messages))

bot.run("MTM3Mjg3NDg5MjA1OTQ3NjA1OQ.GCYigA.UP5b5I38vJ3pIbgpsnsRyjkCzY7-J2d27MjmT8")
