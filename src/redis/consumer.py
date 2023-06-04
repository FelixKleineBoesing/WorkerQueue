import redis
import time
import sys
import multiprocessing as mp


def consumer(j: int):
    r = redis.Redis()
    while True:
        val = r.lpop('queue')
        print(f"Worker: {j}, val: {val}")
        if val is None:
            time.sleep(2)
            print("Sleeping..., no takss")


if __name__ == "__main__":
    p1 = mp.Process(target=consumer, args=(1, ))
    p2 = mp.Process(target=consumer, args=(2, ))
    p2.start()
    p1.start()



