import redis
import time
import sys


def producer():
    r = redis.Redis()

    i = 0
    while True:
        r.rpush('queue', 'Message %d' % i)
        i += 1
        time.sleep(1)

if __name__ == "__main__":
    producer()
