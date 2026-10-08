# Hash Tables ও Dictionary

## এই পাঠ শেষে

- Hash Tables ও Dictionary সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Hash table key-কে hash function দিয়ে bucket বা slot-এর সঙ্গে যুক্ত করে। ফলে dictionary/map-এ lookup, insert ও delete গড়ে প্রায় `O(1)` হতে পারে, কিন্তু এটি worst-case guarantee নয়। Collision হলে একাধিক key একই জায়গায় পড়ে; chaining বা open addressing-এর মতো পদ্ধতিতে তা সামলানো হয়। Hash function key-গুলোকে যতটা সম্ভব সমানভাবে ছড়াতে সাহায্য করে।

Python dict-এ hashable key দরকার এবং equality/hash-এর নিয়ম মিলতে হয়। Hash table password encryption নয়। Password storage-এর জন্য salt-সহ Argon2 বা bcrypt-এর মতো password-specific slow hashing algorithm ব্যবহার করা হয়; সাধারণ fast hash যথেষ্ট নয়।

## বাস্তব জীবনের উপমা

Library catalog number দিয়ে বই খুঁজে পাওয়ার মতো; key-র সাহায্যে দ্রুত value খোঁজা যায়, তবে একই slot-এ collision হলে তা সামলাতে হয়।

## মূল বিষয়

- Hash function key থেকে slot/bucket নির্ধারণ করে।
- Collision স্বাভাবিক এবং handle করতে হয়।
- Dictionary-তে key unique; নতুন value দিলে আগের value replace হয়।

## Code example

```python
prices = {"কলম": 12, "খাতা": 45, "স্কেল": 20}
prices["পেন্সিল"] = 8
print(prices["খাতা"])
print("রাবার" in prices)
for item, price in prices.items():
    print(item, price)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Hash table সব অবস্থায় `O(1)` ধরে নেওয়া।
- Mutable object-কে key করতে চাওয়া।
- Password storage-এ general fast hash ব্যবহার করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
`prices['খাতা']` কী?

**সমাধান:** ৪৫।

### সমস্যা 2
একই key-তে নতুন value রাখলে কী হয়?

**সমাধান:** ঐ key-এর পুরোনো value replace হয়।

### সমস্যা 3
Hash collision কী?

**সমাধান:** দুটি আলাদা key একই bucket বা position-এ map হতে পারে।

## আরও পড়ো

- [https://docs.python.org/3/library/stdtypes.html#mapping-types-dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [https://docs.python.org/3/reference/datamodel.html#object.__hash__](https://docs.python.org/3/reference/datamodel.html#object.__hash__)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
