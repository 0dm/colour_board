from pynput import keyboard as kb
import string as s
from PIL import Image, ImageGrab
import random
import os

# Format RGB to Hex
def rgb2hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b).upper()


# Grabs image from clipboard and outputs color from pixels.
def clip2png():
    i = ImageGrab.grabclipboard()

    # if there's no image on clipboard, return
    try:
        width, height = i.size 
    except AttributeError:
        print("The clipboard does not contain an image.")
        return
    rgb_op = i.convert('RGB')
    r,g,b = rgb_op.getpixel(((width/2),(height/2))) # Get middle
    print(rgb2hex(r,g,b))


# On Key Pressed Event                      
def on_press(key):
    if key == kb.Key.f2:
        clip2png()
    elif key == kb.Key.f12: # exit
        exit()

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()




    
