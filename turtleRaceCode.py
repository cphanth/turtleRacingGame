#!/bin/python3

#import turtle package
from turtle import *
#import random int package
from random import randint

speed(0)

penup()
goto(-140, 140)

for step in range(15):
  write(step, align='center')
  right(90)
  forward(10)
#  forward(150)
  for dash in range(10):
    pendown()
    forward(8)
    penup()
    forward(7)
  penup()
  backward(160)
  left(90)
  forward(20)

#creating an instance of a turtle
ada = Turtle()
ada.color('red')
ada.shape('turtle')
#position ada turtle
ada.penup()
ada.goto(-160, 100)
ada.pendown()

for turn in range(10):
  ada.right(36)

#create bob turtle
bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160, 70)
bob.pendown()

for turn in range(36):
  bob.left(10)

ted = Turtle()
ted.color('orange')
ted.shape('turtle')
ted.penup()
ted.goto(-160, 40)
ted.pendown()

for turn in range(4):
  ted.right(90)

cal = Turtle()
cal.color('purple')
cal.shape('turtle')
cal.penup()
cal.goto(-160, 10)
cal.pendown()

for turn in range(12):
  cal.left(30)

speed(30)


for turn in range(100):
  ada.forward(randint(1,5))
  bob.forward(randint(1,5))
  ted.forward(randint(1,5))
  cal.forward(randint(1,5))
