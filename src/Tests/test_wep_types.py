"""
Author: Feanor
Testing weapon type conversions. Test for every fusion possible.
"""
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

    def test_givenBladeInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.blade.map_fusion(Blade("SAMURAI BLADE")), "claws")
        self.assertEqual(self.blade.map_fusion(Staff("Dark Pit Staff")), "claws")
        self.assertEqual(self.blade.map_fusion(Claws("tIGer cLAws")), "club")
        self.assertEqual(self.blade.map_fusion(Bow("silVER bOW")), "palm")
        self.assertEqual(self.blade.map_fusion(Palm("burning palM")), "arm")
        self.assertEqual(self.blade.map_fusion(Club("Ogre club")), "staff")
        self.assertEqual(self.blade.map_fusion(Cannon("Doom Cannon")), "staff")
        self.assertEqual(self.blade.map_fusion(Orbitars("fairy ORBItars")), "palm")
        self.assertEqual(self.blade.map_fusion(Arm("upperdash arm")), "bow")

    def test_givenStaffInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.staff.map_fusion(Blade("first blade")), "claws")
        self.assertEqual(self.staff.map_fusion(Staff("dark pit staff")), "cannon")
        self.assertEqual(self.staff.map_fusion(Claws("artillery claws")), "arm")
        self.assertEqual(self.staff.map_fusion(Bow("angel bow")), "arm")
        self.assertEqual(self.staff.map_fusion(Palm("pudgy palm")), "cannon")
        self.assertEqual(self.staff.map_fusion(Club("babel club")), "claws")
        self.assertEqual(self.staff.map_fusion(Cannon("fireworks cannon")), "blade")
        self.assertEqual(self.staff.map_fusion(Orbitars("guardian orbitars")), "club")
        self.assertEqual(self.staff.map_fusion(Arm("compact arm")), "orbitars")

    def test_givenClawsInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.claws.map_fusion(Blade("burst blade")), "club")
        self.assertEqual(self.claws.map_fusion(Staff("thanatos staff")), "arm")
        self.assertEqual(self.claws.map_fusion(Claws("bear claws")), "club")
        self.assertEqual(self.claws.map_fusion(Bow("sagittarius bow")), "club")
        self.assertEqual(self.claws.map_fusion(Palm("burning palm")), "arm")
        self.assertEqual(self.claws.map_fusion(Club("capricorn club")), "bow")
        self.assertEqual(self.claws.map_fusion(Cannon("rail cannon")), "bow")
        self.assertEqual(self.claws.map_fusion(Orbitars("eyetrack orbitars")), "staff")
        self.assertEqual(self.claws.map_fusion(Arm("bowl arm")), "staff")

    def test_givenBowInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.bow.map_fusion(Blade("palutena blade")), "palm")
        self.assertEqual(self.bow.map_fusion(Staff("ancient staff")), "arm")
        self.assertEqual(self.bow.map_fusion(Claws("stealth claws")), "club")
        self.assertEqual(self.bow.map_fusion(Bow("meteor bow")), "cannon")
        self.assertEqual(self.bow.map_fusion(Palm("ninja palm")), "club")
        self.assertEqual(self.bow.map_fusion(Club("magnus club")), "palm")
        self.assertEqual(self.bow.map_fusion(Cannon("predator cannon")), "orbitars")
        self.assertEqual(self.bow.map_fusion(Orbitars("standard orbitars")), "cannon")
        self.assertEqual(self.bow.map_fusion(Arm("kraken arm")), "blade")

    def test_givenPalmInFusion_thenReturnsCorrectOutputType(self):
        self.assertEqual(self.palm.map_fusion(Blade("first blade")), "arm")
        self.assertEqual(self.palm.map_fusion(Staff("somewhat staff")), "cannon")
        self.assertEqual(self.palm.map_fusion(Claws("raptor claws")), "arm")
        self.assertEqual(self.palm.map_fusion(Bow("silver bow")), "club")
        self.assertEqual(self.palm.map_fusion(Palm("cutter palm")), "arm")
        self.assertEqual(self.palm.map_fusion(Club("magnus club")), "blade")
        self.assertEqual(self.palm.map_fusion(Cannon("doom cannon")), "blade")
        self.assertEqual(self.palm.map_fusion(Orbitars("arlon orbitars")), "bow")
        self.assertEqual(self.palm.map_fusion(Arm("crusher arm")), "orbitars")

    def test_givenClubInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.club.map_fusion(Blade("royal blade")), "staff")
        self.assertEqual(self.club.map_fusion(Staff("flintlock staff")), "claws")
        self.assertEqual(self.club.map_fusion(Claws("brawler claws")), "bow")
        self.assertEqual(self.club.map_fusion(Bow("darkness bow")), "palm")
        self.assertEqual(self.club.map_fusion(Palm("cutter palm")), "blade")
        self.assertEqual(self.club.map_fusion(Club("earthmaul club")), "orbitars")
        self.assertEqual(self.club.map_fusion(Cannon("leo cannon")), "orbitars")
        self.assertEqual(self.club.map_fusion(Orbitars("standard orbitars")), "claws")
        self.assertEqual(self.club.map_fusion(Arm("upperdash arm")), "blade")

    def test_givenCannonInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.cannon.map_fusion(Blade("first blade")), "staff")
        self.assertEqual(self.cannon.map_fusion(Staff("dark pit staff")), "blade")
        self.assertEqual(self.cannon.map_fusion(Claws("beam claws")), "bow")
        self.assertEqual(self.cannon.map_fusion(Bow("angel bow")), "orbitars")
        self.assertEqual(self.cannon.map_fusion(Palm("midnight palm")), "blade")
        self.assertEqual(self.cannon.map_fusion(Club("aurum club")), "orbitars")
        self.assertEqual(self.cannon.map_fusion(Cannon("fireworks cannon")), "palm")
        self.assertEqual(self.cannon.map_fusion(Orbitars("gemini orbitars")), "claws")
        self.assertEqual(self.cannon.map_fusion(Arm("kraken arm")), "staff")

    def test_givenOrbitarsInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.orbitars.map_fusion(Blade("aurum blade")), "palm")
        self.assertEqual(self.orbitars.map_fusion(Staff("scorpio staff")), "club")
        self.assertEqual(self.orbitars.map_fusion(Claws("hedgehog claws")), "staff")
        self.assertEqual(self.orbitars.map_fusion(Bow("phosphora bow")), "cannon")
        self.assertEqual(self.orbitars.map_fusion(Palm("great reaper palm")), "bow")
        self.assertEqual(self.orbitars.map_fusion(Club("babel club")), "claws")
        self.assertEqual(self.orbitars.map_fusion(Cannon("rail cannon")), "claws")
        self.assertEqual(self.orbitars.map_fusion(Orbitars("fairy orbitars")), "cannon")
        self.assertEqual(self.orbitars.map_fusion(Arm("crusher arm")), "palm")

    def test_givenArmInFusion_thenReturnsCorrectOutputWeaponType(self):
        self.assertEqual(self.arm.map_fusion(Blade("first blade")), "bow")
        self.assertEqual(self.arm.map_fusion(Staff("dark pit staff")), "orbitars")
        self.assertEqual(self.arm.map_fusion(Claws("tiger claws")), "staff")
        self.assertEqual(self.arm.map_fusion(Bow("angel bow")), "blade")
        self.assertEqual(self.arm.map_fusion(Palm("pudgy palm")), "orbitars")
        self.assertEqual(self.arm.map_fusion(Club("ore club")), "blade")
        self.assertEqual(self.arm.map_fusion(Cannon("doom cannon")), "staff")
        self.assertEqual(self.arm.map_fusion(Orbitars("boom orbitars")), "palm")
        self.assertEqual(self.arm.map_fusion(Arm("volcano arm")), "bow")

    def test_whenWeaponNameIsParsed_shouldCorrectlySplitTypeAndName(self):
        self.assertEqual(self.staff.name, "dark pit")
        self.assertEqual(self.palm.name, "great reaper")
        self.assertEqual(self.blade.name, "first")

    def test_whenInvalidWeaponNameIsGiven_shouldRaiseValueError(self):
        self.assertRaises(ValueError, Blade, "invalid blade")


if __name__ == "__main__":
    unittest.main()
