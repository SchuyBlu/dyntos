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
        self.assertEqual(self.blade.fusion(Blade("SAMURAI BLADE")), (Claws("Artillery claws"), 4))
        self.assertEqual(self.blade.fusion(Staff("Dark Pit Staff")), (Claws("Pandora claws"), 3))
        self.assertEqual(self.blade.fusion(Claws("tIGer cLAws")), (Club("Babel club"), 5))
        self.assertEqual(self.blade.fusion(Bow("silVER bOW")), (Palm("needle palm"), 3))
        self.assertEqual(self.blade.fusion(Palm("burning palM")), (Arm("electroshock arm"), 5))
        self.assertEqual(self.blade.fusion(Club("Ogre club")), (Staff("flintlock staff"), 2))
        self.assertEqual(self.blade.fusion(Cannon("Doom Cannon")), (Staff("Scorpio staff"), 5))
        self.assertEqual(self.blade.fusion(Orbitars("fairy ORBItars")), (Palm("cutter palm"), 1))
        self.assertEqual(self.blade.fusion(Arm("upperdash arm")), (Bow("palutena bow"), 2))

    def test_givenStaffInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.staff.fusion(Blade("first blade")), (Claws("pandora claws"), 3))
        self.assertEqual(self.staff.fusion(Staff("dark pit staff")), (Cannon("sonic cannon"), 2))
        self.assertEqual(self.staff.fusion(Claws("artillery claws")), (Arm("bowl arm"), 5))
        self.assertEqual(self.staff.fusion(Bow("angel bow")), (Arm("bomber arm"), 2))
        self.assertEqual(self.staff.fusion(Palm("pudgy palm")), (Cannon("rail cannon"), 3))
        self.assertEqual(self.staff.fusion(Club("babel club")), (Claws("tiger claws"), 5))
        self.assertEqual(self.staff.fusion(Cannon("fireworks cannon")), (Blade("crusader blade"), 5))
        self.assertEqual(self.staff.fusion(Orbitars("guardian orbitars")), (Club("ore club"), 1))
        self.assertEqual(self.staff.fusion(Arm("compact arm")), (Orbitars("standard orbitars"), 2))

    def test_givenClawsInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.claws.fusion(Blade("burst blade")), (Club("atlas club"), 5))
        self.assertEqual(self.claws.fusion(Staff("scorpio staff")), (Arm("kraken arm"), 2))
        self.assertEqual(self.claws.fusion(Claws("artillery claws")), (Club("aurum club"), 4))
        self.assertEqual(self.claws.fusion(Bow("crystal bow")), (Club("black club"), 4))
        self.assertEqual(self.claws.fusion(Palm("cutter palm")), (Arm("end-all arm"), 1))
        self.assertEqual(self.claws.fusion(Club("aurum club")), (Bow("phosphora bow"), 5))
        self.assertEqual(self.claws.fusion(Cannon("cragalanche cannon")), (Bow("silver bow"), 1))
        self.assertEqual(self.claws.fusion(Orbitars("jetstream orbitars")), (Staff("scorpio staff"), 2))
        self.assertEqual(self.claws.fusion(Arm("drill arm")), (Staff("flintlock staff"), 2))

    def test_givenBowInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.bow.fusion(Blade("palutena blade")), (Palm("aurum palm"), 4))
        self.assertEqual(self.bow.fusion(Staff("ancient staff")), (Arm("volcano arm"), 2))
        self.assertEqual(self.bow.fusion(Claws("stealth claws")), (Club("atlas club"), 1))
        self.assertEqual(self.bow.fusion(Bow("meteor bow")), (Cannon("ball cannon"), 1))
        self.assertEqual(self.bow.fusion(Palm("ninja palm")), (Club("Halo Club"), 5))
        self.assertEqual(self.bow.fusion(Club("magnus club")), (Palm("viridi palm"), 2))
        self.assertEqual(self.bow.fusion(Cannon("predator cannon")), (Orbitars("guardian orbitars"), 1))
        self.assertEqual(self.bow.fusion(Orbitars("standard orbitars")), (Cannon("cragalanche cannon"), 1))
        self.assertEqual(self.bow.fusion(Arm("kraken arm")), (Blade("aurum blade"), 2))

    def test_givenPalmInFusion_thenReturnsCorrectOutput(self):
        self.assertEqual(self.palm.fusion(Blade("first blade")), (Arm("crusher arm"), 5))
        self.assertEqual(self.palm.fusion(Staff("somewhat staff")), (Cannon("doom cannon"), 2))
        self.assertEqual(self.palm.fusion(Claws("raptor claws")), (Arm("bowl arm"), 5))
        self.assertEqual(self.palm.fusion(Bow("silver bow")), (Club("babel club"), 3))
        self.assertEqual(self.palm.fusion(Palm("cutter palm")), (Arm("bomber arm"), 4))
        self.assertEqual(self.palm.fusion(Club("magnus club")), (Blade("gaol blade"), 3))
        self.assertEqual(self.palm.fusion(Cannon("doom cannon")), (Blade("bullet blade"), 2))
        self.assertEqual(self.palm.fusion(Orbitars("arlon orbitars")), (Bow("phosphora bow"), 4))
        self.assertEqual(self.palm.fusion(Arm("crusher arm")), (Orbitars("standard orbitars"), 3))

    def test_givenClubInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.club.fusion(Blade("royal blade")), (Staff("somewhat staff"), 1))
        self.assertEqual(self.club.fusion(Staff("flintlock staff")), (Claws("beam claws"), 5))
        self.assertEqual(self.club.fusion(Claws("brawler claws")), (Bow("angel bow"), 2))
        self.assertEqual(self.club.fusion(Bow("darkness bow")), (Palm("ninja palm"), 3))
        self.assertEqual(self.club.fusion(Palm("cutter palm")), (Blade("aquarius blade"), 5))
        self.assertEqual(self.club.fusion(Club("earthmaul club")), (Orbitars("boom orbitars"), 3))
        self.assertEqual(self.club.fusion(Cannon("leo cannon")), (Orbitars("arlon orbitars"), 1))
        self.assertEqual(self.club.fusion(Orbitars("standard orbitars")), (Claws("brawler claws"), 3))
        self.assertEqual(self.club.fusion(Arm("upperdash arm")), (Blade("first blade"), 1))

    def test_givenCannonInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.cannon.fusion(Blade("first blade")), (Staff("flintlock staff"), 3))
        self.assertEqual(self.cannon.fusion(Staff("dark pit staff")), (Blade("royal blade"), 2))
        self.assertEqual(self.cannon.fusion(Claws("beam claws")), (Bow("divine bow"), 5))
        self.assertEqual(self.cannon.fusion(Bow("angel bow")), (Orbitars("standard orbitars"), 2))
        self.assertEqual(self.cannon.fusion(Palm("midnight palm")), (Blade("aurum blade"), 4))
        self.assertEqual(self.cannon.fusion(Club("aurum club")), (Orbitars("eyetrack orbitars"), 1))
        self.assertEqual(self.cannon.fusion(Cannon("fireworks cannon")), (Palm("viridi palm"), 4))
        self.assertEqual(self.cannon.fusion(Orbitars("gemini orbitars")), (Claws("bear claws"), 2))
        self.assertEqual(self.cannon.fusion(Arm("kraken arm")), (Staff("ancient staff"), 5))

    def test_givenOrbitarsInFusion_thenReturnsCorrectOutputWeapon(self):
        self.assertEqual(self.orbitars.fusion(Blade("aurum blade")), (Palm("viridi palm"), 2))
        self.assertEqual(self.orbitars.fusion(Staff("scorpio staff")), (Club("aurum club"), 5))
        self.assertEqual(self.orbitars.fusion(Claws("hedgehog claws")), (Staff("flintlock staff"), 2))
        self.assertEqual(self.orbitars.fusion(Bow("phosphora bow")), (Cannon("ez cannon"), 3))
        self.assertEqual(self.orbitars.fusion(Palm("great reaper palm")), (Bow("Fortune bow"), 2))
        self.assertEqual(self.orbitars.fusion(Club("babel club")), (Claws("bear claws"), 1))
        self.assertEqual(self.orbitars.fusion(Cannon("rail cannon")), (Claws("raptor claws"), 3))
        self.assertEqual(self.orbitars.fusion(Orbitars("fairy orbitars")), (Cannon("rail cannon"), 5))
        self.assertEqual(self.orbitars.fusion(Arm("crusher arm")), (Palm("burning palm"), 3))

    def test_givenArmInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.arm.fusion(Blade("first blade")), (Bow("darkness bow"), 5))
        self.assertEqual(self.arm.fusion(Staff("dark pit staff")), (Orbitars("shock orbitars"), 3))
        self.assertEqual(self.arm.fusion(Claws("tiger claws")), (Staff("ancient staff"), 2))
        self.assertEqual(self.arm.fusion(Bow("angel bow")), (Blade("palutena blade"), 3))
        self.assertEqual(self.arm.fusion(Palm("pudgy palm")), (Orbitars("centurion orbitars"), 2))
        self.assertEqual(self.arm.fusion(Club("ore club")), (Blade("royal blade"), 5))
        self.assertEqual(self.arm.fusion(Cannon("doom cannon")), (Staff("thanatos staff"), 2))
        self.assertEqual(self.arm.fusion(Orbitars("boom orbitars")), (Palm("great reaper palm"), 1))
        self.assertEqual(self.arm.fusion(Arm("volcano arm")), (Bow("hawkeye bow"), 2))

if __name__ == "__main__":
    unittest.main()

