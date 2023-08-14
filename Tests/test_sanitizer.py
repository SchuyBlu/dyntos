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
from lib.sanitizer import *


class TestSanitizer(unittest.TestCase):
    def test_givenStringWithHTTP_thenShouldReturnTrue(self):
        self.assertTrue(contains_url("some text http://testing.com is a url"))
        self.assertTrue(contains_url("http://facebook.com is a url"))
        self.assertTrue(contains_url("some text in from of url http://youtube.com"))

    def test_givenStringWithHTTPS_thenShouldReturnTrue(self):
        self.assertTrue(contains_url("some text https://testing.com is a url"))
        self.assertTrue(contains_url("https://facebook.com is a url"))
        self.assertTrue(contains_url("some text in from of url https://youtube.com"))

    def test_givenStringWithoutURL_thenShouldReturnFalse(self):
        self.assertFalse(contains_url("youtube.com is a website but not a URL"))
        self.assertFalse(contains_url("httpsis a valid string"))
        self.assertFalse(contains_url("http is valid"))
        self.assertFalse(contains_url("http:/Should_also_be_valid.com"))


if __name__ == "__main__":
    unittest.main()

