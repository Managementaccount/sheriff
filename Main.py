import discord
from discord.ext import commands
import keep_alive

bot = commands.Bot(command_prefix="!")
   
@bot.command()
async def ban(ctx, member: discord.Member, *, reason):
  await ctx.guild.ban(member, reason=reason)
  await ctx.send(f"{member} was banned for " + reason)

@bot.event
async def on_member_join(member):
  role = get(member.guild.roles, id=role_id)
  await member.add_roles(role)
  channel = bot.get_channel(636399538650742795)
  await channel.message.send(f"what's up my boy {member}")

@bot.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	
	member_name, member_discriminator = member.split('#')
	for ban_entry in banned_users:
		user = ban_entry.user
		
		if (user.name, user.discriminator) == (member_name, member_discriminator):
 			await ctx.guild.unban(user)
 			await ctx.channel.send(f"Unbanned: {user.mention}")

@bot.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

@bot.event
async def on_ready():
    print("bot is ready")

keep_alive.keep_alive()

bot.run("OTk3MjEwNjQ2OTI2MDczOTI2.GdWLJl.6BYc9pp5FN2UWvP9pzYtauYW5s8LbAsAxFmCnw")
