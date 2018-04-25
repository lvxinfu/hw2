#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 10:29:50 2018

@author: fu
"""

import unittest
import box_office as bo

Box_Office_test = bo.AppShell()

class TestTheater(unittest.TestCase):
    def test_name(self):
        '''Test Theater name'''
        self.assertEqual(Box_Office_test.mt.name, "my_theater")

    def test_seats(self):
        '''Test Theater seats'''
        self.assertEqual(Box_Office_test.mt.seats, 200)

class TestBuy(unittest.TestCase):
    movie_test = "my_movie_1"
    date_test = "20180401"
    tier_test = "3"

    def test_buy(self):
        '''Test length of available tickets list decreases by 1 after sell a ticket'''
        for i in Box_Office_test.mt.screens_list:
            if i.movie == self.movie_test and i.date == self.date_test:
                I = i
                l0 = len(i.tickets_list_avlb)
                break
        Box_Office_test.mt.sell_tickets(self.movie_test, self.date_test, self.tier_test)
        l1 = len(I.tickets_list_avlb)
        self.assertEqual(l0 - 1, l1)

if __name__ == '__main__':
    unittest.main()