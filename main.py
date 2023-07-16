# MIT License
#
# Copyright (c) 2023 Feanor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import hikari
import lightbulb
from os import getenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = str(getenv("TOKEN")) # convert to str as per lightbulb reqs

extensions = [
    "src/extensions/fusion",
]

bot = lightbulb.BotApp(
    TOKEN, prefix = "$",
    intents = hikari.Intents.ALL,
    help_class = None
)

for extension in extensions:
    bot.load_extensions_from(extension, must_exist=True)
bot.run(
    activity = hikari.Activity(name = "/help or $help")
)

