# MIT License
#
# Copyright (c) 2023 Schuy
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
import json
import hikari
import lightbulb


chapter_plugin = lightbulb.Plugin("Chapter", "Collection of solo commands")

@chapter_plugin.command()
@lightbulb.option("member", "Member whose score is being registered.", hikari.User, required=True)
@lightbulb.option("score", "The score being added.", int, required=True)
@lightbulb.option("chapter", "The chapter the score was acheived for.", str, required=True)
@lightbulb.command("score", "Allows moderators to add scores for users.")
@lightbulb.implements(lightbulb.SlashCommand)
async def score(ctx: lightbulb.Context):
    score = ctx.options.score

    has_permission = False
    for role in ctx.member.get_roles():
        is_secretary = (role.name == "Point Secretary and Spreader of Sheets")
        is_admin = (role.permissions.ADMINISTRATOR)
        if is_secretary or is_admin:
            has_permission = True

    if not has_permission:
        await ctx.respond("Only admins and volunteers are allowed to use this command.")
        return

    member = ctx.get_guild().get_member(ctx.options.member)
    member_id = str(member.id)

    with open("data/chapter_data.json") as data:
        chapter_data = json.load(data)

    if ctx.options.chapter not in list(chapter_data.keys()):
        await ctx.respond(f"{ctx.options.chapter} is not a chapter.")
        return

    chapter = chapter_data[ctx.options.chapter]

    leaderboard = chapter["leaderboard"]
    for record in leaderboard:
        if record.split()[0] == member_id:
            leaderboard.remove(record)
            break
    leaderboard.append(f"{member_id} {score}")

    # Replaces existing leaderboard list with one that is sorted
    # by the score
    chapter_data[ctx.options.chapter]["leaderboard"] = sorted(leaderboard, key=lambda x: int(x.split()[-1]), reverse=True)

    with open("data/chapter_data.json", "w") as data:
        json.dump(chapter_data, data, indent=2)

    await ctx.respond(f"{member.display_name}'s score of {score} has been added!")


@chapter_plugin.command()
@lightbulb.option("chapter", "The chapter you want information on.", required=True)
@lightbulb.command("chapter", "Retrieve chapter information.")
@lightbulb.implements(lightbulb.SlashCommand)
async def chapter(ctx: lightbulb.Context):

    with open("data/chapter_data.json") as data:
        chapter_data = json.load(data)

    if ctx.options.chapter not in list(chapter_data.keys()):
        await ctx.respond("An existing chapter must be entered.")
        return

    chapter = chapter_data[ctx.options.chapter]

    title = chapter["name"]
    weapons = chapter["weapons"]
    img = chapter["img"]

    raw_leaderboard = chapter["leaderboard"]
    leaderboard = ""
    retrieved = 1
    for raw_score in raw_leaderboard:
        member_id, score = raw_score.split()
        member = ctx.get_guild().get_member(int(member_id))
        if member:
            mem_name = member.nickname if member.nickname else member.username
            leaderboard += f"{retrieved}. {mem_name}: {score}\n"
        if retrieved == 5: break
        retrieved += 1

    embed = (
        hikari.Embed(
            title = title,
            description = f"Drop data and leaderboards for {title}!",
            color = hikari.Color(0x7D00FF),
        )
        .set_thumbnail(img)
        .add_field(
            name = "Weapon Drops",
            value = weapons,
            inline = True
        )
    )
    if leaderboard:
        embed.add_field(
            name = "Leaderboards",
            value = leaderboard,
            inline = True
        )

    await ctx.respond(embed)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(chapter_plugin)

