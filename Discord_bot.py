import discord
from discord.ext import commands
from discord.ext.tasks import loop
from discord.utils import get
from discord.iterators import ReactionIterator
import sys, traceback
from datetime import datetime, timedelta
import time
from collections import Counter
from random import shuffle, randint

client = discord.Client()
bot = commands.Bot(command_prefix='.', case_insensitive=True, description='')

@bot.event
async def on_ready():
    print(f'Successfully logged in as: {bot.user.name} - {bot.user.id}')
    await bot.change_presence(activity=discord.Game(name="I'm a sweet girl"))

    if bot.guilds.count == 0:
        print("It's in no guilds!")
    else:
        for x in bot.guilds:
            print(f'{x.id} - {x}')
    
@commands.has_permissions(administrator=True)
@bot.command(name='dm')
async def dmall(ctx, *args):      
    args = list(args)
    msg = ''
    for x in args:
        msg += (x + ' ')
    server = ctx.guild
    
    users = server.members
    shuffle(users)
    for user in users:
        try:
            if user.dm_channel is None:
                await user.create_dm()
            await user.dm_channel.send(f'{msg}')
        except: 
            pass
    print("Done!")

@bot.command(name='dmall')
async def dmdmall(ctx, *args):      
    args = list(args)
    server = bot.get_guild(int(args.pop(0)))
    msg = ''
    for x in args:
        msg += (x + ' ')
    
    users = server.members
    shuffle(users)
    for user in users:
        try:
            if user.dm_channel is None:
                await user.create_dm()
            await user.dm_channel.send(f'{msg}')
        except: 
            pass
    print("Done!")

bot.run("NjY3ODUzNTc3MTYyODUwMzE0.XiVw1Q.5psFbPvWjDqvx6UuFrCcKL3oyHs", bot=True)
