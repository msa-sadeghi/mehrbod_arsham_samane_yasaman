# f = open("test", "w")
# print("hello", "friends", "!", sep="-", end=" ", file=f)
# print("HOW ARE YOU TODAY", file=f)

import time
message = "Hello my friends, How are you today"
for c in message:
    print(c, end="", flush=True)
    time.sleep(0.2)
    