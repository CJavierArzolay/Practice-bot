import os
from dotenv import load_dotenv
from discord.ext import commands, tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

CANAL_INICIAL = "459184090219020288"

bot = commands.Bot(command_prefix="?")

@bot.command(name="+")
async def sumar(ctx, a, b):
	if ctx.message.channel.mention[2:-1] == CANAL_INICIAL:
		await ctx.send(f"the result is: {int(a) + int(b)}")

@bot.command(name="x")
async def mult(ctx, a, b):
	await ctx.send(f"the result is: {int(a) * int(b)}")

@tasks.loop(minutes = 6)
async def taskly(channel):
	await channel.send("la persona que escriba arriba es etero, y guapo/a")

@bot.event
async def on_ready():
    channel = bot.get_channel(459184090219020288)
    taskly.start(channel=channel)

bot.run(TOKEN)
	