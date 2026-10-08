# CPU, RAM ও স্টোরেজ

## এই পাঠ শেষে

- CPU, RAM ও স্টোরেজ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

CPU নির্দেশনা fetch, decode ও execute করে। Register খুব দ্রুত ছোট data ধরে, cache বারবার দরকার হয় এমন data CPU-র কাছে রাখে, আর RAM চলমান program ও data-র জন্য বড় অস্থায়ী জায়গা দেয়। RAM কম হলে OS কিছু data storage-এ সরিয়ে নিতে পারে, কিন্তু SSD RAM-এর সমান দ্রুত নয়; তাই একসঙ্গে অনেক বড় app চালালে system ধীর হতে পারে।

SSD ও HDD দীর্ঘমেয়াদি file রাখে। SSD flash memory ব্যবহার করে, HDD ঘূর্ণায়মান magnetic platter ব্যবহার করে। Core count, clock speed ছাড়াও workload, cooling, storage latency ও software-এর দক্ষতা performance-এ প্রভাব ফেলে। একটি specification দেখেই সম্পূর্ণ computer-এর গতি নির্ধারণ করা যায় না।

## বাস্তব জীবনের উপমা

রান্নাঘরের কাউন্টার RAM, স্টোররুম SSD/HDD আর রাঁধুনি CPU। প্রয়োজনীয় উপকরণ কাছে থাকলে কাজ দ্রুত হয়; বারবার স্টোররুমে যেতে হলে সময় লাগে।

## মূল বিষয়

- CPU instruction চালায়।
- Cache দ্রুত কিন্তু ছোট memory।
- RAM volatile; power off হলে সাধারণত data থাকে না।
- SSD/HDD non-volatile storage।

## Code example

```python
tasks = ["browser", "editor", "music player"]
print("চলমান কাজ:", len(tasks))
print("একসঙ্গে খোলা app:", tasks)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- বেশি GHz মানেই সব workload-এ বেশি গতি ধরে নেওয়া।
- RAM-কে permanent backup মনে করা।
- Storage capacity ও RAM capacity-কে একই ধরনের metric ভাবা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Browser বন্ধ করলে RAM-এর কোন বৈশিষ্ট্য বোঝা যায়?

**সমাধান:** RAM চলমান কাজের অস্থায়ী data ধরে; app বন্ধ হলে সেই কাজের প্রয়োজনীয় অংশ মুক্ত হতে পারে।

### সমস্যা 2
কম RAM-এ একসঙ্গে অনেক app চালালে ধীর হয় কেন?

**সমাধান:** System-কে storage থেকে data সরানো-আনা করতে হয়, যা RAM access-এর তুলনায় ধীর।

### সমস্যা 3
দীর্ঘমেয়াদি ছবি সংরক্ষণে RAM না SSD উপযুক্ত?

**সমাধান:** SSD, কারণ power off হলেও এটি file ধরে রাখে।

## আরও পড়ো

- [https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do](https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do)
- [https://www.intel.com/content/www/us/en/gaming/resources/cpu-vs-gpu.html](https://www.intel.com/content/www/us/en/gaming/resources/cpu-vs-gpu.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
