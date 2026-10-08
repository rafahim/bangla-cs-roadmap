# Variables: ডেটার নামযুক্ত ঘর

## এই পাঠ শেষে

- Variables: ডেটার নামযুক্ত ঘর সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Variable মানকে একটি নামে ব্যবহার করতে দেয়। একই সংখ্যা বারবার না লিখে `unit_price` নামে রাখলে হিসাব পড়া সহজ হয় এবং মান এক জায়গায় বদলালেই পরের হিসাবেও তা কাজে লাগে। Python-এ assignment `=` নামের সঙ্গে value বাঁধে; এটি equality comparison নয়। অন্য ভাষায় variable declare করার সময় type বা scope স্পষ্ট করতে হতে পারে।

নামের উদ্দেশ্য বোঝা জরুরি। `total_price` অনেক ক্ষেত্রে `x`-এর চেয়ে স্পষ্ট। Scope বলে নামটি কোথায় ব্যবহারযোগ্য; local variable একটি function-এর ভেতরের কাজের জন্য, আর global state অতিরিক্তভাবে ভাগ করলে testing ও debugging জটিল হতে পারে। Reserved keyword variable name হিসেবে নেওয়া যায় না।

## বাস্তব জীবনের উপমা

রান্নার খাতায় উপকরণের পাত্রে label লাগানো: ‘চিনি’ লেখা পাত্র থেকে বারবার চিনি নেওয়া যায়; প্রতিবার উপকরণটি কী তা বুঝিয়ে দিতে হয় না।

## মূল বিষয়

- Assignment variable-এ value বাঁধে।
- Variable-এর মান পুনরায় পরিবর্তন হতে পারে।
- Scope নামের visibility সীমা নির্ধারণ করে।

## Code example

```python
product_name = "খাতা"
unit_price = 45
quantity = 4
total_price = unit_price * quantity
print(product_name, total_price)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- `=`-কে comparison ধরে নেওয়া; তুলনায় `==` লাগে।
- অস্পষ্ট এক-অক্ষরের নাম অতিরিক্ত ব্যবহার করা।
- সব function-কে global state দিয়ে চালানো।

## অনুশীলন ও সমাধান

### সমস্যা 1
৮০ টাকা দাম ও ৩টি পণ্যের total বের করো।

**সমাধান:** `price = 80`, `quantity = 3`, `total = price * quantity`; ফল ২৪০।

### সমস্যা 2
`user-name` Python variable name হতে পারে না কেন?

**সমাধান:** Hyphen subtraction operator, তাই `user_name` ব্যবহার করো।

### সমস্যা 3
`monthly_rent` নাম `a`-এর চেয়ে ভালো কেন?

**সমাধান:** নাম থেকেই value-র উদ্দেশ্য বোঝা যায় এবং maintenance সহজ হয়।

## আরও পড়ো

- [https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [https://developer.mozilla.org/en-US/docs/Glossary/Variable](https://developer.mozilla.org/en-US/docs/Glossary/Variable)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
