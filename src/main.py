import random
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 756509074773901394  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


@bot.command(name='name') 
async def message_name(ctx):
    
    response = f'{ctx.message.author.name}'
    await ctx.send(response)

@bot.command(name='d6')
async def random6(ctx):
    random_6 = [
        '1',
        '2',
        '3',
        '4',
        '5',
        '6'
        ]

    response = random.choice(random_6)
    await ctx.send(response)


@bot.event
async def on_message(message):
     if "Salut tout le monde" in message.content :
        response = "Salut tout seul "
        response2 = f'{message.author.mention}'
        await message.channel.send(response + response2)
     await bot.process_commands(message)




#@bot.command(name='admin')
#async def role_admin(ctx):
#    member = ctx.message.content[7:]
#    print(member)
    
#    ctx.author.get_member()
#    roles = ctx.member.roles
#    role_names = [role.name for role in roles]

#    print(role_names)
#    await ctx.send(f'')
    # Member object that you want to add the role to
#    role = discord.utils.get(lambda role: role.name == "Admin", ctx.guild.roles) # The role object
#    await member.add_roles(role) # Adds the role to the member

#    ctx.author.get_member()
#    roles = ctx.author.roles
#    role_names = [role.name for role in roles]
#    is_member = 'Admin' in role_names

#    if is_member :
#        return await ctx.send("You are verified")

#    member_role = discord.utils.get(ctx.guild.roles, name='Admin')

#    if ctx.author.roles != "admin" :
#    await ctx.author.add_roles(member_role)
#    await ctx.send(f"{ctx.author.mention} you are now verified") 

@bot.command(name='ban')
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Oh oh {ctx.author.mention} don't provide a reason!")
    else:
        messageok = f"You have been banned from {ctx.guild.name} for {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)



@bot.command()
async def pong(ctx):
    await ctx.send()

token = "MTAyMjE5MjcyMjY4MzExNzYxOA.GSaGsk.epEV1fN2YsNpa5_6T3Xhykdp5f4wXdqBvo1C7Y"
bot.run(token)  # Starts the bot