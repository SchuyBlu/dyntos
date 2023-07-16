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
class Weapon:
    def __init__(self, name=None):
        self.WEAPONS = [
            "first blade",
            "burst blade",
            "viper blade",
            "crusader blade",
            "royal blade",
            "optical blade",
            "samurai blade",
            "bullet blade",
            "aquarius blade",
            "aurum blade",
            "palutena blade",
            "gaol blade",

            "insight staff",
            "orb staff",
            "rose staff",
            "knuckle staff",
            "ancient staff",
            "lancer staff",
            "flintlock staff",
            "somewhat staff",
            "scorpio staff",
            "laser staff",
            "dark pit staff",
            "thanatos staff",

            "tiger claws",
            "wolf claws",
            "bear claws",
            "brawler claws",
            "stealth claws",
            "hedgehog claws",
            "raptor claws",
            "artillery claws",
            "cancer claws",
            "beam claws",
            "viridi claws",
            "pandora claws",

            "fortune bow",
            "silver bow",
            "meteor bow",
            "divine bow",
            "darkness bow",
            "crystal bow",
            "angel bow",
            "hawkeye bow",
            "sagittarius bow",
            "aurum bow",
            "palutena bow",
            "phosphora bow",

            "violet palm",
            "burning palm",
            "needle palm",
            "midnight palm",
            "cursed palm",
            "cutter palm",
            "pudgy palm",
            "ninja palm",
            "virgo palm",
            "aurum palm",
            "viridi palm",
            "great reaper palm",

            "ore club",
            "babel club",
            "skyscraper club",
            "atlas club",
            "earthmaul club",
            "ogre club",
            "halo club",
            "black club",
            "capricorn club",
            "aurum club",
            "hewdraw club",
            "magnus club",

            "ez cannon",
            "ball cannon",
            "predator cannon",
            "poseidon cannon",
            "fireworks cannon",
            "rail cannon",
            "dynamo cannon",
            "doom cannon",
            "leo cannon",
            "sonic cannon",
            "twinbellows cannon",
            "cragalanche cannon",

            "standard orbitars",
            "guardian orbitars",
            "shock orbitars",
            "eyetrack orbitars",
            "fairy orbitars",
            "paw pad orbitars",
            "jetstream orbitars",
            "boom orbitars",
            "gemini orbitars",
            "aurum orbitars",
            "centurion orbitars",
            "arlon orbitars",

            "crusher arm",
            "compact arm",
            "electroshock arm",
            "volcano arm",
            "drill arm",
            "bomber arm",
            "bowl arm",
            "end-all arm",
            "taurus arm",
            "upperdash arm",
            "kraken arm",
            "phoenix arm"
        ]

        if name:
            self.name = " ".join(name.lower().split()[:-1])
            self.type = name.lower().split()[-1]
            if not self._valid(name):
                raise ValueError("Weapon must exist")

    def __str__(self):
        return f"{self.name} {self.type}"

    def __eq__(self, other):
        # Check all related values to ensure both weapons are truly identical
        if (
            str(self) == str(other) and self.cid == other.cid and
            self.id == other.id and self.tid == other.tid
        ):
            return True
        return False

    def _valid(self, name):
        if name.lower() in self.WEAPONS:
            return True
        return False

    def _init_weapon_by_offset(self, name, cid, wid, offset):
        if wid and not name:
            self.name = " ".join(self.WEAPONS[offset + wid - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wid - 1].split()[-1]
            self.id = wid
        else:
            self.id = self.WEAPONS.index(f"{str(self)}") - offset + 1
        self.tid = (self.cid * 12) + self.id

    def _retrieve_fusion_group(self, other):
        unmatched_group = abs(self.tid - other.tid) % 5
        match unmatched_group:
            case 0:
                matched_group = 2
            case 1:
                matched_group = 4
            case 2:
                matched_group = 3
            case 3:
                matched_group = 1
            case 4:
                matched_group = 5
        return matched_group

    def _assign_from_table(self, other, wid):
        result_table = [
        [Claws(wid=wid),   Claws(wid=wid), Club(wid=wid),     Palm(wid=wid),    Arm(wid=wid),   Staff(wid=wid),   Staff(wid=wid),  Palm(wid=wid),     Bow(wid=wid)],
        [Claws(wid=wid),  Cannon(wid=wid),  Arm(wid=wid),      Arm(wid=wid), Cannon(wid=wid),   Claws(wid=wid),   Blade(wid=wid),  Club(wid=wid),Orbitars(wid=wid)],
        [ Club(wid=wid),     Arm(wid=wid), Club(wid=wid),     Club(wid=wid),    Arm(wid=wid),     Bow(wid=wid),     Bow(wid=wid), Staff(wid=wid),   Staff(wid=wid)],
        [ Palm(wid=wid),     Arm(wid=wid), Club(wid=wid),   Cannon(wid=wid),   Club(wid=wid),    Palm(wid=wid),Orbitars(wid=wid),Cannon(wid=wid),   Blade(wid=wid)],
        [  Arm(wid=wid),  Cannon(wid=wid),  Arm(wid=wid),     Club(wid=wid),    Arm(wid=wid),   Blade(wid=wid),   Blade(wid=wid),   Bow(wid=wid),Orbitars(wid=wid)],
        [Staff(wid=wid),   Claws(wid=wid),  Bow(wid=wid),     Palm(wid=wid),  Blade(wid=wid),Orbitars(wid=wid),Orbitars(wid=wid), Claws(wid=wid),   Blade(wid=wid)],
        [Staff(wid=wid),   Blade(wid=wid),  Bow(wid=wid),Orbitars(wid=wid),   Blade(wid=wid),Orbitars(wid=wid),    Palm(wid=wid), Claws(wid=wid),   Staff(wid=wid)],
        [ Palm(wid=wid),    Club(wid=wid),Staff(wid=wid),  Cannon(wid=wid),     Bow(wid=wid),   Claws(wid=wid),   Claws(wid=wid),Cannon(wid=wid),    Palm(wid=wid)],
        [  Bow(wid=wid),Orbitars(wid=wid),Staff(wid=wid),   Blade(wid=wid),Orbitars(wid=wid),   Blade(wid=wid),   Staff(wid=wid),  Palm(wid=wid),     Bow(wid=wid)]]

        return result_table[self.cid][other.cid]

    def _assign_from_exception_table(self, other):
        ret = None
        exception_table = [
            [   Blade(wid=1), Orbitars(wid=11),      Bow(wid=11)],
            [   Blade(wid=7),      Club(wid=5), Orbitars(wid=12)],
            [   Staff(wid=3),  Orbitars(wid=4),     Blade(wid=7)],
            [   Staff(wid=4),       Arm(wid=8),    Blade(wid=12)],
            [   Staff(wid=8),      Palm(wid=9),      Arm(wid=10)],
            [  Staff(wid=11),       Bow(wid=1),    Blade(wid=11)],
            [   Claws(wid=5),      Palm(wid=1),    Cannon(wid=6)],
            [   Claws(wid=6),      Club(wid=6),     Palm(wid=12)],
            [     Bow(wid=7),      Bow(wid=12),     Palm(wid=11)],
            [     Bow(wid=7),       Arm(wid=5), Orbitars(wid=11)],
            [    Palm(wid=5),    Cannon(wid=2),      Club(wid=8)],
            [    Palm(wid=7),    Cannon(wid=5),      Arm(wid=12)],
            [    Club(wid=6),    Cannon(wid=6),    Staff(wid=11)],
            [ Cannon(wid=12), Orbitars(wid=12),    Claws(wid=11)],
            [Orbitars(wid=3),       Arm(wid=4),    Cannon(wid=7)]
        ]
        for entry in exception_table:
            if (
                entry[0] == self and entry[1] == other or
                entry[1] == self and entry[0] == other
            ):
                ret = entry[2]
                break
        if ret:
            return ret, self._retrieve_fusion_group(other)
        return ret

    def fusion(self, other):
        id_sum = self.id + other.id
        rid = id_sum if id_sum <= 12 else id_sum - 12
        group = self._retrieve_fusion_group(other)

        # Check for exceptions in exception table. This is necessary
        # because not all fusion follow the rules we understand
        ret = self._assign_from_exception_table(other)
        if ret: return ret

        # Check for exception case
        ret = self._assign_from_table(other, rid)
        return ret, group


class Blade(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 0
        offset = self.cid * 12 # Used to calculate weapon id in class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Staff(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 1
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Claws(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 2
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)

class Bow(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 3
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Palm(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 4
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Club(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 5
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Cannon(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 6
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Orbitars(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 7
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)


class Arm(Weapon):
    def __init__(self, name=None, wid=None):
        super().__init__(name)
        self.cid = 8
        offset = self.cid * 12 # Used to calculate weapon id within class
        self._init_weapon_by_offset(name, self.cid, wid, offset)

