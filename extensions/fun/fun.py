import json
import random
import hikari
import lightbulb
from PIL import Image
import urllib.request
from io import BytesIO
from lightbulb.commands.base import OptionModifier


fun_plugin = lightbulb.Plugin("fun")

@fun_plugin.command()
@lightbulb.option("slapped", "Who you want to slap.", hikari.User, required=True)
@lightbulb.command("slap", "Slap someone!", auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def slap(ctx: lightbulb.Context):
    member = ctx.get_guild().get_member(ctx.options.slapped)
    user = ctx.member

    member_img = str(member.avatar_url)
    req = urllib.request.Request(member_img, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        img = r.read()

    user_img = str(user.avatar_url)
    req = urllib.request.Request(user_img, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as r:
        img2 = r.read()

    file1 = BytesIO(img)
    file2 = BytesIO(img2)

    batman = Image.open("data/images/batman_slap.jpg")

    mem_img1 = Image.open(file1).resize((256, 256), Image.LANCZOS)
    mem_img2 = Image.open(file2).resize((256, 256), Image.LANCZOS)

    batman.paste(mem_img1, (320, 235))
    batman.paste(mem_img2, (735, 60))
    output = BytesIO()
    batman.save(output, format="jpeg")
    output.seek(0)

    await ctx.respond(hikari.Bytes(output, "batslap.jpg"))

    batman.close()
    file1.close()
    file2.close()


@fun_plugin.command()
@lightbulb.option("text", "Text to be uwuified.", str, required=True, modifier=OptionModifier.CONSUME_REST)
@lightbulb.command("uwuify", "Uwuifies text.")
@lightbulb.implements(lightbulb.SlashCommand)
async def uwuify(ctx: lightbulb.Context):
    if len(ctx.options.text) > 2000:
        await ctx.respond("Message needs to be under 2000 characters.")
        return

    with open("data/asterisk_options.json") as data:
        asterisk = json.load(data)

    text_list = ctx.options.text.split()
    for i, word in enumerate(text_list):
        match word:
            case "my": text_list[i] = "mwy"
            case "to": text_list[i] = "tuwu"
            case "had": text_list[i] = "hawd"
            case "you": text_list[i] = "yuw"
            case "go": text_list[i] = "gow"
            case "and": text_list[i] = "awnd"
            case "have": text_list[i] = "haw"
            case other:
                word = word.replace("ll", "w").replace("r", "w")
                word = word.replace("l", "w").replace("th", "d")
                word = word.replace("fu", "fwu").replace("y", "wy")
                text_list[i] = word

        if random.randrange(0, 11) == 1:
            text_list[i] = word[0] + "-" + word

        if any([char in word for char in [".", "!", "?"]]):
                text_list[i] = text_list[i] + " " + random.choice(asterisk)

    message = " ".join(text_list)
    await ctx.respond(message)


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(fun_plugin)
