# Control Flow: শর্ত ও লুপ

## এই পাঠ শেষে

- Control Flow: শর্ত ও লুপ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Control flow বলে program-এর কোন অংশ কখন চলবে। `if/elif/else` condition অনুযায়ী পথ নেয়; `for` iterable-এর item নিয়ে কাজ করে; `while` condition true থাকা পর্যন্ত চলে। বাস্তব সমস্যায় শর্তের order, unreachable branch এবং loop বন্ধ হওয়ার নিশ্চয়তা যাচাই করতে হয়।

Counter বা sequence ঠিকমতো অগ্রসর না হলে infinite loop বা item skip হওয়ার সমস্যা হয়। ০, ১ ও maximum value-এর মতো boundary test কার্যকর। `break` loop থেকে বের হয়, `continue` পরের iteration-এ যায়; এগুলো অতিরিক্ত ব্যবহার করলে flow বোঝা কঠিন হতে পারে।

## বাস্তব জীবনের উপমা

Traffic signal: সবুজ হলে এগোও, লাল হলে থামো—condition। একে একে গাড়ি পার হওয়া loop; কখন থামবে তার নিয়ম দরকার।

## মূল বিষয়

- Condition boolean ফল দেয়।
- `for` iterable ঘোরে; `range()` sequence তৈরি করে।
- `while` condition বা state update ভুল হলে infinite হতে পারে।

## Code example

```python
score = 76
if score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
else:
    grade = "আরও অনুশীলন"
print(grade)
for number in range(1, 6):
    print(number)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Broad condition আগে দিয়ে specific branch unreachable করা।
- `while` loop-এ state update ভুলে যাওয়া।
- `range(1, 5)`-এ ৫ অন্তর্ভুক্ত ধরে নেওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
১ থেকে ১০ পর্যন্ত জোড় সংখ্যা দেখাও।

**সমাধান:** `for n in range(2, 11, 2): print(n)`।

### সমস্যা 2
Score ০–১০০-এর বাইরে হলে কী করো?

**সমাধান:** Range validation করে input reject বা পুনরায় চাও।

### সমস্যা 3
`while count < 3` থামাতে কী প্রয়োজন?

**সমাধান:** Loop-এর মধ্যে count এমনভাবে বাড়াও যাতে শেষে condition false হয়।

## আরও পড়ো

- [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
