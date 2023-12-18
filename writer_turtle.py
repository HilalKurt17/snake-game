# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 19:48:39 2023

@author: Hilal
"""

from turtle import Turtle,Screen;

class Writer(Turtle):
    
    def __init__(self):
        super().__init__();
        
        self.penup();
        self.hideturtle();
        self.screen = Screen()
    
    def score(self, score, color_score): # write score to score board.

        self.color(color_score);
        self.setposition(-220,230);
        self.clear();
        self.write("Score: {0}".format(score), True, align = "center", font=('Arial', 15, 'normal'));
   
    def game_over(self): 
        self.setposition(0,0)
        self.write("GAME OVER...", True, align = "center", font=('Arial', 20, 'bold'))
