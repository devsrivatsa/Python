import concurrent.futures
import time

def somefunction(seconds):
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} second(s)'

start = time.perf_counter()
"""Its best to use a context manager here"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(somefunction, 10)
    f2 = executor.submit(somefunction, 6)
    f3 = executor.submit(somefunction, 3)
    print(f1.result())
    print(f2.result())
    print(f3.result())
stop = time.perf_counter()

print(f"It took {stop-start} second(s) for execution")
