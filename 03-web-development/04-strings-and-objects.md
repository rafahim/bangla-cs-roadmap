# Strings ও Objects

## এই পাঠ শেষে

- Strings ও Objects সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

String হলো text-এর ধারাবাহিকতা; search, slice, replace, split ও join-এর মতো কাজ করা যায়। Unicode-এর কারণে দৃশ্যমান অক্ষর সবসময় এক byte বা এক code unit নয়; emoji ও যুক্তাক্ষরে string length-এর সরল হিসাব বিভ্রান্ত করতে পারে। Input trim বা normalize করার আগে কোন পরিবর্তন দরকার তা বোঝো, যাতে তথ্য অনিচ্ছায় না হারায়।

Object key-value জোড়ায় সম্পর্কিত তথ্য রাখে। JavaScript-এ property dot বা bracket notation দিয়ে পড়া যায়; key variable থেকে এলে bracket notation দরকার হতে পারে। `JSON.stringify` object-কে JSON text করে, আর `JSON.parse` বৈধ JSON থেকে value বানায়। JSON function বা circular object সরাসরি সংরক্ষণ করে না। API data-র structure ও type যাচাই করা উচিত।

## বাস্তব জীবনের উপমা

Student form-এ নাম, course ও active status একই ব্যক্তির সম্পর্কিত field—object; নামের অক্ষরগুলো string।

## মূল বিষয়

- String method নতুন string ফেরাতে পারে।
- Object related field একসঙ্গে রাখে।
- JSON interchange format, JavaScript object-এর পুরো সমার্থক নয়।

## Code example

```javascript
const student = { name: "সামিয়া", course: "Web Development", active: true };
const label = `${student.name} — ${student.course}`;
const trimmed = "  বাংলা কোড  ".trim();
const encoded = JSON.stringify(student);
const decoded = JSON.parse(encoded);
console.log(label);
console.log(trimmed);
console.log(decoded.active);
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- String method মূল variable বদলে দেয় ধরে নেওয়া।
- Parsed JSON-এর field type যাচাই না করা।
- Dynamic key পড়তে bracket notation দরকার তা ভুলে যাওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
`'  Dhaka  '.trim()`-এর ফল কী?

**সমাধান:** `'Dhaka'`।

### সমস্যা 2
`const key = 'course'; student[key]` কী করে?

**সমাধান:** `key`-এর মান দিয়ে `course` property পড়ে।

### সমস্যা 3
JSON-এ JavaScript function রাখা যায়?

**সমাধান:** না, JSON function data হিসেবে সংরক্ষণ করে না।

## আরও পড়ো

- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String)
- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
