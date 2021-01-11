import discord
from discord.ext import commands
from config import TOKEN, PREFIX

client = commands.Bot(command_prefix=PREFIX)


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid Command.")


@client.command(aliases=['test'])
async def Test(ctx):
    await ctx.send("This is a command test.")


@client.command()
async def embed(ctx):
    embed = discord.Embed(
        title="This is a Title",
        description="This is a Description",
        colour=discord.Colour.blue()
    )

    embed.set_author(name="Author Name")
    embed.set_footer(text="Developed By Aco")
    embed.add_field(name="Field Name 1", value="Field Value 1", inline=True)
    embed.add_field(name="Field Name 2", value="Field Value 2", inline=True)
    embed.add_field(name="Field Name 3", value="Field Value 3", inline=True)

    await ctx.send(embed=embed)


client.run(TOKEN)
