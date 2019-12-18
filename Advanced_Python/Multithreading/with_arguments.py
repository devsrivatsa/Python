import threading
import time

def somefunction(seconds):
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds)

start = time.perf_counter()
threads=[]
for _ in range(10):
     thread = threading.Thread(target=somefunction,args=[1.5])
     thread.start()
     threads.append(thread)

for t in threads:
    t.join()

stop = time.perf_counter()

print(f"It took {stop-start} second(s) for execution")
