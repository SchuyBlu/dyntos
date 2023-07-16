"""
Author: Feanor
Testing weapon ids for all weapon types.
"""
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
        self.assertEqual(self.first_blade.weapon_id, 1)
        self.assertEqual(self.gaol_blade.weapon_id, 12)
        self.assertEqual(self.insight_staff.weapon_id, 1)
        self.assertEqual(self.thanatos_staff.weapon_id, 12)
        self.assertEqual(self.tiger_claws.weapon_id, 1)
        self.assertEqual(self.pandora_claws.weapon_id, 12)
        self.assertEqual(self.fortune_bow.weapon_id, 1)
        self.assertEqual(self.phosphora_bow.weapon_id, 12)
        self.assertEqual(self.violet_palm.weapon_id, 1)
        self.assertEqual(self.great_reaper_palm.weapon_id, 12)
        self.assertEqual(self.ore_club.weapon_id, 1)
        self.assertEqual(self.magnus_club.weapon_id, 12)
        self.assertEqual(self.ez_cannon.weapon_id, 1)
        self.assertEqual(self.cragalanche_cannon.weapon_id, 12)
        self.assertEqual(self.standard_orbitars.weapon_id, 1)
        self.assertEqual(self.arlon_orbitars.weapon_id, 12)
        self.assertEqual(self.crusher_arm.weapon_id, 1)
        self.assertEqual(self.phoenix_arm.weapon_id, 12)


if __name__ == "__main__":
    unittest.main()

