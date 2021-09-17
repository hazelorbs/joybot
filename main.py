import os
import discord
from discord.ext import commands
from keep_alive import keep_alive
import music
import random as rd

client = commands.Bot(command_prefix='~', intents = discord.Intents.all())

def choose_random(filepath): 
    file = open(filepath, 'r')
    list = file.readlines()
    file.close()
    index = rd.randint(1, len(list))
    return list[index - 1]

@client.event
async def on_ready():
  print("Successfully run")

cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)

@client.event
async def on_message(msg):
  if msg.author == client.user:
    return
  if msg.content.startswith('gm') or msg.content.startswith('Gm'):
    await msg.channel.send("gm")
  if msg.content.startswith('gn') or msg.content.startswith('Gn'):
    await msg.channel.send("gn")

  await client.process_commands(msg)
  
@client.command()
async def insult(ctx, arg):
  await ctx.send(arg + ', ' + choose_random('insults.txt').lower())

@client.command()
async def compliment(ctx, arg):
  await ctx.send(arg + ', ' + choose_random('compliments.txt').lower())

@client.command()
async def info(ctx):
  embedVar = discord.Embed(title="Joy Bot Info", description="Hi! I'm Joy Bot v2! Joy has finally let me out of her integration basement.", color=discord.Colour.dark_teal())
  embedVar.add_field(name="Commands", value="prefix: ~ \n \n Text Commands: \n gm \n gn \n quote \n nut \n embedfail \n youre \n spelling \n compliment {argument} \n insult {argument} \n e \n suicide \n \n Voice Commands: \n join \n play {argument} \n pause \n resume \n disconnect \n \n More commands to come!", inline=False)
  await ctx.send(embed=embedVar)

@client.command()
async def quote(ctx):
  await ctx.send(choose_random('quotes.txt'))

@client.command()
async def embedfail(ctx):
  await ctx.send(choose_random('embedfail.txt'))

@client.command()
async def youre(ctx):
  await ctx.send(choose_random('youre.txt'))

@client.command()
async def spelling(ctx):
  await ctx.send(choose_random('spellingmistake.txt'))

@client.command()
async def nut(ctx):
  await ctx.send('https://tenor.com/view/deez-nuts-chungus-reddit-cum-gif-18654257')

@client.command()
async def suicide(ctx):
  await ctx.send('https://tenor.com/view/cat-gif-18549716')

keep_alive()
