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
    def test_do_buy(self):
        '''Test do_buy under different conditions'''
        Box_Office_test.do_buy("my_movie_1 20180401 1")
        print()
        Box_Office_test.do_setd("20180401") # set today's date
        print()
        Box_Office_test.do_buy("my_movie_1 20180401 1")
        print()
        Box_Office_test.do_buy("my_movie_1 20180410 2")
        print()

    def test_buy(self):
        '''Test length of available tickets list decreases by 1 after sell a ticket'''
        movie_test = "my_movie_1"
        date_test = "20180401"
        tier_test = "3"
    
        for i in Box_Office_test.mt.screens_list:
            if i.movie == movie_test and i.date == date_test:
                I = i
                break
        
        l0 = len(I.tickets_list_avlb)
        Box_Office_test.mt.sell_tickets(movie_test, date_test, tier_test)
        l1 = len(I.tickets_list_avlb)
        
        self.assertEqual(l0 - 1, l1)
        print()

class TestRefund(unittest.TestCase):    
    def test_do_refund(self):
        '''Test do_refund under different conditions'''
        Box_Office_test.do_refund("2018040101011")
        print()
        Box_Office_test.do_refund("2018040101112")
        print()
        Box_Office_test.do_setd("20180402") # set today's date
        print()
        Box_Office_test.do_refund("2018040101213")
        print()

    def test_refund(self):
        '''Test length of available tickets list increases by 1 after refund a ticket'''
        Box_Office_test.do_setd("20180402") # set today's date
        print()
        Box_Office_test.do_buy("my_movie_1 20180402 1")
        print()
        serial_number_test = "2018040201011"
        
        for i in Box_Office_test.mt.screens_list:
            for j in i.tickets_list_sold:
                if j.serial_number == serial_number_test:
                    I = i
                    break
        
        l0 = len(I.tickets_list_avlb)
        Box_Office_test.mt.refund_ticket("2018040201011")
        l1 = len(I.tickets_list_avlb)
        
        self.assertEqual(l0 + 1, l1)
        print()

class TestStats(unittest.TestCase):
    def test_do_stats(self):
        '''Test do_stats under different conditions'''
        Box_Office_test.do_stats("20180400") # need to dectect invalid date, but not done yet
        print()
        Box_Office_test.do_stats("20180401")
        print()
        Box_Office_test.do_stats("20180402")
        print()
        
        Box_Office_test.do_stats("20180401 1")        
        print()

if __name__ == '__main__':
    unittest.main()