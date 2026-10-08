# Programming কী

## এই পাঠ শেষে

- Programming কী সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Programming হলো কম্পিউটারকে একটি নির্দিষ্ট কাজ করাতে সুনির্দিষ্ট নির্দেশনা লেখা। কাজটি সফল হলেই যথেষ্ট নয়; code বোঝা, পরীক্ষা করা এবং পরিবর্তন করাও সহজ হওয়া দরকার। সমস্যা নির্ধারণ, input/output চিহ্নিত, algorithm সাজানো, code লেখা এবং ফল যাচাই—এই চক্র অধিকাংশ সফটওয়্যার কাজের ভিত্তি।

Programming language মানুষের ভাবনা ও computer instruction-এর মধ্যে সেতু। Python সহজ syntax-এর জন্য শেখার উপযোগী, JavaScript browser-এ চলে, আর C/C++ system ও memory-র ধারণা শেখায়। এক ভাষার syntax মুখস্থ করার চেয়ে সমস্যা বিশ্লেষণ, data নিয়ে যুক্তি এবং test লেখার ক্ষমতা গুরুত্বপূর্ণ; syntax অনুশীলনে আয়ত্ত হয়।

## বাস্তব জীবনের উপমা

রান্নার recipe-র মতো: উপকরণ input, ধাপগুলো algorithm, আর তৈরি খাবার output। নির্দেশনা অস্পষ্ট হলে ফল অনিশ্চিত হয়, code-এও তাই।

## মূল বিষয়

- সমস্যা নির্ধারণ করে প্রত্যাশিত output স্পষ্ট করো।
- Algorithm হলো language-নিরপেক্ষ ধাপে সমাধানের পরিকল্পনা।
- Implementation হলো পরিকল্পনাকে code-এ রূপ দেওয়া।
- স্বাভাবিক, boundary ও invalid input দিয়ে test করো।

## Code example

```python
price = 350
quantity = 3
total = price * quantity
print(total)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- পরিকল্পনা ছাড়াই code লেখা।
- একটি input দিয়েই পরীক্ষা শেষ করা।
- অর্থপূর্ণ variable name না রাখা।

## অনুশীলন ও সমাধান

### সমস্যা 1
দুটি সংখ্যার গড় বের করার algorithm লেখো।

**সমাধান:** দুটি সংখ্যা নাও, যোগ করো, যোগফলকে ২ দিয়ে ভাগ করো, ফল দেখাও।

### সমস্যা 2
দৈনিক খরচের প্রোগ্রামে input, process ও output কী?

**সমাধান:** Input হলো খরচের তালিকা, process হলো যোগ করা, output হলো মোট খরচ।

### সমস্যা 3
একই program একাধিক input-এ পরীক্ষা করতে হয় কেন?

**সমাধান:** শূন্য, ঋণাত্মক, বড় বা অস্বাভাবিক input-এ আচরণ ঠিক আছে কি না জানতে।

## আরও পড়ো

- [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
- [https://www.freecodecamp.org/learn/](https://www.freecodecamp.org/learn/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
