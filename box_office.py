#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:26:32 2018

@author: fu
"""

import cmd
import tickets as t

class AppShell(cmd.Cmd):
    intro = "\nWelcome to the My App!\nType `help` or `?` to list commands.\n"
    prompt = '> '
    event = None
    
    mt = t.Theater("my_theater")
    mt.generate_screens(1, "my_movie_1", "20180401", 40)
    mt.generate_screens(2, "my_movie_2", "20180401", 40)        

    def do_quit(self, arg):
      """Quit"""
      return True
      
    def do_buy(self, args):
      """Buy a Ticket"""
      args = args.split()
      if hasattr(self, 'today'):
          if int(args[1]) - int(self.today) <= 7:
              for i in range(int(args[-1])):
                  self.mt.sell_tickets(args[0], args[1], args[2])
                  print()
          else:
              print("Tickets are sold up to 7 days in advance!")
      else:
          print("Date of today need to be set up first!")
          
    def do_refund(self, args):
      """Refund a Ticket"""
      if int(self.today) <= int(args[0:8]):
          self.mt.refund_ticket(args)
      else:
          print("Refunds can only be given if the movie hasn't started yet!")
      
    def do_stats(self, args):
      """Show screen stats"""
      args = args.split()
      if len(args) == 1:
          self.mt.stats(args[0])
      else:
          self.mt.stats(args[0], args[1])
    
    def do_setd(self, args):
      """Set today's date"""
      self.today = args
      print("Set today's date to", args)
      self.mt.generate_screens(1, "my_movie_1", self.today, 40)

if __name__ == '__main__':
    AppShell().cmdloop()