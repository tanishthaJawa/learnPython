import time
from threading import Thread, Lock, current_thread
from queue import Queue

database_value = 0


# def square_numbers():
#     for i in range(100):
#         i * i
#         time.sleep(0.1)
#
#
# num_threads = 10
# threads = []
#
# # create threads
# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()


# share data between threads
def increase(lock):
    global database_value

    with lock:
        local_copy = database_value

        # processing
        local_copy += 1
        time.sleep(0.1)
        database_value = local_copy


if __name__ == "__main__":
    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print('end value', database_value)
print('end main')

# q.put(1)
# q.put(2)
# q.put(3)
#
# first = q.get()
#
# q.task_done() # after you are done with processing queue element you should call task done
# print(first)
#
# q.join() # block the main thread and wait until all the elements of q are done

num_threads = 10


def worker(q, lock):
    while True:
        value = q.get()

        # processing
        with lock:
            print(f' in {current_thread().name} got {value}')
        q.task_done()


q = Queue()
lock = Lock()

for i in range(num_threads):
    thread = Thread(target=worker, args=(q, lock))
    thread.daemon = True
    thread.start()

for i in range(1, 21):
    q.put(i)

q.join()
print('end')
