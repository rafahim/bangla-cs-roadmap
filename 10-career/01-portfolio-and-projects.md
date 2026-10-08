# Portfolio ও বাস্তব প্রকল্প

## এই পাঠ শেষে

- Portfolio ও বাস্তব প্রকল্প সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Portfolio screenshot-এর সংগ্রহ নয়; সমস্যা বোঝা, সিদ্ধান্ত নেওয়া, কাজ শেষ করা ও ফল ব্যাখ্যা করার প্রমাণ। Project README-তে problem, target user, feature, technology, local setup, screenshot, test instruction এবং limitation থাকা উচিত। Demo-তে accessibility ও error state-সহ কাজ করে কি না যাচাই করো। ছোট কিন্তু সম্পূর্ণ প্রকল্প অস্পষ্ট বড় প্রকল্পের চেয়ে শক্তিশালী প্রমাণ হতে পারে।

তুমি বোঝো এমন সমস্যা বেছে নাও—expense tracker, course catalog বা Bangla text tool। প্রথমে minimum useful scope নির্ধারণ করো, তারপর validation, responsive layout, error handling ও deployment যোগ করো। অন্যের কাজ ব্যবহার করলে license মানো। API key, personal user data বা অনুমতিহীন client content প্রকাশ কোরো না।

## বাস্তব জীবনের উপমা

Case study-তে শুধু result নয়; problem, process, trade-off ও শেখা বিষয় দেখানো হয়। Portfolio review-তে মানুষ তোমার decision-making দেখতে চায়।

## মূল বিষয়

- Problem statement ও target user স্পষ্ট করো।
- README project পুনরুৎপাদনযোগ্য করে।
- Success, empty, loading ও error state পরীক্ষা করো।

## Code example

```markdown
# Expense Tracker

## Problem
দৈনিক খরচ category অনুযায়ী দেখা কঠিন।

## Features
- খরচ যোগ, edit ও delete
- মাসভিত্তিক total
- Local data storage

## Run
1. Repository clone করো।
2. `index.html` browser-এ খোলো।
3. Sample expense দিয়ে যাচাই করো।

## Limitations
এই demo বহু-device sync দেয় না।
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- README-তে কী problem solve করে তা না বলা।
- শুধু happy path দেখানো।
- অনুমতি ছাড়া private code/data/asset প্রকাশ করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Project README-তে অন্তত পাঁচটি অংশ কী?

**সমাধান:** Problem, feature, technology, setup/run, demo/screenshot, tests/limitations—এগুলোর অন্তত পাঁচটি।

### সমস্যা 2
Scope ছোট করে শেষ করা কেন উপকারী?

**সমাধান:** Test ও deploy করা যায় এবং completion-এর প্রমাণ থাকে।

### সমস্যা 3
Screenshot দেওয়ার আগে কী যাচাই করবে?

**সমাধান:** Responsive layout, readable text, current version ও sensitive data না থাকা।

## আরও পড়ো

- [https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [https://roadmap.sh/roadmaps](https://roadmap.sh/roadmaps)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
