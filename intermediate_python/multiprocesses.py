from multiprocessing import Pool, Process, Value, Array, Lock
from threading import Thread
from multiprocessing import Queue
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


processes = []
num_processes = os.cpu_count()
num_threads = 10
threads = []


# create threads
# for i in range(num_threads):
#     t = Thread(target=square_numbers)
#     threads.append(t)
#
# for t in threads:
#     t.start()
#
# for t in threads:
#     t.join()


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def add(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)


def cube(number):
    return number * number * number


if __name__ == '__main__':
    # create processes
    # for i in range(num_processes):
    #     p = Process(target=square_numbers)
    #     processes.append(p)
    #
    # # start
    # for p in processes:
    #     p.start()
    #
    # # join processes
    # for p in processes:
    #     p.join()

    shared_number = Value('i', 0)  # i represent int
    shared_array = Array('d', [0.0, 100.0, 200.0])  # i represent double
    lock = Lock()
    # print('Number at the beginning is', shared_number.value)
    print('Array at the beginning is', shared_array[:])

    p1 = Process(target=add, args=(shared_array, lock))
    p2 = Process(target=add, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # print('Number at the end is', shared_number.value)
    print('Array at the end is', shared_array[:])

    numbers = range(1, 6)
    q = Queue()
    p3 = Process(target=square, args=(numbers, q))
    p4 = Process(target=make_negative, args=(numbers, q))

    p3.start()
    p4.start()

    p3.join()
    p4.join()

    while not q.empty():
        print(q.get())

    numbers = range(10)
    pool = Pool()
    # map, apply,join ,close
    result = pool.map(cube, numbers)

    print(result)

    pool.close()
    pool.join()

print('end main')
