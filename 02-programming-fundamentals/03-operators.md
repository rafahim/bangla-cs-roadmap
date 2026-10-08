# Operators: গণনা ও তুলনা

## এই পাঠ শেষে

- Operators: গণনা ও তুলনা সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Operator value-এর ওপর কাজ করে। Arithmetic operator যোগ, বিয়োগ, গুণ, ভাগ ও remainder দেয়; comparison operator সমতা বা বড়-ছোট পরীক্ষা করে; logical operator শর্ত যুক্ত করে। Precedence নির্ধারণ করে expression-এর কোন অংশ আগে মূল্যায়িত হবে—সাধারণত multiplication যোগের আগে হয়। জটিল expression-এ parentheses দিয়ে অভিপ্রায় স্পষ্ট করা ভালো।

Python-এর `and`, `or`, `not` condition-এর যুক্তি প্রকাশ করে। Short-circuit evaluation-এ ফল আগেই জানা গেলে পরের অংশ চলতে নাও পারে। Floating-point-এ `0.1 + 0.2 == 0.3` সত্য হবে ধরে নেওয়া উচিত নয়; tolerance বা decimal arithmetic দরকার হতে পারে।

## বাস্তব জীবনের উপমা

গণিতের সূত্রে bracket বসানোর মতো; কোন কাজ আগে হবে তা বন্ধনী স্পষ্ট করে।

## মূল বিষয়

- Arithmetic: `+`, `-`, `*`, `/`, `%`।
- Comparison: `==`, `!=`, `<`, `<=`, `>`, `>=`।
- Logical: `and`, `or`, `not`।

## Code example

```python
price = 125
discount = 20
final_price = price - (price * discount / 100)
has_coupon = True
free_delivery = final_price >= 100 or has_coupon
print(final_price)
print(free_delivery)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- `=` এবং `==` গুলিয়ে ফেলা।
- Precedence-এ সন্দেহ থাকলেও parentheses না দেওয়া।
- Float equality সরাসরি পরীক্ষা করে rounding issue উপেক্ষা করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
১৭ ভাগ ৫-এর remainder কী?

**সমাধান:** `17 % 5` ফল ২।

### সমস্যা 2
`age >= 18 and has_id` কী যাচাই করে?

**সমাধান:** বয়স ১৮ বা বেশি এবং ID আছে—দুটিই true কি না।

### সমস্যা 3
`2 + 3 * 4` ও `(2 + 3) * 4`-এর ফল কী?

**সমাধান:** প্রথমটির ফল ১৪, দ্বিতীয়টির ২০।

## আরও পড়ো

- [https://docs.python.org/3/reference/expressions.html](https://docs.python.org/3/reference/expressions.html)
- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Expressions_and_operators)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
