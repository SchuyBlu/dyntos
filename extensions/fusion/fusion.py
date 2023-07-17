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
import lightbulb
from lib.embeds import fusion_embed
from lib.weapons import *
from lib.fuse_results import str_to_wep

fusion_plugin = lightbulb.Plugin("fusion", "Shows the result of a fusion")

@fusion_plugin.command()
@lightbulb.option("second", "The second weapon in the fusion", str, required=True)
@lightbulb.option("first", "The first weapon in the fusion", str, required=True)
@lightbulb.command("fusion", "Displays the result of a fusion.", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def fusion(ctx: lightbulb.Context):
    try:
        first = str_to_wep(ctx.options.first)
        second = str_to_wep(ctx.options.second)
    except ValueError:
        await ctx.respond("Please enter a valid weapon.")
        return

    res, group = first.fusion(second)

    embed = fusion_embed(first, second, res, group)
    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fusion_plugin)

