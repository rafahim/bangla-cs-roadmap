# Linked Lists

## এই পাঠ শেষে

- Linked Lists সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Linked list-এ প্রতিটি node value এবং পরের node-এর reference রাখে। Singly linked list এক দিকে চলে; doubly linked list previous ও next—দুই reference রাখে। Array-এর মতো node-গুলো memory-তে পাশাপাশি থাকা জরুরি নয়। আগে থেকে node reference জানা থাকলে তার পাশে insertion সহজ, কিন্তু index খুঁজতে শুরু থেকে traverse করতে হয়, তাই access সাধারণত `O(n)`।

Head প্রথম node-কে চিহ্নিত করে, আর শেষ node-এর next সাধারণত `None`/null। ভুল pointer update করলে বাকি list বিচ্ছিন্ন হতে পারে বা cycle তৈরি হতে পারে। বাস্তব ভাষায় built-in list/array অনেক সময় cache locality-র কারণে দ্রুত; linked list বেছে নাও প্রয়োজনীয় operation ও memory overhead বিবেচনা করে।

## বাস্তব জীবনের উপমা

ট্রেনের বগির মতো: প্রতিটি বগি পরেরটির সঙ্গে যুক্ত। নির্দিষ্ট বগিতে যেতে একে একে এগোতে হয়; মাঝখানে বগি জুড়তে link বদলাতে হয়।

## মূল বিষয়

- Node-এ value ও link থাকে।
- Head প্রথম node-কে চিহ্নিত করে।
- Traversal `O(n)`; reference জানা থাকলে local insertion সাধারণত `O(1)`।

## Code example

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

first = Node(10)
second = Node(20)
third = Node(30)
first.next = second
second.next = third
current = first
values = []
while current is not None:
    values.append(current.value)
    current = current.next
print(values)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Next reference সংরক্ষণ না করে বাকি list হারানো।
- শেষ node-এর `next` `None` না রাখা।
- Linked list-এ index access constant time ধরে নেওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
Values ১, ২, ৩-এর traversal output কী?

**সমাধান:** `[1, 2, 3]`।

### সমস্যা 2
Head `None` মানে কী?

**সমাধান:** সাধারণত list খালি।

### সমস্যা 3
৮ম node পেতে কেন `O(n)` লাগতে পারে?

**সমাধান:** Head থেকে একে একে link অনুসরণ করে সেখানে পৌঁছাতে হয়।

## আরও পড়ো

- [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/ListLinked.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/ListLinked.html)
- [https://www.geeksforgeeks.org/data-structures/linked-list/](https://www.geeksforgeeks.org/data-structures/linked-list/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
