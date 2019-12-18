import concurrent.futures
import time

def somefunction(seconds):
    print(f"sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f'Done Sleeping for {seconds} second(s)'

start = time.perf_counter()
"""Its best to use a context manager here"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    #works best if secs is initialized inside the context manager
    secs = [1,2,5,8,14,6,12,9]
    #Creating a list comprehension
    results = [executor.submit(somefunction, sec) for sec in secs]
    for f in concurrent.futures.as_completed(results):
        print(f.result())
stop = time.perf_counter()

print(f"It took {stop-start} second(s) for execution")
