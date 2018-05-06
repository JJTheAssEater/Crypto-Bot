# Made by JJ // Octuplet

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk
import time

bot = commands.Bot(command_prefix='#')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! pong!!")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I found.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I found.", color=0x00ff00)
    embed.set_author(name="CryptoBot")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("ðŸ˜‚ðŸ‘Œ Friends")
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya loser!".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="Chat Rules", description="Restrain from racial slurs and from posting incredibly disgusting videos or pictures.", color=0x00ff00)
    embed.set_footer(text="Please enjoy our server while following these few simple rules.")
    embed.set_author(name="")
    embed.add_field(name="Voice Chat Rules", value="No mic spamming or anything of that sort.", inline=True)
    await bot.say(embed=embed)

bot.run("NDQyNTM0MzAzOTgxNjMzNTQ3.DdAWpQ.bfSBMl22L46_Vx-RgS9quPl2gxY")
