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
import re
import json
import math
import hikari
import lightbulb
from lib.weapons import *
from lib.consts import regex_map
from lightbulb.utils import pag, nav
from lib.fuse_results import str_to_wep, fuse_by_result, fuse_from_comb
from lib.embeds import fusion_embed, construct_pages, run_paginated_embed, calc_embed


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


@fusion_plugin.command()
@lightbulb.option("mod6", "Sixth modifier.", str, required=False)
@lightbulb.option("mod5", "Fifth modifier.", str, required=False)
@lightbulb.option("mod4", "fourth modifier.", str, required=False)
@lightbulb.option("mod3", "Third modifier.", str, required=False)
@lightbulb.option("mod2", "Second modifier.", str, required=False)
@lightbulb.option("mod1", "First modifier.", str, required=False)
@lightbulb.option("melee", "Melee stars.", str, required=False)
@lightbulb.option("ranged", "Ranged stars.", str, required=False)
@lightbulb.option("weapon", "Weapon name.", str, required=True)
@lightbulb.command("calc", "Calculator to determine weapon value.", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def calc(ctx: lightbulb.Context):
    name = ctx.options.weapon

    modlist = [
        ctx.options.mod1,
        ctx.options.mod2,
        ctx.options.mod3,
        ctx.options.mod4,
        ctx.options.mod5,
        ctx.options.mod6
    ]

    value = 100
    ranged = "0.0" if not ctx.options.ranged else str(float(ctx.options.ranged))
    melee = "0.0" if not ctx.options.melee else str(float(ctx.options.melee))

    with open("data/star_data.json") as data:
        star_data = json.load(data)

    value += star_data["ranged"][ranged]

    whole_star, half_star = ranged.split(".")
    ranged_stars = "\u2605" * int(whole_star)
    if int(half_star):
        ranged_stars += "\u2606"
    whole_star, half_star = melee.split(".")
    melee_stars = "\u2605" * int(whole_star)
    if int(half_star):
        melee_stars += "\u2606"

    with open("data/mod_data.json") as data:
        mod_data = json.load(data)

    mods = []
    for mod in modlist:
        if mod:
            mod_name, mod_attr = mod[:-2].lower().strip(), mod[-2:].strip()
            for mod in regex_map:
                mod_name = mod[1] if re.match(mod[0], mod_name) else mod_name
            value += mod_data[mod_name][mod_attr]

            mods.append(f"{mod_name.title()} {mod_attr}")
    mods = "\n".join(mods)

    value = str(math.floor(value))
    embed = calc_embed(name, ranged_stars, melee_stars, mods, value)

    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fusion_plugin)

