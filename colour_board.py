from pynput import keyboard as kb
import string as s
from PIL import Image, ImageGrab
import random
import os

def rgb2hex(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b).upper()

def clip2png():
    
    i = ImageGrab.grabclipboard()
    try:
        width, height = i.size 
    except AttributeError:
        print("The clipboard does not contain an image.")
        return
    rgb_op = i.convert('RGB')
    r,g,b = rgb_op.getpixel(((width/2),(height/2))) # Get middle
    print(rgb2hex(r,g,b))


                      
def on_press(key):
    if key == kb.Key.f2:
        clip2png()
        
def on_release(key):
    if key == kb.Key.f12: # exit
        exit()

with kb.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
listener = kb.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()



    
