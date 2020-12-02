import discord
from discord.ext import commands
import datetime

class Channel(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        async for i in channel.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.channel_delete):
            await channel.guild.ban(i.user)
            return

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        async for i in channel.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.channel_create):

            await i.user.ban()
            return
            
