import discord
from discord.ext import commands
import datetime

class Removal(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        async for i in guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.ban):
            
            await guild.ban(i.user, reason="Anti Nuke")

    @commands.Cog.listener()
    async def on_member_remove(self, member, guild):
        async for i in member.guild.audit_logs(limit=1, after=datetime.datetime.now() - datetime.timedelta(minutes = 2), action=discord.AuditLogAction.kick):   
            if i.target.id == member.id:
                await guild.ban(i.user, reason="Anti Nuke")
                return
