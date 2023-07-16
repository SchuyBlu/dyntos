import lightbulb
from lib.weapons import *

fusion_plugin = lightbulb.Plugin("fusion", "Shows the result of a fusion")

@fusion_plugin.command()
@lightbulb.option("second", "The second weapon in the fusion", str, required=True)
@lightbulb.option("first", "The first weapon in the fusion", str, required=True)
@lightbulb.command("fusion", "Displays the result of a fusion.")
@lightbulb.implements(lightbulb.SlashCommand)
async def fusion(ctx: lightbulb.Context):
    first = str_to_wep(ctx.options.first)
    second = str_to_wep(ctx.options.second)

    res = first.fusion(second)
    await ctx.respond(f"{str(first).title()} + {str(second).title()} = {str(res[0]).title()} in group {res[1]}")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fusion_plugin)

