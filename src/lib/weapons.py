"""
Author: Feanor
Weapons objects containing relevant methods.
"""

class Weapon:
    def __init__(self, name):
        self.valid_names = [
            "first",
            "burst",
            "viper",
            "crusader",
            "royal",
            "optical",
            "samurai",
            "bullet",
            "aquarius",
            "aurum",
            "palutena",
            "gaol",
            "insight",
            "orb",
            "rose",
            "knuckle",
            "ancient",
            "lancer",
            "flintlock",
            "somewhat",
            "scorpio",
            "laser",
            "dark pit",
            "thanatos",
            "tiger",
            "wolf",
            "bear",
            "brawler",
            "stealth",
            "hedgehog",
            "raptor",
            "artillery",
            "cancer",
            "beam",
            "viridi",
            "pandora",
            "fortune",
            "silver",
            "meteor",
            "divine",
            "darkness",
            "crystal",
            "angel",
            "hawkeye",
            "sagittarius",
            "palutena",
            "phosphora",
            "violet",
            "burning",
            "needle",
            "midnight",
            "cursed",
            "cutter",
            "pudgy",
            "ninja",
            "virgo",
            "viridi",
            "great reaper",
            "ore",
            "babel",
            "skyscraper",
            "atlas",
            "earthmaul",
            "ogre",
            "halo",
            "black",
            "capricorn",
            "aurum",
            "hewdraw",
            "magnus",
            "ez",
            "ball",
            "predator",
            "poseidon",
            "fireworks",
            "rail",
            "dynamo",
            "doom",
            "leo",
            "sonic",
            "twinbellows",
            "cragalanche",
            "standard",
            "guardian",
            "shock",
            "eyetrack",
            "fairy",
            "paw pad",
            "jetstream",
            "boom",
            "gemini",
            "aurum",
            "centurion",
            "arlon",
            "crusher",
            "compact",
            "electroshock",
            "volcano",
            "drill",
            "bomber",
            "bowl",
            "end-all",
            "taurus",
            "upperdash",
            "kraken",
            "phoenix"
        ]
        self.name = " ".join(name.lower().split()[:-1])
        self.type = name.lower().split()[-1]
        if not self.is_valid():
            raise ValueError("Weapon name must exist")

    def is_valid(self):
        if self.name in self.valid_names:
            return True
        return False


class Blade(Weapon):
    def __init__(self, name):
        super().__init__(name)
    
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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
    def __init__(self, name):
        super().__init__(name)

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
