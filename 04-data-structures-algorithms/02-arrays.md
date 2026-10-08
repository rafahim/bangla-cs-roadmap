# Arrays ও index

## এই পাঠ শেষে

- Arrays ও index সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Array ধারাবাহিক slot-এ ordered item রাখে; index দিয়ে নির্দিষ্ট item পড়া যায়। Python list dynamic array-এর মতো আচরণ করে, যদিও ভাষার implementation এক নয়। Index সাধারণত ০ থেকে শুরু হয়, তাই length `n` হলে বৈধ index `0` থেকে `n-1`; ভুল index out-of-range error দিতে পারে।

Index access সাধারণত `O(1)`, কিন্তু মাঝখানে insert/delete করলে পরের item সরাতে হয় বলে `O(n)` হতে পারে। পুরো list traverse করা `O(n)`। Position access ও iteration বেশি দরকার হলে array সুবিধাজনক; insert/delete pattern ঘনঘন হলে অন্য structure বিবেচনা করো।

## বাস্তব জীবনের উপমা

সারি করে রাখা সিনেমার আসনের মতো: seat number জানা থাকলে সরাসরি সেখানে যাওয়া যায়, মাঝখানে নতুন seat ঢোকাতে হলে অন্যদের সরাতে হয়।

## মূল বিষয়

- Index zero-based হতে পারে।
- Length ও last index এক নয়।
- Middle insertion array/list-এ ব্যয়বহুল হতে পারে।

## Code example

```python
scores = [72, 88, 91, 67]
print(scores[0])
print(scores[-1])
scores.append(95)
scores[1] = 90
print(scores)
print(sum(scores) / len(scores))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- `items[len(items)]`-কে শেষ index ধরা।
- খালি list-এ first item access করা।
- Loop চলাকালে list বদলে item skip করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
`[10, 20, 30]`-এর index ১-এর মান কী?

**সমাধান:** ২০।

### সমস্যা 2
Python list-এর শেষ item কীভাবে পাবে?

**সমাধান:** খালি নয় নিশ্চিত হলে `items[-1]`।

### সমস্যা 3
List-এ positive number-এর সংখ্যা কীভাবে গুনবে?

**সমাধান:** `sum(1 for x in values if x > 0)`।

## আরও পড়ো

- [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
