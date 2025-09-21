import minescript
import time
import random

with minescript.EventQueue() as events:
    events.register_chat_listener()
    while True:
        event = events.get()
        if event.type == minescript.EventType.CHAT:
            if event.message.lstrip("\n") == ("(!) The first player to solve "):
                expr = event.message.lstrip("\n")[30:-9]
                ans = eval(expr)
                delay = 3 + random.uniform(0, 1.5)
                time.sleep(delay)
                minescript.chat(f"{ans}")

            elif event.message.lstrip("\n")[:34] == "(!) The first player to unreverse ":
                question = event.message.lstrip("\n")[34:-6][::-1]
                delay = 3 + random.uniform(0, 1.5)
                time.sleep(delay)
                minescript.chat(question.lower())

            elif event.message.lstrip("\n")[:29] == "(!) The first player to type ":
                word = event.message.lstrip("\n")[29:-6]
                delay = 3 + random.uniform(0, 1.5)
                time.sleep(delay)
                minescript.chat(word.lower())
