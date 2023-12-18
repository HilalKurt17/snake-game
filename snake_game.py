# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 03:20:37 2023

@author: Hilal Kurt
"""
from turtle import Screen,Turtle;
from writer_turtle import Writer
from snake import Snake;
from food import Food;
import time

class Snake_Game():
    def __init__(self):
        # create screen and world coordinates
        self.screen = Screen();
        self.screen.setworldcoordinates(-250, -250, 250, 250)
        self.screen.tracer(0)
        
        self.writer_turtle = Writer(); # create writer turtle object 
        self.snake = Snake(); # create snake object
        self.food = Food(); # create food object
        self.score = 0;  # score attribute to keep score
        self.is_game_over = False;
        
        self.light_mode();
        self.begin_game();
    
    
    def light_mode(self):
        mode = self.screen.textinput("Light Mode", "Dark/Light"); # ask user for light mode
        if mode.lower() == "light":
            self.screen.bgcolor("light blue")
            self.color = "black"
            self.color_score = "midnight blue"
            self.food.color("black")
        else:
            self.screen.bgcolor("midnight blue")
            self.color = "white"
            self.color_score = "light cyan"
            self.food.color("white")
            
        for snake in self.snake.snake_parts:
            snake.color(self.color)
            
    def begin_game(self):
        
        
        while not self.is_game_over: 
            self.screen.update(); 
            time.sleep(0.1);
            self.snake.move_snake(); 
            
            # if snake and food collides increase score and snake length
            if self.snake.snake_parts[0].distance(self.food) < 10:
                self.food.create_food()
                self.score += 1;
                self.snake.snake_longer(self.color);
            
            self.writer_turtle.score(self.score,self.color_score); # rewrite score on score board
            
            # when snake hits the walls, game is over.
            if self.snake.snake_parts[0].xcor() >= 250 or self.snake.snake_parts[0].xcor() <= -250 or self.snake.snake_parts[0].ycor() >= 250 or self.snake.snake_parts[0].ycor() <= -250: 
                self.writer_turtle.game_over()
                break;
                
            self.is_game_over = self.snake.is_there_collision(); # if snake bites itself game is over.
            self.listen()

    
        self.screen.exitonclick()
        
    # listen to user instructions
    def listen(self):
        self.screen.listen()
        self.screen.onkeyrelease(fun=self.snake.move_up, key="Up");
        self.screen.onkeyrelease(fun=self.snake.move_down, key="Down");
        self.screen.onkeyrelease(fun=self.snake.move_right, key="Right");
        self.screen.onkeyrelease(fun=self.snake.move_left, key="Left");
       
Snake_Game();