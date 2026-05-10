import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
import discord
from discord.ext import commands
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hey {ctx.author.mention}!')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong! 🏓')

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)

@bot.command()
async def flip(ctx):
    result = random.choice(['Heads! 🪙', 'Tails! 🪙'])
    await ctx.send(result)

@bot.command()
async def info(ctx):
    embed = discord.Embed(
        title=f'{ctx.guild.name} Info',
        color=discord.Color.blue()
    )
    embed.add_field(name='Members', value=ctx.guild.member_count)
    embed.add_field(name='Owner', value=ctx.guild.owner)
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f'Kicked {member.name}!')



@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)


@bot.command()
@commands.has_permissions(administrator=True)
async def makeadmin(ctx, member: discord.Member):
    # Get the admin role
    role = discord.utils.get(ctx.guild.roles, name='ADMIN')

    # Give it to them
    await member.add_roles(role)
    await ctx.send(f'{member.mention} is now an Admin!')

@bot.command()
@commands.has_permissions(administrator=True)
async def clearmsg(ctx,amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'deleted {amount} messages!')
load_dotenv()
bot.run(os.getenv('TOKEN'))

