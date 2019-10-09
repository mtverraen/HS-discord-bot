# main.py
import os
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.ext import commands
import firebase_lib
import wechall_lib

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = Bot(command_prefix="!")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command(name='scoreboard', help='returns the wechall scoreboard for Helt Sikker members')
async def scoreboard(ctx):
    response = wechall_lib.build_scoreboard(firebase_lib.get_discord_users())
    await ctx.send(response)


@bot.command(name='addme', help="use: '!addme player_name'")
async def addme(ctx, we_chall):
    if firebase_lib.does_discord_user_exist(ctx.message.author.name) is not None or ctx.message.author.bot:
        await ctx.send(ctx.message.author.name + " already exist, or is a bot.")
        return
    else:
        firebase_lib.add_user_as_document(ctx.message.author.name, we_chall)
        response = "Added " + we_chall+" to the score board"
        await ctx.send(response)


@bot.command(name='deleteme', help='removes you from the HS wechall DB')
async def deleteme(ctx):
    if firebase_lib.does_discord_user_exist(ctx.message.author.name) is None or ctx.message.author.bot:
        await ctx.send(ctx.message.author.name +" does not exist in the DB, or is a bot.")
        return
    else:
        firebase_lib.delete_user(ctx.message.author.name)
        response = "Deleted user: " + ctx.message.author.name
        await ctx.send(response)


@bot.command(name='sites', help="use:'sites player_name' displays the ctfs a player has linked on wechall")
async def sites(ctx, player_name):
    response=wechall_lib.get_sites(player_name)
    await ctx.send(response)

bot.run(TOKEN)

