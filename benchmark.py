import time
import random

from lru_cache import LRUCache


def benchmark(capacity, operations):

    cache = LRUCache(capacity)

    keys = list(range(operations))

    start = time.time()

    for i in range(operations):

        key = random.choice(keys)

        if random.random() < 0.5:
            cache.put(key, i)
        else:
            cache.get(key)

    end = time.time()

    return end - start


def main():

    print("LRU Cache Benchmark\n")

    ops = 100_000

    capacities = [100, 1000, 5000]

    for cap in capacities:

        t = benchmark(cap, ops)

        print(
            f"Capacity={cap:<5} | "
            f"Ops={ops:<7} | "
            f"Time={t:.4f}s"
        )


if __name__ == "__main__":
    main()
