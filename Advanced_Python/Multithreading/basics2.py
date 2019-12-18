"""suppose you wanted to execute the dosomething function multiple times"""

import threading
import time

def somefunction():
    print("sleeping for 1 second")
    time.sleep(1)

start = time.perf_counter()
threads=[]
for _ in range(10):
     thread = threading.Thread(target=somefunction)
     thread.start()
     threads.append(thread)

for t in threads:
    t.join()

stop = time.perf_counter()

print(f"It took {start-stop} second(s) to execution")
