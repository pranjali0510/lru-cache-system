# LRU Cache System 🔁

A production-style implementation of Least Recently Used (LRU) Cache in Python using HashMap and Doubly Linked List.

The system supports constant-time operations, concurrency safety, benchmarking and automated testing.

---

## 🚀 Features

- O(1) get and put operations
- Automatic eviction of least recently used items
- Doubly linked list for usage tracking
- Hash map for fast lookup
- Thread-safe implementation
- Configurable cache capacity
- Unit testing and benchmarking support

---

## 🛠️ Tech Stack

- Python 3
- Data Structures (HashMap, Doubly Linked List)
- Threading (Locks)
- unittest

---

## 📦 Requirements

- Python 3.9+

Check version:

```bash
python --version
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone <repo-link>
cd lru-cache-system
```

Run demo:

```bash
python main.py --capacity 5
```

Run tests:

```bash
python test_lru.py
```

Run benchmark:

```bash
python benchmark.py
```

---

## 📌 Time Complexity

| Operation | Complexity |
|-----------|------------|
| get       | O(1)       |
| put       | O(1)       |
| eviction  | O(1)       |

---

## 📁 Project Structure

```
lru-cache-system/
│
├── lru_cache.py
├── node.py
├── main.py
├── test_lru.py
├── benchmark.py
└── README.md
```

---

## 👩‍💻 Author

Pranjali Sharma
