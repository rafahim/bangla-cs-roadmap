# অপারেটিং সিস্টেম ও কমান্ড লাইন

## এই পাঠ শেষে

- অপারেটিং সিস্টেম ও কমান্ড লাইন সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Operating system (OS) application ও hardware-এর মধ্যে সমন্বয় করে। এটি process চালায়, memory বরাদ্দ করে, filesystem পরিচালনা করে, device-এর সঙ্গে যোগাযোগ ও permission control করে। Windows, Linux, macOS ও Android OS-এর উদাহরণ। Application সাধারণত OS API ব্যবহার করে কাজ চায়; hardware-এর সব detail নিজে পরিচালনা করে না।

Command-line interface-এ লিখিত command দিয়ে কাজ হয়। `pwd` বর্তমান directory জানায়, `ls` file দেখায়, `cd` directory বদলায়, `mkdir` folder তৈরি করে। Shell command ব্যাখ্যা করে চালায়। CLI-তে কাজ দ্রুত হয়, কিন্তু ভুল path বা destructive command ক্ষতি করতে পারে; command চালানোর আগে target যাচাই করো।

## বাস্তব জীবনের উপমা

OS ভবনের রিসেপশনের মতো: কে কোন ঘরে যাবে, কোন যন্ত্র ব্যবহার করবে ও কার অনুমতি আছে তা সমন্বয় করে। CLI হলো ব্যবস্থাপককে সরাসরি নির্দেশ দেওয়ার কাউন্টার।

## মূল বিষয়

- Kernel process, memory ও hardware-এর মৌলিক কাজ পরিচালনা করে।
- Shell command ব্যাখ্যা করে।
- Absolute path সম্পূর্ণ অবস্থান জানায়; relative path বর্তমান directory-র তুলনায়।

## Code example

```bash
pwd
ls
mkdir practice-folder
cd practice-folder
printf 'Hello, terminal!\n' > hello.txt
cat hello.txt
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- বর্তমান directory না দেখে file তৈরি বা delete করা।
- সব OS-এ একই command আছে ধরে নেওয়া।
- অজানা destructive command কপি করে চালানো।

## অনুশীলন ও সমাধান

### সমস্যা 1
`pwd` কী জানায়?

**সমাধান:** বর্তমান working directory-র path।

### সমস্যা 2
Delete command সাবধানে চালাতে হয় কেন?

**সমাধান:** ভুল target-এ চালালে গুরুত্বপূর্ণ file স্থায়ীভাবে মুছে যেতে পারে।

### সমস্যা 3
একটি folder তৈরি করে ঢোকার command লেখো।

**সমাধান:** `mkdir notes` তারপর `cd notes`।

## আরও পড়ো

- [https://ubuntu.com/tutorials/command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
- [https://learn.microsoft.com/en-us/windows/terminal/](https://learn.microsoft.com/en-us/windows/terminal/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
