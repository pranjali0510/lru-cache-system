import unittest

from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_basic_put_get(self):

        cache = LRUCache(2)

        cache.put(1, 10)
        cache.put(2, 20)

        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(2), 20)

    def test_eviction(self):

        cache = LRUCache(2)

        cache.put(1, 10)
        cache.put(2, 20)
        cache.put(3, 30)   # Evicts key 1

        self.assertEqual(cache.get(1), -1)
        self.assertEqual(cache.get(2), 20)
        self.assertEqual(cache.get(3), 30)

    def test_update_existing(self):

        cache = LRUCache(2)

        cache.put(1, 10)
        cache.put(1, 50)

        self.assertEqual(cache.get(1), 50)

    def test_access_updates_order(self):

        cache = LRUCache(2)

        cache.put(1, 10)
        cache.put(2, 20)

        cache.get(1)       # Make 1 most recent
        cache.put(3, 30)   # Evicts 2

        self.assertEqual(cache.get(2), -1)
        self.assertEqual(cache.get(1), 10)
        self.assertEqual(cache.get(3), 30)

    def test_invalid_capacity(self):

        with self.assertRaises(ValueError):
            LRUCache(0)


if __name__ == "__main__":
    unittest.main()
