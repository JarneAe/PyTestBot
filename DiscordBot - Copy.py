import discord
from discord.ext import commands, tasks 

import random
from random import choice
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Doin\' your mom.'))
    print('Bot is ready.')
    
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'EightBall', '8Ball'])
async def _8Ball(ctx, *, question ):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.','Yes - Definetly!', 'You may rely on it.','Yes.','Ask again later.','Concentrate and ask again.','Don\'t count on it','My sources say no.', 'Very doubtful.', 'Outlook not so good.', 'My reply is no.','I have no idea. Try again.']
    await ctx.send(f'Question: {question}\n Answer: {random.choice(responses)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(str(amount) + f' Messages cleared!')

@client.command(aliases=['randomnumber','random'])
async def randomnum(ctx):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    await ctx.send(f'You\'re random number is:  {random.choice(numbers)}')

@client.command()
async def kick(ctx, member : discord.Member, *, Reason=None):
    await member.kick(reason=Reason)

@client.command()
async def ban(ctx, member : discord.Member, *, Reason=None):
    await member.ban(reason=Reason)

@client.command()
async def load(ctx, extension):
    client.load_extensions()

@client.command()
async def isgay(ctx, member: discord.Member ):
    yesno =['is gay!','isn\'t gay!']
    await ctx.send(f'@{member} {random.choice(yesno)}')










client.run('NzUyMjA3NDIwNTk1NjM0Mjc3.X1URwA.SMjZp5t-SvtfulMOeJxwZ4uqwHE')



