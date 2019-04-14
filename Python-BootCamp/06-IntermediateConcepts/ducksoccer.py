#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 14:39:03 2018

@author: denisvrdoljak
"""

import random

class Duck:
    def __init__(self,name=None):
        if name is not None:
            self.name = name.title()
        else:
            self.name = "[unnamed]"

    def nametheduck(self,name):
        assert type(name) == str
        self.name = name.title()

    def quack(self):
        print("{} the Duck says, 'Quack!'".format(self.name))


class SoccerBall:
    def __init__(self):
        pass
    def kick(self):
        print("You kicked the ball...")
        if random.uniform(0, 1) > 0.8:
            print("Goal!")
        else:
            print("You missed the goal.")

