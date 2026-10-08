# Data Types: ডেটার ধরন

## এই পাঠ শেষে

- Data Types: ডেটার ধরন সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Data type বলে value কী ধরনের এবং তার ওপর কোন operation অর্থপূর্ণ। Python-এ `int` integer, `float` approximate decimal, `str` text, `bool` true/false, আর `list` একাধিক item ধরে। JavaScript-এর type system আলাদা। Text-এর সঙ্গে number মিশিয়ে arithmetic করতে গেলে language অনুযায়ী ফল অপ্রত্যাশিত হতে পারে।

Type conversion এক type-কে অন্য type-এ বদলায়। User input প্রায়ই text হয়, তাই arithmetic-এর আগে validation ও conversion দরকার। `int('abc')` exception তুলবে। বাস্তব app-এ type ছাড়াও blank value, format, range ও domain-specific rule যাচাই করতে হয়।

## বাস্তব জীবনের উপমা

ডাকঘরের প্যাকেট: চিঠি, ভঙ্গুর জিনিস ও তরল আলাদা নিয়মে সামলাতে হয়। Data type-ও কোন কাজ করা যাবে তা জানায়।

## মূল বিষয়

- Type value-এর operation ও representation নির্ধারণ করে।
- `type(value)` Python-এ type দেখায়।
- Validation ও conversion আলাদা ধাপ।

## Code example

```python
age_text = input("বয়স লিখো: ")
if age_text.isdigit():
    age = int(age_text)
    print(age + 1)
else:
    print("বয়স পূর্ণসংখ্যা হতে হবে")
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- User input যাচাই ছাড়া number ধরে নেওয়া।
- Zero ও empty string-এর truthiness গুলিয়ে ফেলা।
- Floating-point সব decimal একদম নিখুঁত রাখবে ধরে নেওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
`'42'` ও `42`-এর পার্থক্য কী?

**সমাধান:** প্রথমটি string, দ্বিতীয়টি integer; তাই arithmetic behavior আলাদা।

### সমস্যা 2
৩৬.৬ তাপমাত্রা রাখার সাধারণ type কী?

**সমাধান:** সাধারণ হিসাবের জন্য float; precise finance-এর জন্য decimal type বিবেচনা করো।

### সমস্যা 3
User বয়সে `abc` দিলে কী করবে?

**সমাধান:** Input reject বা পুনরায় চাইবে; পরিষ্কার error message দেবে।

## আরও পড়ো

- [https://docs.python.org/3/library/stdtypes.html](https://docs.python.org/3/library/stdtypes.html)
- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
