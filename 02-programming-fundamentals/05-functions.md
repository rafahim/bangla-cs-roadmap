# Functions: পুনর্ব্যবহারযোগ্য কাজ

## এই পাঠ শেষে

- Functions: পুনর্ব্যবহারযোগ্য কাজ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Function একটি নামযুক্ত কাজের একক, যা input নিতে, হিসাব করতে এবং ফল ফেরত দিতে পারে। একই যুক্তি কয়েক জায়গায় দরকার হলে function-এ রাখলে duplicate code কমে। Parameter হলো definition-এ input-এর নাম, argument হলো call-এর সময় দেওয়া value। `return` caller-কে value দেয়; `print()` কেবল output দেখায়।

ভালো function-এর দায়িত্ব স্পষ্ট, input/output বোঝা যায় এবং side effect সীমিত থাকে। Local variable function-এর ভেতরে থাকে। Python-এ mutable default argument ভুলভাবে ব্যবহার করলে এক call-এর state পরের call-এ থেকে যেতে পারে; list বা dict parameter-এর default নতুন করে তৈরি করার প্রয়োজন হলে `None` ব্যবহার করা নিরাপদ কৌশল।

## বাস্তব জীবনের উপমা

কফি মেশিনের বোতামের মতো: size ও sugar বেছে দিলে মেশিন ধাপ চালিয়ে পানীয় দেয়। Argument পছন্দ, function body কাজ, return ফল।

## মূল বিষয়

- Function definition ও call আলাদা ধাপ।
- Parameter ও argument আলাদা ধারণা।
- Return value অন্য expression-এ ব্যবহার করা যায়।

## Code example

```python
def calculate_total(price, quantity, discount=0):
    subtotal = price * quantity
    return subtotal - subtotal * discount / 100

print(calculate_total(200, 3, 10))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Value return না করে কেবল print করা।
- এক function-এ অনেক অপ্রাসঙ্গিক দায়িত্ব রাখা।
- অজান্তে global state বদলানো।

## অনুশীলন ও সমাধান

### সমস্যা 1
দুটি সংখ্যার বড়টি return করে এমন function লেখো।

**সমাধান:** `def larger(a, b): return a if a > b else b`।

### সমস্যা 2
`return` ও `print` কীভাবে আলাদা?

**সমাধান:** `return` caller-কে value দেয়; `print` output দেখায়।

### সমস্যা 3
`calculate_total(50, 4)` কত, discount না দিলে?

**সমাধান:** ফল ২০০।

## আরও পড়ো

- [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
