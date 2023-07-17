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
import json

def fusion_embed(first, second, result, group):
    with open("data/weapon_images.json") as data:
        weapon_images = json.load(data)
    image = weapon_images[str(result)]

    new_embed = (
        hikari.Embed(
            title = ":sparkles: Weapon Fusion Result :sparkles:",
            description = "Listed below are the fusion results.",
            color = hikari.Color(0x7D00FF),
        )
        .set_image(image)
        .add_field(
            name = "Weapon 1",
            value = f"{str(first).title()}",
            inline = True,
        )
        .add_field(
            name = "Weapon 2",
            value = f"{str(second).title()}",
            inline = True,
        )
        .add_field(
            name = "Result",
            value = f"{str(result).title()}",
            inline = False,
        )
        .add_field(
            name = "Fusion Group",
            value = f"Group {group}",
            inline = False,
        )
    )
    return new_embed

