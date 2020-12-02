import datetime
start_time = datetime.datetime.utcnow()
import discord
import os
import asyncio
import os.path
import json
import random
import time
from discord.ext import commands
intents = discord.Intents.default()
intents.members = True
intents.guilds = True
from dotenv import load_dotenv
load_dotenv()

from cogs.Channel import Channel
from cogs.Removal import Removal
from cogs.Permissions import Permissions

def is_allowed(ctx):
    return ctx.message.author.id == 655460372307771392

def is_server_owner(ctx):
    return ctx.message.author.id == ctx.guild.owner.id or ctx.message.author.id == 655460372307771392

client = commands.Bot(command_prefix=';;')

client.remove_command("help")

client.add_cog(Channel(client))
client.add_cog(Removal(client))
client.add_cog(Permissions(client))


@client.event
async def on_connect():
  print(f'''
   ██╗░██████╗░█████╗░  ██████╗░██████╗░
   ██║██╔════╝██╔══██╗  ╚════██╗╚════██╗
   ██║╚█████╗░██║░░██║  ░░███╔═╝░█████╔╝
   ██║░╚═══██╗██║░░██║  ██╔══╝░░░╚═══██╗
   ██║██████╔╝╚█████╔╝  ███████╗██████╔╝
   ╚═╝╚═════╝░░╚════╝░  ╚══════╝╚═════╝░ 
   
   Cached Users: {len(client.users)}
   Guilds: {len(client.guilds)}
   Prefix: {client.command_prefix}
   Creators: Zie#1200 & 4tacey | jayceez#0001
   Murda's Server : discord.gg/vanity
  ''')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Gamer(name=f"Watching{len(client.users)} Users"))
  await client.change_presence(activity=discord.Streaming(name="My Stream", url="https://www.twitch.tv/meekmill"))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
  print("ready")

async def ch_pr():
  await client.wait_until_ready()
  statuses = [".gg/vanity",f"Protecting {len(client.guilds)} Servers | Prefix: {client.command_prefix}","Forever Untouchable","OnTop Forever"]
  while not client.is_closed():
     status = random.choice(statuses)
     await client.change_presence(activity=discord.Streaming(name=status, url="https://www.twitch.tv/meekmill"))
     await asyncio.sleep(5)


client.loop.create_task(ch_pr())    

@client.event
async def on_guild_join(guild):
    with open ('prefixes.json', 'r') as f:
        prefixes = json.load(f)


    prefixes[str(guild.id)] = '>'
    
    with open ('prefixes.json', 'w') as f: 
        json.dump(prefixes , f, indent=4)

@client.event
async def on_guild_remove(guild):
     with open ('prefixes.json', 'r') as f:
        prefixes = json.load(f)


     prefixes.pop(str(guild.id))

     with open ('prefixes.json', 'w') as f: 
         json.dump(prefixes , f, indent=4)

@client.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
        
    prefixes[str(ctx.guild.id)] = prefix
    
    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)
        
    await ctx.send(f'Guild Prefix Changed To: ***{prefix}***')

@client.command(pass_context=True)
async def ping(ctx):
	ctx = ctx.message.ctx 
	t1 = time.perf_counter()
	await ctx.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping ・ {}'.format(round((t2-t1)*1000)), color=0x0504aa)
	await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    await ctx.send(embed=discord.Embed(title="Irregular Anti Nuke", description=f"{len(client.guilds)} servers, {len(client.users)} users | .gg/vanity | Made In Python"))
    await ctx.message.delete()

@client.command()   
async def setup(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=(0xffffff))
  embed = discord.Embed(description=f"**Irregular  Nuke**")
  embed.add_field(name="`Irregular Anti Nuke", value="Automatic Anti Nuke Created By Murda Members | Whitelist Commands Do Not Exist On This Anti", inline=False)
  embed.add_field(name="``[Creators]``", value=f"Made By <@655460372307771392> , <@751765280505593858> , and <@414127519319719936>", inline=False)
  embed.set_image(url='https://media.discordapp.net/attachments/778630594171109416/779068141572456458/image0.gif')
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
  await ctx.send(embed=embed)

