"""
Created on Fri Dec  8 19:50:17 2023

@author: Hilal
"""
from turtle import Turtle, Screen
from writer_turtle import Writer
import time

screen = Screen();
snake_size = 7;
n = 3;

class Snake():
    
    def __init__(self):
        self.snake_parts = [];
        self.create_snake()
        self.snake_head = self.snake_parts[0];
        self.writer = Writer()


    def create_snake(self): # create snake with 3 segments
        for i in range(0,n):
            self.snake = Turtle();
            self.snake.shape("square");
            self.snake.speed(10)
            self.snake.penup();
            self.snake.shapesize(1/2)
            self.snake_parts.append(self.snake);
        for i in range(0,n):

            self.snake_parts[i].setposition((-i*snake_size,0))
    
    def is_there_collision(self): # check whether snake bites itself or not
        is_game_over = False
        for i in range(1,len(self.snake_parts)):
            if self.snake_parts[0].position() == self.snake_parts[i].position():
                self.writer.game_over()
                is_game_over = True;
                break;
        return is_game_over
    
    
    def snake_longer(self,color): # increase lenght of the snake when it eats food.

        self.last_position = self.snake_parts[len(self.snake_parts)-1].position();
        self.heading = self.snake_parts[len(self.snake_parts)-1].heading();
        self.snake = Turtle();
        self.snake.shape("square");
        self.snake.speed(10)
        self.snake.penup();
        self.snake.color(color)
        self.snake.shapesize(1/2)
        self.snake.setposition(self.last_position)
        self.snake.setheading(self.heading)
        self.snake_parts.append(self.snake);

    
    
    def move_snake(self):  # move snake when keys are not used
        
        for i in range(1,len(self.snake_parts)+1):
            if (len(self.snake_parts)-i) == 0:
                self.snake_parts[len(self.snake_parts)-i].forward(snake_size)
            else:
                self.position = self.snake_parts[len(self.snake_parts)-1-i].position()
                self.snake_parts[len(self.snake_parts)-i].setposition(self.position)
         
    def move(self, degree, forbidden_degree): # move snake when keys are used
        j = -1
        for i in range(len(self.snake_parts)):  # each snake segment takes the position of the previous segment
            if (self.snake_parts[i].heading() != forbidden_degree):
                if i != len(self.snake_parts)-1:
                    self.snake_parts[j-i].setheading(degree)
                    self.snake_parts[j-i].setposition(self.snake_parts[j-i-1].position())
                else:
                    self.snake_parts[j-i].setheading(degree);
                    self.snake_parts[j-i].forward(snake_size) 
        screen.update();
        time.sleep(0.1);
            
    def move_up(self):  # move the snake to the North
        self.move(90,270)


    def move_down(self): # move the snake to the South
        self.move(270,90)          

    def move_left(self): # move the snake to the West
        self.move(180,0)        

    def move_right(self): # move the snake to the East
        self.move(0,180)        














