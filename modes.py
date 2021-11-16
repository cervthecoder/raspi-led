#!usr/bin/python

'''
This program is for controling rgb led strip with rapsberry pi

'''

import pigpio
from PIL import ImageColor
import time
import os

#configuration
pi = pigpio.pi() #accesses the local Pi's GPIO

# define pins
RED_PIN = 17
GREEN_PIN = 24
BLUE_PIN = 22

stop = False

# simple colors
colors = {
    "white": [255, 255, 255],
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255],
    "yellow": [255, 255, 0],
    "cyan": [0, 255, 255],
    "magenta": [255, 0, 255],
    "orange": [255, 165, 0],
    "gold": [255, 215, 0],
    "violet": [255, 165, 0]
}

# modes

def write_pwm(r, g, b):
    pi.set_PWM_dutycycle(RED_PIN, r)
    pi.set_PWM_dutycycle(GREEN_PIN, g)
    pi.set_PWM_dutycycle(BLUE_PIN, b)

def print_colors():
    print(colors.keys())

def rgb(rgb):
    colors = rgb.split(", ")
    return [int(i) for i in colors]

def rgba_color(rgb):# Takes color in format "r, g, b"
    red, green, blue = rgb(rgb)
    write_pwm(red, green, blue)
#def hex_color(hex):# Takes hex color format
#    red, green, blue = ImageColor.getcolor(rgb, "RGB")
#    write_pwm(red, green, blue)
def simple_color(color, intensity):# Writes simple color from the dictionary above with intensity between 0 and 1
    red, green, blue = colors[color]
    write_pwm(red*intensity, green*intensity, blue*intensity)

def fade():
    intensity = [pi.get_PWM_dutycycle(RED_PIN), pi.get_PWM_dutycycle(GREEN_PIN), pi.get_PWM_dutycycle(BLUE_PIN)]
    red, green, blue = [int(i)*0.9 for i in intensity]
    write_pwm(red, green, blue)

def bright():
    intensity = [pi.get_PWM_dutycycle(RED_PIN), pi.get_PWM_dutycycle(GREEN_PIN), pi.get_PWM_dutycycle(BLUE_PIN)]
    if intensity[0]*1.1 <= 255 and intensity[1]*1.1 <= 255 and intensity[2]*1.1 <= 255:
        red, green, blue = [int(i)*1.1 for i in intensity]
        write_pwm(red, green, blue)
    else:
        print("Cannot be any brighter")

def fading(t):# Fading one color with time in between changes as arguement
    intensity = [pi.get_PWM_dutycycle(RED_PIN), pi.get_PWM_dutycycle(GREEN_PIN), pi.get_PWM_dutycycle(BLUE_PIN)]
    red, green, blue = intensity
    while stop == False:
        while red*1.05 <= 255 and green*1.05 <= 255 and blue*1.05 <= 255:
            time.sleep(t/2)
            red, green, blue = red*1.1, green*1.1, blue*1.1
            write_pwm(red, green, blue)
            time.sleep(t/2)
        while red*0.95 > 40 and green*0.95 > 40 and blue*0.95 > 40:
            time.sleep(t/2)
            red, green, blue = red*0.9, green*0.9, blue*0.9
            write_pwm(red, green, blue)
            time.sleep(t/2)
def change_colors(t, intensity):# Changing between colors, time is the period of change, intensity between 0 and 1
    if intensity > 0 and intensity <= 1:
        for red, green, blue in colors.values():
            write_pwm(red*intensity, green*intensity, blue*intensity)
            time.sleep(t)
    else:
        print("Wrong intensity, it needs to be number between 0 and 1")
          
