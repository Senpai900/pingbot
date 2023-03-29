import disnake
from disnake.ext import commands, tasks

bot = commands.Bot(intents=disnake.Intents.all())
channel = int(open("channel.txt", "r").read().strip())
text = open("text.txt", "r").read().strip()


@bot.event
async def on_ready():
    loop.start()
    print("ready")


@bot.command()
async def channel(ctx, channel_: disnake.TextChannel):
    global channel
    channel = channel_.id
    with open("channel.txt", "w") as f:
        f.write(str(channel_.id))
    await ctx.send("ок")


@bot.command()
async def text(ctx, *, text_: str):
    global text
    text = text_
    with open("text.txt", "w") as f:
        f.write(str(text_))
    await ctx.send("ок")


@tasks.loop(minutes=10)
async def loop():
    channel_i = await bot.fetch_channel(channel)
    await channel_i.send(text, delete_after=2)

bot.run("")
