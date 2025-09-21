import minescript
import time
import file

i = 0
start_time = time.time()
while True:
    minescript.player_press_attack(True)
    minescript.player_press_attack(False)
    time.sleep(0.05)
    i += 1

    if i == 800:
        # Compute elapsed time since script started
        elapsed = time.time() - start_time
        minescript.echo(f"Time passed since script started: {elapsed:.2f} seconds")

        # Execute batteries command
        minescript.execute("/batteries")
        time.sleep(10)

        minescript.player_set_orientation(-1.9/-20, 7)
        minescript.player_press_use(True)
        time.sleep(13)
        minescript.player_set_orientation(-130, 30)
        # Reset i for next cycle
        i = 0
