import os
import discord
from discord.ext import commands

def main():
  token = os.getenv("DISCORD_TOKEN")
  
  initial_extensions = [
    'cogs.commands.HelloWorld'
  ]

  intents = discord.Intents.all()

  tenko = commands.Bot(intents=intents)

  for extension in initial_extensions:
    try:
      tenko.load_extension(extension)
    except Exception as e:
      print(e)

  tenko.run(token, reconnect=True)

if __name__ == "__main__":
  main()
