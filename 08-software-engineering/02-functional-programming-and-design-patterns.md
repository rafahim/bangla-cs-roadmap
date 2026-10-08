# Functional Programming ও Design Patterns

## এই পাঠ শেষে

- Functional Programming ও Design Patterns সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Functional programming pure function, immutable data, composition এবং side effect সীমিত রাখায় জোর দেয়। Pure function একই input-এ একই output দেয় এবং বাইরের state বদলায় না; তাই test ও reasoning সহজ হয়। `map`, `filter` ও `reduce` collection transform করতে পারে। লক্ষ্য mutation নিষিদ্ধ করা নয়, বরং state পরিবর্তন কোথায় হয় তা স্পষ্ট করা।

Design pattern বারবার দেখা software design problem-এর পরিচিত সমাধানের কাঠামো, copy-paste code নয়। Strategy interchangeable behavior, Observer event-এ subscriber notification, Factory object creation আলাদা করতে পারে। Problem না বুঝে pattern বসালে abstraction বাড়ে; আগে সহজ সমাধান চেষ্টা করো, পরে প্রয়োজন থাকলে pattern নাও।

## বাস্তব জীবনের উপমা

একই উপকরণে একই ফল দেয় এমন recipe pure function-এর মতো। Design pattern হলো কাজের নকশা—সমস্যা মিলে গেলে ব্যবহার করো, জোর করে নয়।

## মূল বিষয়

- Pure function external visible side effect করে না।
- Immutable style shared-state bug কমাতে পারে।
- Pattern-এর মূল্য problem-fit-এ, নাম ব্যবহারে নয়।

## Code example

```python
prices = [100, 250, 80]
with_tax = list(map(lambda price: round(price * 1.05, 2), prices))
expensive = list(filter(lambda price: price >= 100, prices))
print(with_tax)
print(expensive)
class PercentageDiscount:
    def __init__(self, percent):
        self.percent = percent
    def apply(self, total):
        return total * (1 - self.percent / 100)
def checkout(total, strategy):
    return strategy.apply(total)
print(checkout(500, PercentageDiscount(10)))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Pure function-এর নামে global state/file I/O লুকানো।
- প্রতিটি conditional-কে জটিল pattern দিয়ে বদলানো।
- Problem-fit না দেখে pattern প্রয়োগ করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Pure function-এর একটি গুণ লেখো।

**সমাধান:** একই input-এ একই output দেয় এবং বাইরে দৃশ্যমান state বদলায় না।

### সমস্যা 2
৫০০ টাকায় ১০% discount-এর ফল কত?

**সমাধান:** ৪৫০।

### সমস্যা 3
বিভিন্ন payment method পাল্টে ব্যবহার করতে কোন pattern উপকারী?

**সমাধান:** Common interface-সহ Strategy pattern।

## আরও পড়ো

- [https://docs.python.org/3/howto/functional.html](https://docs.python.org/3/howto/functional.html)
- [https://refactoring.guru/design-patterns/catalog](https://refactoring.guru/design-patterns/catalog)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
