# Stacks ও Queues

## এই পাঠ শেষে

- Stacks ও Queues সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Stack হলো Last In, First Out (LIFO): শেষে যোগ করা item আগে বের হয়। `push` item যোগ করে, `pop` top item সরায়, `peek` না সরিয়ে দেখে। Function call stack, undo history ও expression parsing-এ এই ধারণা দেখা যায়। Queue হলো First In, First Out (FIFO): আগে ঢোকা item আগে বের হয়; print job বা ticket line-এর মতো কাজের জন্য উপযোগী।

Stack ও queue abstract data type; তারা operation নির্ধারণ করে, internal storage নয়। Python list-এ stack করা যায়, কিন্তু queue-এর জন্য `collections.deque` ভালো, কারণ list-এর `pop(0)` বাকি item shift করতে পারে। Empty structure থেকে pop করার আগে state যাচাই করো।

## বাস্তব জীবনের উপমা

Stack থালা রাখার স্তূপ—শেষ থালা আগে ওঠে। Queue কাউন্টারের লাইন—আগে আসা মানুষ আগে সেবা পায়।

## মূল বিষয়

- Stack: push/pop/peek এবং LIFO।
- Queue: enqueue/dequeue এবং FIFO।
- Structure বাছাই operation pattern-এর ওপর নির্ভর করে।

## Code example

```python
from collections import deque
stack = []
stack.append("পৃষ্ঠা-১")
stack.append("পৃষ্ঠা-২")
print(stack.pop())
queue = deque(["রহিম", "করিম"])
queue.append("সুমি")
print(queue.popleft())
print(list(queue))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- বড় queue-তে list `pop(0)`-কে efficient মনে করা।
- Empty stack/queue থেকে item নেওয়ার error handling বাদ দেওয়া।
- LIFO ও FIFO গুলিয়ে ফেলা।

## অনুশীলন ও সমাধান

### সমস্যা 1
A তারপর B push করলে প্রথম pop কী?

**সমাধান:** B, কারণ LIFO।

### সমস্যা 2
A তারপর B enqueue করলে প্রথম dequeue কী?

**সমাধান:** A, কারণ FIFO।

### সমস্যা 3
Browser back history-তে stack ধারণা কীভাবে কাজে লাগে?

**সমাধান:** সর্বশেষ navigation-এর আগের state-এ ফিরে যাওয়ার ক্রম stack-এর সঙ্গে মেলে; browser-এর বাস্তব history অবশ্য আরও জটিল।

## আরও পড়ো

- [https://docs.python.org/3/library/collections.html#collections.deque](https://docs.python.org/3/library/collections.html#collections.deque)
- [https://opendsa-server.cs.vt.edu/](https://opendsa-server.cs.vt.edu/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
