"""
Author: Feanor
Weapons objects containing relevant methods.
"""

class Blade:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "blade"

    def _map_exceptions(self, wep):
        if self.name == "samurai" and wep.name == "earthmaul":
            return "orbitars"
        else:
            return None
    
    def map_fusion(self, wep):
        # If fusion
        res = self._map_exceptions(wep)
        if res is not None:
            return res

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


class Staff:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "staff"

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
        

class Claws:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "claws"

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


class Bow:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "bow"

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


class Palm:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "palm"

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


class Club:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "club"

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


class Cannon:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "cannon"

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


class Orbitars:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "orbitars"

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


class Arm:
    def __init__(self, name):
        self.name = "".join(name.lower().split()[:-1])
        self.type = "arm"

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