@client.command()   
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=(0xffffff),description=f"**Irregular  Nuke**")
  embed.add_field(name="`Setup", value="setup Irregular  Nuke", inline=False)
  embed.add_field(name="`Mod", value="shows moderator menu", inline=False)
  embed.add_field(name="`Server",value="shows server commands")
  embed.add_field(name="`Invite", value="returns invite of Irregular ", inline=False)
  embed.set_image(url='https://media.discordapp.net/attachments/774419522987098164/777406191441412136/image1.gif')
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
  await ctx.send(embed=embed)  

@client.command()   
async def mod(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=(0xF9E29C),description=f"**Irregular  Nuke**")
  embed.add_field(name="`Ban", value="bans mentioned user", inline=False)
  embed.add_field(name="`Kick", value="kicks mentioned user", inline=False)
  embed.add_field(name="`Purge", value="deletes certain amount of messages", inline=False)
  embed.set_image(url='https://media.discordapp.net/attachments/774419522987098164/777409490059657226/image1.gif')
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
  await ctx.send(embed=embed) 

@client.command()   
async def server(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=(0xF9E29C),description=f"**Server Commands**")
  embed.add_field(name="`Whois", value="checks mentioned user's stats", inline=False)
  embed.add_field(name="`Serverinfo", value="checks server's info", inline=False)
  embed.add_field(name="`Ping", value="returns ping", inline=False)
  embed.set_image(url='https://media.discordapp.net/attachments/697225400505598044/783144406889922580/image0.gif')
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
  await ctx.send(embed=embed) 

@client.command()
async def invite(ctx):
  await ctx.message.delete()
  embed = discord.Embed(color=(0xffffff), timestamp=ctx.message.created_at)
  embed.title=("*IRREGULAR INVITE REQUESTED*")
  embed.set_thumbnail(url=ctx.guild.icon_url)
  embed.description=f"[INVITE LINK](https://discord.com/api/oauth2/authorize?client_id=776551517888446484&permissions=8&scope=bot)"
  embed.set_footer(text=f"{ctx.guild.name}", icon_url=ctx.guild.icon_url)
  embed.add_field(name="*Requested By*", value=f"{ctx.author.mention}")
  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=(0xF9E29C), timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been banned by {ctx.author.mention}"
  await member.ban()
  await ctx.send(embed=embed)

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, (commands.BadArgument)):
    embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
    embed.title=("ban error")
    embed.description=f"user was not found goofy,ping the right person next time"
    await ctx.send(embed=embed)
  else:
    raise error  

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member = None):
  if member is None:
     await ctx.send(f"{ctx.author.mention} you must mention a user to do that!")
  else:
   embed = discord.Embed(color=(0xF9E29C), timestamp=ctx.message.created_at)
  embed.description = f"{member.mention} has been kicked by {ctx.author.mention}"
  await member.kick()
  await ctx.send(embed=embed)

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, (commands.BadArgument)):
    embed = discord.Embed(color=0x0504aa, timestamp=ctx.message.created_at)
    embed.title=("ban error")
    embed.description=f"user was not found goofy,ping the right person next time"
    await ctx.send(embed=embed)
  else:
    raise error   

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, limit:int):
  await ctx.channel.purge(limit=limit)
  await ctx.send('Cleared by {}'.format(ctx.author.mention))
  await asyncio.sleep(3)
  await ctx.message.delete()

@client.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@client.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    if isinstance(ctx.message.channel, discord.Guild):
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Registered", value=user.created_at.strftime(date_format))
        em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        em.add_field(name="Join position", value=str(members.index(user) + 1))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            em.add_field(name="Roles [{}]".format(len(user.roles) - 1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        em.add_field(name="Permissions", value=perm_string, inline=False)
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)
    else:
        date_format = "%a, %d %b %Y %I:%M %p"
        em = discord.Embed(description=user.mention)
        em.set_author(name=str(user), icon_url=user.avatar_url)
        em.set_thumbnail(url=user.avatar_url)
        em.add_field(name="Created", value=user.created_at.strftime(date_format))
        em.set_footer(text='ID: ' + str(user.id))
        return await ctx.send(embed=em)

client.run("BOT TOKEN HERE")
