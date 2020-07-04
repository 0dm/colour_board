from pynput import keyboard as kb
import string as s
from PIL import Image, ImageGrab
import random
import os

def rgb2hex(r,g,b):
    return '#{:02x}{:02x}{:02x}{:02x}'.format(r,g,b,a).upper()

def clip2png():
    ic = ImageGrab.grabclipboard()
    suffix = ''.join(random.choice(s.digits) for _ in range(3))
    name = 'CB_' + suffix + '.png'
    dir = os.path.join(os.getcwd(), 'temp')
    path = os.path.join(dir, name)
    
    try:
        ic.save(path,'png')
    except AttributeError:
        print("The clipboard does not contain an image.")
        return
        
    i = Image.open(path)    
    width, height = i.size 
    rgb_op = i.convert('RGBA')
    r,g,b,a = rgb_op.getpixel(((width/2),(height/2))) # Get middle
    print(rgb2hex(r,g,b,a))

                      
def on_press(key):
    if key == kb.Key.f2:
        clip2png()
    if key == kb.Key.f12: # exit
        exit()   

with kb.Listener(
        on_press=on_press) as listener:
    listener.join()



    
