from pynput.mouse import Controller as MouseController, Button
from pynput.keyboard import Controller as KeyboardController, Key
import time


mouse = MouseController()
keyboard = KeyboardController()


def insert_items_batteries():
    time.sleep(2)

    #take first porkchop
    mouse.position = (668, 914)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)

        #move to second and double click it with shift
    mouse.position = (749, 912)
    keyboard.press(Key.shift)
    mouse.click(Button.left)
    mouse.click(Button.left)

        #release shift 
    time.sleep(0.5)
    keyboard.release(Key.shift)
    mouse.click(Button.left)
    time.sleep(0.5)
    keyboard.press(Key.shift)
    mouse.click(Button.left)
    keyboard.release(Key.shift)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1.5) 
    
def insert_items_chest():
    time.sleep(2)

    #take first porkchop
    mouse.position = (675, 918)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.5)

    #move to second and double click it with shift
    mouse.position = (741, 924)
    keyboard.press(Key.shift)
    mouse.click(Button.left)
    mouse.click(Button.left)

    #release shift 
    time.sleep(0.5)
    keyboard.release(Key.shift)
    mouse.click(Button.left)
    time.sleep(0.5)
    keyboard.press(Key.shift)
    mouse.click(Button.left)
    keyboard.release(Key.shift)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(1.5) 

file_path = "/home/nareius/Documents/curseforge/minecraft/Instances/test/batteries.txt"

while True:
    with open(file_path) as f:
        last_line = None
        for line in f:
            last_line = line.rstrip("\n")

    if last_line is None:
        time.sleep(1)
        continue  # skip empty file

    if last_line == "Batteries":
        insert_items_batteries()
        with open(file_path, "a") as f:
            f.write("Ready_1\n")
        
    elif last_line == "Chest":
        insert_items_chest()
        with open(file_path, "a") as f:
            f.write("Ready_2\n") 
