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
import unittest
from lib.weapons import *

class TestWeaponIDs(unittest.TestCase):
    def setUp(self):
        # I am only concerned with testing first and last of each weapon class.
        # If both work, it is safe to assume all in between work.
        self.first_blade = Blade("First blade")
        self.gaol_blade = Blade("Gaol blade")
        self.insight_staff = Staff("Insight staff")
        self.thanatos_staff = Staff("Thanatos staff")
        self.tiger_claws = Claws("Tiger claws")
        self.pandora_claws = Claws("Pandora claws")
        self.fortune_bow = Bow("Fortune bow")
        self.phosphora_bow = Bow("Phosphora bow")
        self.violet_palm = Palm("Violet palm")
        self.great_reaper_palm = Palm("Great reaper palm")
        self.ore_club = Club("Ore club")
        self.magnus_club = Club("Magnus club")
        self.ez_cannon = Cannon("Ez cannon")
        self.cragalanche_cannon = Cannon("Cragalanche cannon")
        self.standard_orbitars = Orbitars("Standard orbitars")
        self.arlon_orbitars = Orbitars("Arlon orbitars")
        self.crusher_arm = Arm("Crusher arm")
        self.phoenix_arm = Arm("Phoenix arm")

    def test_givenAnyWeapon_thenIdShouldBeCorrect(self):
        self.assertEqual(self.first_blade.id, 1)
        self.assertEqual(self.gaol_blade.id, 12)
        self.assertEqual(self.insight_staff.id, 1)
        self.assertEqual(self.thanatos_staff.id, 12)
        self.assertEqual(self.tiger_claws.id, 1)
        self.assertEqual(self.pandora_claws.id, 12)
        self.assertEqual(self.fortune_bow.id, 1)
        self.assertEqual(self.phosphora_bow.id, 12)
        self.assertEqual(self.violet_palm.id, 1)
        self.assertEqual(self.great_reaper_palm.id, 12)
        self.assertEqual(self.ore_club.id, 1)
        self.assertEqual(self.magnus_club.id, 12)
        self.assertEqual(self.ez_cannon.id, 1)
        self.assertEqual(self.cragalanche_cannon.id, 12)
        self.assertEqual(self.standard_orbitars.id, 1)
        self.assertEqual(self.arlon_orbitars.id, 12)
        self.assertEqual(self.crusher_arm.id, 1)
        self.assertEqual(self.phoenix_arm.id, 12)

    def test_whenIdEnteredAsParameter_shouldCreateCorrectWeapon(self):
        self.assertEqual(str(Blade(wid=1)), "first blade")
        self.assertEqual(str(Blade(wid=2)), "burst blade")
        self.assertEqual(str(Blade(wid=3)), "viper blade")
        self.assertEqual(str(Blade(wid=4)), "crusader blade")
        self.assertEqual(str(Blade(wid=5)), "royal blade")
        self.assertEqual(str(Blade(wid=6)), "optical blade")
        self.assertEqual(str(Blade(wid=7)), "samurai blade")
        self.assertEqual(str(Blade(wid=8)), "bullet blade")
        self.assertEqual(str(Blade(wid=9)), "aquarius blade")
        self.assertEqual(str(Blade(wid=10)), "aurum blade")
        self.assertEqual(str(Blade(wid=11)), "palutena blade")
        self.assertEqual(str(Blade(wid=12)), "gaol blade")

        self.assertEqual(str(Staff(wid=1)), "insight staff")
        self.assertEqual(str(Staff(wid=2)), "orb staff")
        self.assertEqual(str(Staff(wid=3)), "rose staff")
        self.assertEqual(str(Staff(wid=4)), "knuckle staff")
        self.assertEqual(str(Staff(wid=5)), "ancient staff")
        self.assertEqual(str(Staff(wid=6)), "lancer staff")
        self.assertEqual(str(Staff(wid=7)), "flintlock staff")
        self.assertEqual(str(Staff(wid=8)), "somewhat staff")
        self.assertEqual(str(Staff(wid=9)), "scorpio staff")
        self.assertEqual(str(Staff(wid=10)), "laser staff")
        self.assertEqual(str(Staff(wid=11)), "dark pit staff")
        self.assertEqual(str(Staff(wid=12)), "thanatos staff")

        self.assertEqual(str(Claws(wid=1)), "tiger claws")
        self.assertEqual(str(Claws(wid=2)), "wolf claws")
        self.assertEqual(str(Claws(wid=3)), "bear claws")
        self.assertEqual(str(Claws(wid=4)), "brawler claws")
        self.assertEqual(str(Claws(wid=5)), "stealth claws")
        self.assertEqual(str(Claws(wid=6)), "hedgehog claws")
        self.assertEqual(str(Claws(wid=7)), "raptor claws")
        self.assertEqual(str(Claws(wid=8)), "artillery claws")
        self.assertEqual(str(Claws(wid=9)), "cancer claws")
        self.assertEqual(str(Claws(wid=10)), "beam claws")
        self.assertEqual(str(Claws(wid=11)), "viridi claws")
        self.assertEqual(str(Claws(wid=12)), "pandora claws")

        self.assertEqual(str(Bow(wid=1)), "fortune bow")
        self.assertEqual(str(Bow(wid=2)), "silver bow")
        self.assertEqual(str(Bow(wid=3)), "meteor bow")
        self.assertEqual(str(Bow(wid=4)), "divine bow")
        self.assertEqual(str(Bow(wid=5)), "darkness bow")
        self.assertEqual(str(Bow(wid=6)), "crystal bow")
        self.assertEqual(str(Bow(wid=7)), "angel bow")
        self.assertEqual(str(Bow(wid=8)), "hawkeye bow")
        self.assertEqual(str(Bow(wid=9)), "sagittarius bow")
        self.assertEqual(str(Bow(wid=10)), "aurum bow")
        self.assertEqual(str(Bow(wid=11)), "palutena bow")
        self.assertEqual(str(Bow(wid=12)), "phosphora bow")

        self.assertEqual(str(Palm(wid=1)), "violet palm")
        self.assertEqual(str(Palm(wid=2)), "burning palm")
        self.assertEqual(str(Palm(wid=3)), "needle palm")
        self.assertEqual(str(Palm(wid=4)), "midnight palm")
        self.assertEqual(str(Palm(wid=5)), "cursed palm")
        self.assertEqual(str(Palm(wid=6)), "cutter palm")
        self.assertEqual(str(Palm(wid=7)), "pudgy palm")
        self.assertEqual(str(Palm(wid=8)), "ninja palm")
        self.assertEqual(str(Palm(wid=9)), "virgo palm")
        self.assertEqual(str(Palm(wid=10)), "aurum palm")
        self.assertEqual(str(Palm(wid=11)), "viridi palm")
        self.assertEqual(str(Palm(wid=12)), "great reaper palm")

        self.assertEqual(str(Club(wid=1)), "ore club")
        self.assertEqual(str(Club(wid=2)), "babel club")
        self.assertEqual(str(Club(wid=3)), "skyscraper club")
        self.assertEqual(str(Club(wid=4)), "atlas club")
        self.assertEqual(str(Club(wid=5)), "earthmaul club")
        self.assertEqual(str(Club(wid=6)), "ogre club")
        self.assertEqual(str(Club(wid=7)), "halo club")
        self.assertEqual(str(Club(wid=8)), "black club")
        self.assertEqual(str(Club(wid=9)), "capricorn club")
        self.assertEqual(str(Club(wid=10)), "aurum club")
        self.assertEqual(str(Club(wid=11)), "hewdraw club")
        self.assertEqual(str(Club(wid=12)), "magnus club")

        self.assertEqual(str(Cannon(wid=1)), "ez cannon")
        self.assertEqual(str(Cannon(wid=2)), "ball cannon")
        self.assertEqual(str(Cannon(wid=3)), "predator cannon")
        self.assertEqual(str(Cannon(wid=4)), "poseidon cannon")
        self.assertEqual(str(Cannon(wid=5)), "fireworks cannon")
        self.assertEqual(str(Cannon(wid=6)), "rail cannon")
        self.assertEqual(str(Cannon(wid=7)), "dynamo cannon")
        self.assertEqual(str(Cannon(wid=8)), "doom cannon")
        self.assertEqual(str(Cannon(wid=9)), "leo cannon")
        self.assertEqual(str(Cannon(wid=10)), "sonic cannon")
        self.assertEqual(str(Cannon(wid=11)), "twinbellows cannon")
        self.assertEqual(str(Cannon(wid=12)), "cragalanche cannon")

        self.assertEqual(str(Orbitars(wid=1)), "standard orbitars")
        self.assertEqual(str(Orbitars(wid=2)), "guardian orbitars")
        self.assertEqual(str(Orbitars(wid=3)), "shock orbitars")
        self.assertEqual(str(Orbitars(wid=4)), "eyetrack orbitars")
        self.assertEqual(str(Orbitars(wid=5)), "fairy orbitars")
        self.assertEqual(str(Orbitars(wid=6)), "paw pad orbitars")
        self.assertEqual(str(Orbitars(wid=7)), "jetstream orbitars")
        self.assertEqual(str(Orbitars(wid=8)), "boom orbitars")
        self.assertEqual(str(Orbitars(wid=9)), "gemini orbitars")
        self.assertEqual(str(Orbitars(wid=10)), "aurum orbitars")
        self.assertEqual(str(Orbitars(wid=11)), "centurion orbitars")
        self.assertEqual(str(Orbitars(wid=12)), "arlon orbitars")

        self.assertEqual(str(Arm(wid=1)), "crusher arm")
        self.assertEqual(str(Arm(wid=2)), "compact arm")
        self.assertEqual(str(Arm(wid=3)), "electroshock arm")
        self.assertEqual(str(Arm(wid=4)), "volcano arm")
        self.assertEqual(str(Arm(wid=5)), "drill arm")
        self.assertEqual(str(Arm(wid=6)), "bomber arm")
        self.assertEqual(str(Arm(wid=7)), "bowl arm")
        self.assertEqual(str(Arm(wid=8)), "end-all arm")
        self.assertEqual(str(Arm(wid=9)), "taurus arm")
        self.assertEqual(str(Arm(wid=10)), "upperdash arm")
        self.assertEqual(str(Arm(wid=11)), "kraken arm")
        self.assertEqual(str(Arm(wid=12)), "phoenix arm")


if __name__ == "__main__":
    unittest.main()

