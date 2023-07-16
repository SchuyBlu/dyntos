"""
Author: Feanor
Weapons objects containing relevant methods.
"""

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

    def _valid(self, name):
        if name.lower() in self.WEAPONS:
            return True
        return False


class Blade(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 0
        offset = self.CLASS_ID * 12 # Used to calculate weapon id in class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "claws"
            case "staff":
                res = "claws"
            case "claws":
                res = "club"
            case "bow":
                res = "palm"
            case "palm":
                res = "arm"
            case "club":
                res = "staff"
            case "cannon":
                res = "staff"
            case "orbitars":
                res = "palm"
            case "arm":
                res = "bow"
            case other:
                res = None
        return res


class Staff(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 1
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "claws"
            case "staff":
                res = "cannon"
            case "claws":
                res = "arm"
            case "bow":
                res = "arm"
            case "palm":
                res = "cannon"
            case "club":
                res = "claws"
            case "cannon":
                res = "blade"
            case "orbitars":
                res = "club"
            case "arm":
                res = "orbitars"
            case other:
                res = None
        return res


class Claws(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 2
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "club"
            case "staff":
                res = "arm"
            case "claws":
                res = "club"
            case "bow":
                res = "club"
            case "palm":
                res = "arm"
            case "club":
                res = "bow"
            case "cannon":
                res = "bow"
            case "orbitars":
                res = "staff"
            case "arm":
                res = "staff"
            case other:
                res = None
        return res


class Bow(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 3
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "palm"
            case "staff":
                res = "arm"
            case "claws":
                res = "club"
            case "bow":
                res = "cannon"
            case "palm":
                res = "club"
            case "club":
                res = "palm"
            case "cannon":
                res = "orbitars"
            case "orbitars":
                res = "cannon"
            case "arm":
                res = "blade"
            case other:
                res = None
        return res


class Palm(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 4
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "arm"
            case "staff":
                res = "cannon"
            case "claws":
                res = "arm"
            case "bow":
                res = "club"
            case "palm":
                res = "arm"
            case "club":
                res = "blade"
            case "cannon":
                res = "blade"
            case "orbitars":
                res = "bow"
            case "arm":
                res = "orbitars"
            case other:
                res = None
        return res


class Club(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 5
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "staff"
            case "staff":
                res = "claws"
            case "claws":
                res = "bow"
            case "bow":
                res = "palm"
            case "palm":
                res = "blade"
            case "club":
                res = "orbitars"
            case "cannon":
                res = "orbitars"
            case "orbitars":
                res = "claws"
            case "arm":
                res = "blade"
            case other:
                res = None
        return res


class Cannon(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 6
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "staff"
            case "staff":
                res = "blade"
            case "claws":
                res = "bow"
            case "bow":
                res = "orbitars"
            case "palm":
                res = "blade"
            case "club":
                res = "orbitars"
            case "cannon":
                res = "palm"
            case "orbitars":
                res = "claws"
            case "arm":
                res = "staff"
            case other:
                res = None
        return res


class Orbitars(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 7
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "palm"
            case "staff":
                res = "club"
            case "claws":
                res = "staff"
            case "bow":
                res = "cannon"
            case "palm":
                res = "bow"
            case "club":
                res = "claws"
            case "cannon":
                res = "claws"
            case "orbitars":
                res = "cannon"
            case "arm":
                res = "palm"
            case other:
                res = None
        return res


class Arm(Weapon):
    def __init__(self, name=None, wep_id=None):
        super().__init__(name)
        self.CLASS_ID = 8
        offset = self.CLASS_ID * 12 # Used to calculate weapon id within class

        if wep_id and not name:
            self.name = " ".join(self.WEAPONS[offset + wep_id - 1].split()[:-1])
            self.type = self.WEAPONS[offset + wep_id - 1].split()[-1]
        else:
            self.id = self.WEAPONS.index(f"{self.name} {self.type}") - offset + 1

    def __str__(self):
        return f"{self.name} {self.type}"

    def map_fusion(self, wep):
        match wep.type:
            case "blade":
                res = "bow"
            case "staff":
                res = "orbitars"
            case "claws":
                res = "staff"
            case "bow":
                res = "blade"
            case "palm":
                res = "orbitars"
            case "club":
                res = "blade"
            case "cannon":
                res = "staff"
            case "orbitars":
                res = "palm"
            case "arm":
                res = "bow"
            case other:
                res = None
        return res
