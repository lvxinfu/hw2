#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 17:06:00 2018

@author: fu
"""

class Theater():
    def __init__(self, name, c = 200, s = 5):
        self.name = name
        self.seats = c
        self.ns = s # num of screens
        self.screens_list = [] # screens list
        
    def generate_screens(self, n, movie, date, seats): # generate screens
        self.screens_list.append(Screen(n, movie, date, seats))
        self.screens_list[-1].generate_tickets(4)
    
    def sell_tickets(self, movie, date, tier): # sell tickets
        for i in self.screens_list:
            if i.movie == movie and i.date == date:
                for j in i.tickets_list_avlb:
                    if j.serial_number[-1] == tier:
                        print("Printing ticket:")
                        print(j.serial_number)
                        i.tickets_list_sold.append(j)
                        i.tickets_list_avlb.remove(j)
                        break
                else:
                    print("All tickets are sold out!")
                break
        else:
            print("Invalid movie/date!")
    
    def refund_ticket(self, serial_number): # refund ticket
        for i in self.screens_list:
            for j in i.tickets_list_sold:
                if j.serial_number == serial_number:
                    i.tickets_list_sold.remove(j)
                    i.tickets_list_avlb.append(j)
                    print("Refund for your ticket is done.")
                    break
            else:
                continue
            break
        else:
            print("Invalid ticket!")
    
    def stats(self, date, n = 0):
        if n != 0:
            for i in self.screens_list:
                if i.date == date and i.no == int(n):
                    print("Total seats: ", i.seats)
                    print("Tickets sold: ", len(i.tickets_list_sold))
                    print("Vacant seats: ", len(i.tickets_list_avlb))
                    break
            else:
                print("Invalid date!")
        else:
            total_sold = 0
            for i in self.screens_list:
                if i.date == date:
                    total_sold += len(i.tickets_list_sold)
            print("Total tickets sold: ", total_sold)

class Screen():
    def __init__(self, n, movie, date, seats):
        self.no = n # screen no.
        self.movie = movie
        self.date = date
        self.seats = seats
        self.tickets_list_avlb = [] # available tickits list
        self.tickets_list_sold = [] # sold tickets list

    def generate_tickets(self, t): # generate tickets
        tiers = t
        c = self.seats // tiers # seats each tier
        price = 10 # price from tier 1 to 4: $10, $8, $6, $4
        for i in range(tiers):
            for j in range(c):
                serial_number = str(self.date) + str(self.no).zfill(2) + str(c*i+j+1).zfill(2) + str(i+1)
                self.tickets_list_avlb.append(Ticket(serial_number, price))
            price -= 2

class Ticket():
    def __init__(self, i, price):
        self.serial_number = i # unique serial number
        self.price = price