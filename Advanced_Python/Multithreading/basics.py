import threading
import time

"This is how you can build threads"

def somefunction():
    print("sleeping for 1 second")
    time.sleep(1)


thread1 = threading.Thread(target=somefunction)
thread2 = threading.Thread(target=somefunction)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
