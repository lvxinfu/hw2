#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:29:50 2018

@author: fu
"""

import unittest
import box_office as bo

class TestTheater(unittest.TestCase):
    Box_Office_test = bo.AppShell()

    def test_name(self):
        self.assertEqual(self.Box_Office_test.mt.name, "my_theater")

if __name__ == '__main__':
    unittest.main()