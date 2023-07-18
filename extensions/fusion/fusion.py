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
import hikari
from lightbulb.utils import pag, nav
from lib.embeds import fusion_embed, construct_pages, run_paginated_embed
from lib.weapons import *
from lib.fuse_results import str_to_wep, fuse_by_result, fuse_from_comb

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


@fusion_plugin.command()
@lightbulb.option("weapon", "One weapon in the fusion.", str, required=False)
@lightbulb.option("result", "The result of the fusion.", str, required=False)
@lightbulb.option("group", "The group of the resulting fusion.", str, required=False)
@lightbulb.command("search", "Displays possible fusions depending on the input given.", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def search(ctx: lightbulb.Context):
    weapon = ctx.options.weapon
    result = ctx.options.result
    group = ctx.options.group

    try:
        if weapon: weapon = str_to_wep(weapon)
        if result: result = str_to_wep(result)
    except ValueError:
        await ctx.respond("Please enter a valid weapon or result")

    if group:
        try:
            group = int(group)
            if 1 > group > 5:
                raise ValueError
        except:
            await ctx.respond("Please enter a valid fusion group.")

    if (weapon and result) and not group:
        res_list = []
        fuse_from_comb(weapon, result, res_list)
        message = construct_pages(res_list)
        await run_paginated_embed(ctx, message, ":sparkles: Search by Weapon and Result :sparkles:")
        return

    elif (weapon and group) and not result:
        res_list = []
        fuse_from_comb(weapon, group, res_list)
        message = construct_pages(res_list)
        await run_paginated_embed(ctx, message, ":sparkles: Search by Weapon and Group :sparkles:")
        return

    elif weapon and not (result and group):
        res_list = []
        fuse_from_comb(weapon, None, res_list)
        message = construct_pages(res_list)
        await run_paginated_embed(ctx, message, ":sparkles: Search by Weapon :sparkles:")
        return

    elif result and not (weapon and group):
        results = fuse_by_result(result)
        message = construct_pages(results)
        await run_paginated_embed(ctx, message, ":sparkles: Search by Result :sparkles:")
        return

    elif (result and group) and not weapon:
        results = fuse_by_result(result, group=group)
        message = construct_pages(results)
        await run_paginated_embed(ctx, message, ":sparkles: Search by Result and Group :sparkles:")
        return

    elif group and not (weapon and result):
        results = fuse_by_result(group)
        message = construct_pages(results)
        await run_paginated_embed(ctx, message, ":sparkles: Search by Group :sparkles:")
        return

    else:
        await ctx.respond("Cannot search by weapon only.")

def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fusion_plugin)

