import discord
from discord.commands import SlashCommandGroup, option, slash_command
from discord.ext import commands
# import traceback

class HelloWorldCommand(commands.Cog):
  def __init__(self, bot: discord.Bot):
    self.bot = bot


  @commands.slash_command(name="helloworld", description="Hello world!", guild_only=True)
  async def hello_world(self, ctx: discord.ApplicationContext):
    await ctx.respond(f"Hello world!")


  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot is online!")

  # @commands.Cog.listener()
  # async def on_message(self, message):
  #   print(f"[@{message.guild}#{message.channel}] {message.author}: {message.content}")



def setup(bot):
  bot.add_cog(HelloWorldCommand(bot))
