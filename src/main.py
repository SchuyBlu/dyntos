"""--------------------------------------------------------------------
Author: Feanor
Discord bot for the Kid Icarus Uprising Multiplayer server.
--------------------------------------------------------------------"""
import hikari
import lightbulb
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = str(getenv("TOKEN")) # convert to str as per lightbulb reqs

bot = lightbulb.BotApp(
    TOKEN, prefix = "$",
    intents = hikari.Intents.ALL,
    help_class = None
)

bot.run(
    activity = hikari.Activity(name = "/help or $help")
)

