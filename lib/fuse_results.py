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
from lib.weapons import *


def str_to_wep(string):
    ret = None
    match string.split()[-1].lower():
        case "blade": ret = Blade(string)
        case "staff": ret = Staff(string)
        case "claws": ret = Claws(string)
        case "bow": ret = Bow(string)
        case "palm": ret = Palm(string)
        case "club": ret = Club(string)
        case "cannon": ret = Cannon(string)
        case "orbitars": ret = Orbitars(string)
        case "arm": ret = Arm(string)
    # Raise value error if weapon does not exist
    if not ret:
        raise ValueError("Weapon must exist.")
    return ret


def slice_wep_list(input_list):
    return [input_list[i:i+12] for i in range(0, len(input_list), 12)]


def append_by_weapon(wep1, wep2, output):
    wep2 = str_to_wep(wep2)
    res, group = wep1.fusion(wep2)
    output.append([wep1, wep2, res, group])


def append_by_result(wep1, wep2, desired, output):
    wep2 = str_to_wep(wep2)
    res, group = wep1.fusion(wep2)
    if res == desired:
        output.append([wep1, wep2, res, group])


def append_by_group(wep1, wep2, desired, output):
    wep2 = str_to_wep(wep2)
    res, group = wep1.fusion(wep2)
    if group == desired:
        output.append([wep1, wep2, res, group])


def fuse_from_comb(wep, desired, output, skip=None):
    for category in slice_wep_list(Weapon().WEAPONS):
        for weapon in category:

            # This skips all weapons whose fusions have already been recorded.
            if skip and weapon in skip: continue

            if not desired:
                append_by_weapon(wep, weapon, output)

            elif not isinstance(desired, int):
                append_by_result(wep, weapon, desired, output)
            elif isinstance(desired, int):
                append_by_group(wep, weapon, desired, output)


def fuse_by_result(desired, group=None):
    results = []
    skip = []
    for category in slice_wep_list(Weapon().WEAPONS):
        for weapon in category:
            weapon = str_to_wep(weapon)
            fuse_from_comb(weapon, desired, results, skip)
            skip.append(str(weapon))

    # If group is set, create a new list with the correct fuses
    if group:
        results = [x for x in results if x[-1] == group]
    return results

