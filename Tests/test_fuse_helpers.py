import unittest
from lib.weapons import *
import lib.fuse_results as fr


class TestFuseResults(unittest.TestCase):
    def setUp(self):
        self.misc_weapon = Weapon()
        self.weapon_list_2d = [
            [
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
                "gaol blade"
            ],
            [
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
                "thanatos staff"
            ],
            [
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
                "pandora claws"
            ],
            [
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
                "phosphora bow"
            ],
            [
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
                "great reaper palm"
            ],
            [
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
                "magnus club"
            ],
            [
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
                "cragalanche cannon"
            ],
            [
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
                "arlon orbitars"
            ],
            [
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
            ],
        ]

    def test_givenWeaponList_thenSplitsInto2dList(self):
        new_2d_list = fr.slice_wep_list(self.misc_weapon.WEAPONS)
        self.assertEqual(new_2d_list, self.weapon_list_2d)

    def test_givenInputAndDesired_thenOutputsCorrectResList(self):
        # Case 1: Inputting First Blade, wanting Tiger Claws
        res = []
        correct_res = [
            [Blade(wid=1), Blade(wid=12), Claws(wid=1), 4],
            [Blade(wid=1), Staff(wid=12), Claws(wid=1), 1]
        ]
        fr.fuse_from_comb(Blade(wid=1), Claws(wid=1), res)
        self.assertEqual(res, correct_res)

        # Case 2: Inputting Insight Staff, wanting Earthmaul Club
        res = []
        correct_res = [
            [Staff(wid=1), Orbitars(wid=4), Club(wid=5), 2]
        ]
        fr.fuse_from_comb(Staff(wid=1), Club(wid=5), res)
        self.assertEqual(res, correct_res)

        # Case 3: Inputting Doom Cannon, wanting Flintlock Staff
        res = []
        correct_res = [
            [Cannon(wid=8), Blade(wid=11), Staff(wid=7), 5],
            [Cannon(wid=8), Arm(wid=11), Staff(wid=7), 3]
        ]
        fr.fuse_from_comb(Cannon(wid=8), Staff(wid=7), res)
        self.assertEqual(res, correct_res)

        # NOTE: Should add more test cases, but am unsure what outliers
        # there may be.

    def test_givenInputAndDesiredGroup_thenOutputsCorrectResList(self):
        # Case 1: Inputting First Blade, wanting Group 1
        res = []
        correct_res = [
            [Blade(wid=1), Blade(wid=4), Claws(wid=5), 1],
            [Blade(wid=1), Blade(wid=9), Claws(wid=10), 1],
            [Blade(wid=1), Staff(wid=2), Claws(wid=3), 1],
            [Blade(wid=1), Staff(wid=7), Claws(wid=8), 1],
            [Blade(wid=1), Staff(wid=12), Claws(wid=1), 1],
            [Blade(wid=1), Claws(wid=5), Club(wid=6), 1],
            [Blade(wid=1), Claws(wid=10), Club(wid=11), 1],
            [Blade(wid=1), Bow(wid=3), Palm(wid=4), 1],
            [Blade(wid=1), Bow(wid=8), Palm(wid=9), 1],
            [Blade(wid=1), Palm(wid=1), Arm(wid=2), 1],
            [Blade(wid=1), Palm(wid=6), Arm(wid=7), 1],
            [Blade(wid=1), Palm(wid=11), Arm(wid=12), 1],
            [Blade(wid=1), Club(wid=4), Staff(wid=5), 1],
            [Blade(wid=1), Club(wid=9), Staff(wid=10), 1],
            [Blade(wid=1), Cannon(wid=2), Staff(wid=3), 1],
            [Blade(wid=1), Cannon(wid=7), Staff(wid=8), 1],
            [Blade(wid=1), Cannon(wid=12), Staff(wid=1), 1],
            [Blade(wid=1), Orbitars(wid=5), Palm(wid=6), 1],
            [Blade(wid=1), Orbitars(wid=10), Palm(wid=11), 1],
            [Blade(wid=1), Arm(wid=3), Bow(wid=4), 1],
            [Blade(wid=1), Arm(wid=8), Bow(wid=9), 1]
        ]
        fr.fuse_from_comb(Blade(wid=1), 1, res)
        self.assertEqual(res, correct_res)

        # Case 2: Input weapon is Crystal Bow, want Group 5
        res = []
        correct_res = [
            [Bow(wid=6), Blade(wid=3), Palm(wid=9), 5],
            [Bow(wid=6), Blade(wid=8), Palm(wid=2), 5],
            [Bow(wid=6), Staff(wid=1), Arm(wid=7), 5],
            [Bow(wid=6), Staff(wid=6), Arm(wid=12), 5],
            [Bow(wid=6), Staff(wid=11), Arm(wid=5), 5],
            [Bow(wid=6), Claws(wid=4), Club(wid=10), 5],
            [Bow(wid=6), Claws(wid=9), Club(wid=3), 5],
            [Bow(wid=6), Bow(wid=2), Cannon(wid=8), 5],
            [Bow(wid=6), Bow(wid=10), Cannon(wid=4), 5],
            [Bow(wid=6), Palm(wid=3), Club(wid=9), 5],
            [Bow(wid=6), Palm(wid=8), Club(wid=2), 5],
            [Bow(wid=6), Club(wid=1), Palm(wid=7), 5],
            [Bow(wid=6), Club(wid=6), Palm(wid=12), 5],
            [Bow(wid=6), Club(wid=11), Palm(wid=5), 5],
            [Bow(wid=6), Cannon(wid=4), Orbitars(wid=10), 5],
            [Bow(wid=6), Cannon(wid=9), Orbitars(wid=3), 5],
            [Bow(wid=6), Orbitars(wid=2), Cannon(wid=8), 5],
            [Bow(wid=6), Orbitars(wid=7), Cannon(wid=1), 5],
            [Bow(wid=6), Orbitars(wid=12), Cannon(wid=6), 5],
            [Bow(wid=6), Arm(wid=5), Blade(wid=11), 5],
            [Bow(wid=6), Arm(wid=10), Blade(wid=4), 5]
        ]
        fr.fuse_from_comb(Bow(wid=6), 5, res)
        self.assertEqual(res, correct_res)
        # NOTE: Should run more tests, but I don't want to write
        # any more out by hand. Seeing as these two cases work, I'm
        # going to assume that any weapon + group input works.

    def test_givenSingularDesiredWeapon_ConstructsListOfCorrectWeapons(self):
        # NOTE: Writing out an automatic test for this is far too difficult
        # and time consuming, as I'd need to check each combination in game
        # and calculate the fusion group. Instead, following the assuming that
        # the previous tests have passed, we will assume this test works, and
        # print out the resulting lists in log files found in
        # "Tests/logs/single_input_fusions.log.
        file = open("Tests/logs/single_input_fusions.log", "w")
        res = fr.fuse_by_result(Blade(wid=3))
        for fusion in res:
            file.write(f"{str(fusion[0])} + {str(fusion[1])} = {str(fusion[2])} in Group {fusion[3]}\n")
        file.close()

    def test_givenDesiredWeaponAndGroup_thenConstructsListOfCorrectWeapons(self):
        # Want Viper Blade in fusion group 3
        res = []
        correct_res = [
            [Staff(wid=4), Cannon(wid=11), Blade(wid=3), 3],
            [Staff(wid=9), Cannon(wid=6), Blade(wid=3), 3],
            [Bow(wid=4), Arm(wid=11), Blade(wid=3), 3],
            [Bow(wid=9), Arm(wid=6), Blade(wid=3), 3],
            [Palm(wid=5), Club(wid=10), Blade(wid=3), 3],
            [Palm(wid=6), Cannon(wid=9), Blade(wid=3), 3],
            [Palm(wid=10), Club(wid=5), Blade(wid=3), 3],
            [Palm(wid=11), Cannon(wid=4), Blade(wid=3), 3],
            [Club(wid=1), Arm(wid=2), Blade(wid=3), 3],
            [Club(wid=7), Arm(wid=8), Blade(wid=3), 3],
            [Club(wid=12), Arm(wid=3), Blade(wid=3), 3]
        ]
        res = fr.fuse_by_result(Blade(wid=3), group=3)
        self.assertEqual(res, correct_res)

    def test_givenDesiredGroupOnly_thenConstructsListOfCorrectWeapons(self):
        # NOTE: Writing out an automatic test for this is far too difficult
        # and time consuming, as I'd need to check each combination in game
        # and calculate the fusion group. Instead, following the assuming that
        # the previous tests have passed, we will assume this test works, and
        # print out the resulting lists in log files found in
        # "Tests/logs/single_input_fusions.log.
        file = open("Tests/logs/group_fusions.log", "w")
        res = fr.fuse_by_result(1)
        for fusion in res:
            file.write(f"{str(fusion[0])} + {str(fusion[1])} = {str(fusion[2])} in Group {fusion[3]}\n")
        file.close()


if __name__ == "__main__":
    unittest.main()

