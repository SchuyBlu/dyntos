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
import unittest
from lib.weapons import *

class TestWeapons(unittest.TestCase):
    def setUp(self):
        self.blade = Blade("First blade")
        self.staff = Staff("Dark PIT Staff")
        self.claws = Claws("Wolf Claws")
        self.bow = Bow("PALUTEna Bow")
        self.palm = Palm("Great Reaper palm")
        self.club = Club("Skyscraper Club")
        self.cannon = Cannon("Rail Cannon")
        self.orbitars = Orbitars("Standard Orbitars")
        self.arm = Arm("Volcano Arm")

    def test_givenBladeInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.blade.fusion(Blade("SAMURAI BLADE")), Claws("Artillery claws"))
        self.assertEqual(self.blade.fusion(Staff("Dark Pit Staff")), Claws("Pandora claws"))
        self.assertEqual(self.blade.fusion(Claws("tIGer cLAws")), Club("Babel club"))
        self.assertEqual(self.blade.fusion(Bow("silVER bOW")), Palm("needle palm"))
        self.assertEqual(self.blade.fusion(Palm("burning palM")), Arm("electroshock arm"))
        self.assertEqual(self.blade.fusion(Club("Ogre club")), Staff("flintlock staff"))
        self.assertEqual(self.blade.fusion(Cannon("Doom Cannon")), Staff("Scorpio staff"))
        self.assertEqual(self.blade.fusion(Orbitars("fairy ORBItars")), Palm("cutter palm"))
        self.assertEqual(self.blade.fusion(Arm("upperdash arm")), Bow("palutena bow"))

    def test_givenStaffInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.staff.fusion(Blade("first blade")), Claws("pandora claws"))
        self.assertEqual(self.staff.fusion(Staff("dark pit staff")), Cannon("sonic cannon"))
        self.assertEqual(self.staff.fusion(Claws("artillery claws")), Arm("bowl arm"))
        self.assertEqual(self.staff.fusion(Bow("angel bow")), Arm("bomber arm"))
        self.assertEqual(self.staff.fusion(Palm("pudgy palm")), Cannon("rail cannon"))
        self.assertEqual(self.staff.fusion(Club("babel club")), Claws("tiger claws"))
        self.assertEqual(self.staff.fusion(Cannon("fireworks cannon")), Blade("crusader blade"))
        self.assertEqual(self.staff.fusion(Orbitars("guardian orbitars")), Club("ore club"))
        self.assertEqual(self.staff.fusion(Arm("compact arm")), Orbitars("standard orbitars"))

    def test_givenClawsInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.claws.fusion(Blade("burst blade")), Club("atlas club"))
        self.assertEqual(self.claws.fusion(Staff("scorpio staff")), Arm("kraken arm"))
        self.assertEqual(self.claws.fusion(Claws("artillery claws")), Club("aurum club"))
        self.assertEqual(self.claws.fusion(Bow("crystal bow")), Club("black club"))
        self.assertEqual(self.claws.fusion(Palm("cutter palm")), Arm("end-all arm"))
        self.assertEqual(self.claws.fusion(Club("aurum club")), Bow("phosphora bow"))
        self.assertEqual(self.claws.fusion(Cannon("cragalanche cannon")), Bow("silver bow"))
        self.assertEqual(self.claws.fusion(Orbitars("jetstream orbitars")), Staff("scorpio staff"))
        self.assertEqual(self.claws.fusion(Arm("drill arm")), Staff("flintlock staff"))

    def test_givenBowInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.bow.fusion(Blade("palutena blade")), Palm("aurum palm"))
        self.assertEqual(self.bow.fusion(Staff("ancient staff")), Arm("volcano arm"))
        self.assertEqual(self.bow.fusion(Claws("stealth claws")), Club("atlas club"))
        self.assertEqual(self.bow.fusion(Bow("meteor bow")), Cannon("ball cannon"))
        self.assertEqual(self.bow.fusion(Palm("ninja palm")), Club("Halo Club"))
        self.assertEqual(self.bow.fusion(Club("magnus club")), Palm("viridi palm"))
        self.assertEqual(self.bow.fusion(Cannon("predator cannon")), Orbitars("guardian orbitars"))
        self.assertEqual(self.bow.fusion(Orbitars("standard orbitars")), Cannon("cragalanche cannon"))
        self.assertEqual(self.bow.fusion(Arm("kraken arm")), Blade("aurum blade"))

    def test_givenPalmInFusion_thenReturnsCorrectOutput(self):
        self.assertEqual(self.palm.fusion(Blade("first blade")), Arm("crusher arm"))
        self.assertEqual(self.palm.fusion(Staff("somewhat staff")), Cannon("doom cannon"))
        self.assertEqual(self.palm.fusion(Claws("raptor claws")), Arm("bowl arm"))
        self.assertEqual(self.palm.fusion(Bow("silver bow")), Club("babel club"))
        self.assertEqual(self.palm.fusion(Palm("cutter palm")), Arm("bomber arm"))
        self.assertEqual(self.palm.fusion(Club("magnus club")), Blade("gaol blade"))
        self.assertEqual(self.palm.fusion(Cannon("doom cannon")), Blade("bullet blade"))
        self.assertEqual(self.palm.fusion(Orbitars("arlon orbitars")), Bow("phosphora bow"))
        self.assertEqual(self.palm.fusion(Arm("crusher arm")), Orbitars("standard orbitars"))

    def test_givenClubInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.club.fusion(Blade("royal blade")), Staff("somewhat staff"))
        self.assertEqual(self.club.fusion(Staff("flintlock staff")), Claws("beam claws"))
        self.assertEqual(self.club.fusion(Claws("brawler claws")), Bow("angel bow"))
        self.assertEqual(self.club.fusion(Bow("darkness bow")), Palm("ninja palm"))
        self.assertEqual(self.club.fusion(Palm("cutter palm")), Blade("aquarius blade"))
        self.assertEqual(self.club.fusion(Club("earthmaul club")), Orbitars("boom orbitars"))
        self.assertEqual(self.club.fusion(Cannon("leo cannon")), Orbitars("arlon orbitars"))
        self.assertEqual(self.club.fusion(Orbitars("standard orbitars")), Claws("brawler claws"))
        self.assertEqual(self.club.fusion(Arm("upperdash arm")), Blade("first blade"))

    def test_givenCannonInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.cannon.fusion(Blade("first blade")), Staff("flintlock staff"))
        self.assertEqual(self.cannon.fusion(Staff("dark pit staff")), Blade("royal blade"))
        self.assertEqual(self.cannon.fusion(Claws("beam claws")), Bow("divine bow"))
        self.assertEqual(self.cannon.fusion(Bow("angel bow")), Orbitars("standard orbitars"))
        self.assertEqual(self.cannon.fusion(Palm("midnight palm")), Blade("aurum blade"))
        self.assertEqual(self.cannon.fusion(Club("aurum club")), Orbitars("eyetrack orbitars"))
        self.assertEqual(self.cannon.fusion(Cannon("fireworks cannon")), Palm("viridi palm"))
        self.assertEqual(self.cannon.fusion(Orbitars("gemini orbitars")), Claws("bear claws"))
        self.assertEqual(self.cannon.fusion(Arm("kraken arm")), Staff("ancient staff"))

    def test_givenOrbitarsInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.orbitars.fusion(Blade("aurum blade")), Palm("viridi palm"))
        self.assertEqual(self.orbitars.fusion(Staff("scorpio staff")), Club("aurum club"))
        self.assertEqual(self.orbitars.fusion(Claws("hedgehog claws")), Staff("flintlock staff"))
        self.assertEqual(self.orbitars.fusion(Bow("phosphora bow")), Cannon("ez cannon"))
        self.assertEqual(self.orbitars.fusion(Palm("great reaper palm")), Bow("Fortune bow"))
        self.assertEqual(self.orbitars.fusion(Club("babel club")), Claws("bear claws"))
        self.assertEqual(self.orbitars.fusion(Cannon("rail cannon")), Claws("raptor claws"))
        self.assertEqual(self.orbitars.fusion(Orbitars("fairy orbitars")), Cannon("rail cannon"))
        self.assertEqual(self.orbitars.fusion(Arm("crusher arm")), Palm("burning palm"))

    def test_givenArmInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.arm.fusion(Blade("first blade")), Bow("darkness bow"))
        self.assertEqual(self.arm.fusion(Staff("dark pit staff")), Orbitars("shock orbitars"))
        self.assertEqual(self.arm.fusion(Claws("tiger claws")), Staff("ancient staff"))
        self.assertEqual(self.arm.fusion(Bow("angel bow")), Blade("palutena blade"))
        self.assertEqual(self.arm.fusion(Palm("pudgy palm")), Orbitars("centurion orbitars"))
        self.assertEqual(self.arm.fusion(Club("ore club")), Blade("royal blade"))
        self.assertEqual(self.arm.fusion(Cannon("doom cannon")), Staff("thanatos staff"))
        self.assertEqual(self.arm.fusion(Orbitars("boom orbitars")), Palm("great reaper palm"))
        self.assertEqual(self.arm.fusion(Arm("volcano arm")), Bow("hawkeye bow"))

if __name__ == "__main__":
    unittest.main()

