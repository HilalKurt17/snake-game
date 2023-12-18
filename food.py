# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 01:51:03 2023

@author: Hilal
"""

from turtle import Turtle, Screen
from snake import Snake
import random
import time
screen = Screen()

class Food(Turtle):
    
    def __init__(self):    
        super().__init__();
        self.shape("circle");
        self.shapesize(1/3);
        self.color("dark turquoise")
        self.penup();
        self.create_food();
        self.score = 0;
        
    def create_food(self): # create food with random coordinates.
       
        x_coordinate = random.randint(-240,240);
        y_coordinate = random.randint(-240,240);

        self.setposition(x_coordinate,y_coordinate);

        