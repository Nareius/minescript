
import minescript
import time

i = 0

# sends a message to the text file so invetory_crafter.py knows what to do
with open("/home/nareius/Documents/curseforge/minecraft/Instances/test/batteries.txt", "a") as f:
    f.write("W8"+ "\n")  

file_path = "/home/nareius/Documents/curseforge/minecraft/Instances/test/batteries.txt"

while True:

    # Read the last line of the file
    with open(file_path) as f:
        last_line = None
        for line in f:
            last_line = line.rstrip("\n")

    if last_line is None:
        time.sleep(1)
        continue  # skip empty file

    # Check the last line and act accordingly
    if last_line == "W8":
        for i in range (300):
            minescript.player_press_attack(True)
            minescript.player_press_attack(False)
            time.sleep(0.02)

        minescript.execute("/batteries")
        with open(file_path, "a") as f:
            f.write("Batteries\n")

    elif last_line == "Ready_1":
        minescript.player_set_orientation(-1.9/-20, 7)
        minescript.player_press_use(True)
        with open(file_path, "a") as f:
            f.write("Chest\n")

    elif last_line == "Ready_2":
        minescript.player_set_orientation(-130, 30)
        with open(file_path, "a") as f:
            f.write("W8\n")
