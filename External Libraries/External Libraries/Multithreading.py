# Multithreading in Python
# These techniques allow your programs to perform multiple tasks concurrently, improving performance.
# Multithreading (using threading module):
# Multithreading is suitable for I/O-bound tasks (e.g., waiting for network requests)
# import threading
# import time
# def worker(num):
#     print(f"Thread {num}: Starting")
#     time.sleep(2)  # Simulate some work
#     print(f"Thread {num}: Finishing")
# threads = []
# for i in range(3):
#     thread = threading.Thread(target=worker, args=(i,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()  # Wait for all threads to finish
# print("All threads completed.")



# ***explore multiprocessing module***