#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:06:00 2018

@author: fu
"""

class ticket():
    def __init__(self, i, p):
        self.sn = i # unique serial number
        self.price = p

class screen():
    def __init__(self, n, m, d, s):
        self.no = n # screen no.
        self.movie = m
        self.date = d
        self.seats = s
        self.tickets_list_avlb = [] # available tickits list
        self.tickets_list_sold = [] # sold tickets list

    def generate_tickets(self, t): # generate tickets
        tiers = t
        c = self.seats // tiers # seats each tier
        price = 10 # price from tier 1 to 4: $10, $8, $6, $4
        for i in range(tiers):
            for j in range(c):
                sn = str(self.date) + str(self.no).zfill(2) + str(c*i+j+1).zfill(2) + str(i+1)
                self.tickets_list_avlb.append(ticket(sn, price))
            price -= 2

class theater():
    def __init__(self, n, c = 200, s = 5):
        self.name = n
        self.seats = c
        self.ns = s # num of screens
        self.sl = [] # screens list
        
    def gs(self, n, m, d, s): # generate screens
        self.sl.append(screen(n, m, d, s))
        self.sl[-1].generate_tickets(4)
    
    def st(self, m, d, t): # sell tickets
        for i in self.sl:
            if i.movie == m and i.date == d:
                for j in i.tickets_list_avlb:
                    if j.sn[-1] == t:
                        print("Printing ticket:")
                        print(j.sn)
                        i.tickets_list_sold.append(j)
                        i.tickets_list_avlb.remove(j)
                        break
                else:
                    print("All tickets are sold out!")
                break
        else:
            print("Invalid movie/date!")
    
    def rt(self, t): # refund ticket
        for i in self.sl:
            for j in i.tickets_list_sold:
                if j.sn == t:
                    i.tickets_list_sold.remove(j)
                    i.tickets_list_avlb.append(j)
                    print("Refund for your ticket is done.")
                    break
            else:
                continue
            break
        else:
            print("Invalid ticket!")
    
    def stats(self, d, n = 0):
        if n != 0:
            for i in self.sl:
                if i.date == d and i.no == int(n):
                    print("Total seats: ", i.seats)
                    print("Tickets sold: ", len(i.tickets_list_sold))
                    print("Vacant seats: ", len(i.tickets_list_avlb))
                    break
            else:
                print("Invalid date!")
        else:
            ts = 0
            for i in self.sl:
                if i.date == d:
                    ts += len(i.tickets_list_sold)
            print("Total tickets sold: ", ts)
    