# Graphs: node, edge ও পথ

## এই পাঠ শেষে

- Graphs: node, edge ও পথ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Graph node/vertex ও edge দিয়ে সম্পর্ক মডেল করে। Directed edge A থেকে B-তে একমুখী হতে পারে; undirected edge দুইমুখী সম্পর্ক বোঝায়। Weighted graph-এ edge-এর সঙ্গে distance, cost বা time থাকে। Map, social network, dependency ও web link graph-এর ব্যবহার।

Adjacency list প্রতিটি node-এর neighbor রাখে এবং sparse graph-এ memory-efficient হতে পারে। Adjacency matrix edge lookup দ্রুত করলেও `O(V²)` space নিতে পারে। BFS queue দিয়ে layer ধরে এগোয় এবং unweighted graph-এ shortest path খুঁজতে পারে; DFS stack বা recursion দিয়ে গভীরে যায়। Cycle সামলাতে visited set দরকার।

## বাস্তব জীবনের উপমা

শহরের মানচিত্রে মোড় node, রাস্তা edge, আর দূরত্ব edge weight হতে পারে। Graph algorithm সম্ভাব্য পথ তুলনা করে।

## মূল বিষয়

- Vertex ও edge সম্পর্ক মডেল করে।
- Adjacency list ও matrix-এর trade-off আলাদা।
- BFS queue ব্যবহার করে; DFS depth-এ যায়।

## Code example

```python
from collections import deque
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
def bfs(start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order
print(bfs("A"))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Visited set বাদ দিয়ে cyclic graph-এ বারবার ঘোরা।
- Directed edge-কে ভুল করে দুই দিকের ধরে নেওয়া।
- Weighted graph-এ সবসময় BFS-কে minimum-cost path solver ভাবা।

## অনুশীলন ও সমাধান

### সমস্যা 1
A→B ও B→C থাকলে A থেকে C-তে পথ আছে?

**সমাধান:** হ্যাঁ, A→B→C।

### সমস্যা 2
BFS কোন structure ব্যবহার করে?

**সমাধান:** Queue।

### সমস্যা 3
Non-negative unequal weights-এ shortest path-এর জন্য কী দেখবে?

**সমাধান:** Dijkstra algorithm; negative edge হলে Bellman–Ford-এর মতো বিকল্প বিবেচনা করো।

## আরও পড়ো

- [https://networkx.org/documentation/stable/tutorial.html](https://networkx.org/documentation/stable/tutorial.html)
- [https://visualgo.net/en/dfsbfs](https://visualgo.net/en/dfsbfs)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
