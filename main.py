import argparse

from lru_cache import LRUCache


def main():

    parser = argparse.ArgumentParser(
        description="LRU Cache Demo"
    )

    parser.add_argument(
        "--capacity",
        type=int,
        default=3,
        help="Cache capacity (default: 3)"
    )

    args = parser.parse_args()

    cache = LRUCache(args.capacity)

    print(f"\nLRU Cache Demo (Capacity = {args.capacity})\n")

    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(3, 30)

    print("Cache:", cache.display())

    print("Get 1 ->", cache.get(1))
    print("Cache:", cache.display())

    cache.put(4, 40)

    print("\nAfter adding key 4 (evicts LRU)")
    print("Cache:", cache.display())

    print("Get 2 ->", cache.get(2))


if __name__ == "__main__":
    main()
