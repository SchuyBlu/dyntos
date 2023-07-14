"""
Author: Feanor
Testing weapon type conversions. Test for every fusion possible.
"""
import unittest
from lib.weapons import *

class TestWeapons(unittest.TestCase):
    def setUp(self):
        self.blade = Blade()
        self.staff = Staff()
        self.claws = Claws()
        self.bow = Bow()
        self.palm = Palm()
        self.club = Club()
        self.cannon = Cannon()
        self.orbitars = Orbitars()
        self.arm = Arm()

    def test_givenBladeAndVariableCaps_thenReturnsCorrectOutput(self):
        self.assertEqual(self.blade.map_fusion("BLADE"), "claws")
        self.assertEqual(self.blade.map_fusion("Staff"), "claws")
        self.assertEqual(self.blade.map_fusion("cLAws"), "club")
        self.assertEqual(self.blade.map_fusion("bOW"), "palm")
        self.assertEqual(self.blade.map_fusion("palM"), "arm")
        self.assertEqual(self.blade.map_fusion("club"), "staff")
        self.assertEqual(self.blade.map_fusion("Cannon"), "staff")
        self.assertEqual(self.blade.map_fusion("ORBItars"), "palm")
        self.assertEqual(self.blade.map_fusion("arm"), "bow")

    def test_givenStaff_thenReturnsCorrectOutput(self):
        self.assertEqual(self.staff.map_fusion("blade"), "claws")
        self.assertEqual(self.staff.map_fusion("staff"), "cannon")
        self.assertEqual(self.staff.map_fusion("claws"), "arm")
        self.assertEqual(self.staff.map_fusion("bow"), "arm")
        self.assertEqual(self.staff.map_fusion("palm"), "cannon")
        self.assertEqual(self.staff.map_fusion("club"), "claws")
        self.assertEqual(self.staff.map_fusion("cannon"), "blade")
        self.assertEqual(self.staff.map_fusion("orbitars"), "club")
        self.assertEqual(self.staff.map_fusion("arm"), "orbitars")

    def test_givenClaws_thenReturnsCorrectOutput(self):
        self.assertEqual(self.claws.map_fusion("blade"), "club")
        self.assertEqual(self.claws.map_fusion("staff"), "arm")
        self.assertEqual(self.claws.map_fusion("claws"), "club")
        self.assertEqual(self.claws.map_fusion("bow"), "club")
        self.assertEqual(self.claws.map_fusion("palm"), "arm")
        self.assertEqual(self.claws.map_fusion("club"), "bow")
        self.assertEqual(self.claws.map_fusion("cannon"), "bow")
        self.assertEqual(self.claws.map_fusion("orbitars"), "staff")
        self.assertEqual(self.claws.map_fusion("arm"), "staff")

    def test_givenBow_thenReturnsCorrectOutput(self):
        self.assertEqual(self.bow.map_fusion("blade"), "palm")
        self.assertEqual(self.bow.map_fusion("staff"), "arm")
        self.assertEqual(self.bow.map_fusion("claws"), "club")
        self.assertEqual(self.bow.map_fusion("bow"), "cannon")
        self.assertEqual(self.bow.map_fusion("palm"), "club")
        self.assertEqual(self.bow.map_fusion("club"), "palm")
        self.assertEqual(self.bow.map_fusion("cannon"), "orbitars")
        self.assertEqual(self.bow.map_fusion("orbitars"), "cannon")
        self.assertEqual(self.bow.map_fusion("arm"), "blade")

    def test_givenPalm_thenReturnsCorrectOutput(self):
        self.assertEqual(self.palm.map_fusion("blade"), "arm")
        self.assertEqual(self.palm.map_fusion("staff"), "cannon")
        self.assertEqual(self.palm.map_fusion("claws"), "arm")
        self.assertEqual(self.palm.map_fusion("bow"), "club")
        self.assertEqual(self.palm.map_fusion("palm"), "arm")
        self.assertEqual(self.palm.map_fusion("club"), "blade")
        self.assertEqual(self.palm.map_fusion("cannon"), "blade")
        self.assertEqual(self.palm.map_fusion("orbitars"), "bow")
        self.assertEqual(self.palm.map_fusion("arm"), "orbitars")

    def test_givenClub_thenReturnsCorrectOutput(self):
        self.assertEqual(self.club.map_fusion("blade"), "staff")
        self.assertEqual(self.club.map_fusion("staff"), "claws")
        self.assertEqual(self.club.map_fusion("claws"), "bow")
        self.assertEqual(self.club.map_fusion("bow"), "palm")
        self.assertEqual(self.club.map_fusion("palm"), "blade")
        self.assertEqual(self.club.map_fusion("club"), "orbitars")
        self.assertEqual(self.club.map_fusion("cannon"), "orbitars")
        self.assertEqual(self.club.map_fusion("orbitars"), "claws")
        self.assertEqual(self.club.map_fusion("arm"), "blade")

    def test_givenCannon_thenReturnsCorrectOutput(self):
        self.assertEqual(self.cannon.map_fusion("blade"), "staff")
        self.assertEqual(self.cannon.map_fusion("staff"), "blade")
        self.assertEqual(self.cannon.map_fusion("claws"), "bow")
        self.assertEqual(self.cannon.map_fusion("bow"), "orbitars")
        self.assertEqual(self.cannon.map_fusion("palm"), "blade")
        self.assertEqual(self.cannon.map_fusion("club"), "orbitars")
        self.assertEqual(self.cannon.map_fusion("cannon"), "palm")
        self.assertEqual(self.cannon.map_fusion("orbitars"), "claws")
        self.assertEqual(self.cannon.map_fusion("arm"), "staff")

    def test_givenOrbitars_thenReturnsCorrectOutput(self):
        self.assertEqual(self.orbitars.map_fusion("blade"), "palm")
        self.assertEqual(self.orbitars.map_fusion("staff"), "club")
        self.assertEqual(self.orbitars.map_fusion("claws"), "staff")
        self.assertEqual(self.orbitars.map_fusion("bow"), "cannon")
        self.assertEqual(self.orbitars.map_fusion("palm"), "bow")
        self.assertEqual(self.orbitars.map_fusion("club"), "claws")
        self.assertEqual(self.orbitars.map_fusion("cannon"), "claws")
        self.assertEqual(self.orbitars.map_fusion("orbitars"), "cannon")
        self.assertEqual(self.orbitars.map_fusion("arm"), "palm")

    def test_givenArm_thenReturnsCorrectOutput(self):
        self.assertEqual(self.arm.map_fusion("blade"), "bow")
        self.assertEqual(self.arm.map_fusion("staff"), "orbitars")
        self.assertEqual(self.arm.map_fusion("claws"), "staff")
        self.assertEqual(self.arm.map_fusion("bow"), "blade")
        self.assertEqual(self.arm.map_fusion("palm"), "orbitars")
        self.assertEqual(self.arm.map_fusion("club"), "blade")
        self.assertEqual(self.arm.map_fusion("cannon"), "staff")
        self.assertEqual(self.arm.map_fusion("orbitars"), "palm")
        self.assertEqual(self.arm.map_fusion("arm"), "bow")


if __name__ == "__main__":
    unittest.main()
