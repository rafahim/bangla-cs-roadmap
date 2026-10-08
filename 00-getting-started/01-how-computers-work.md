# কম্পিউটার কীভাবে কাজ করে

## এই পাঠ শেষে

- কম্পিউটার কীভাবে কাজ করে সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

কম্পিউটারকে শুধু মনিটর বা ল্যাপটপ হিসেবে নয়, ইনপুট থেকে আউটপুট তৈরি করা সমন্বিত ব্যবস্থা হিসেবে বোঝো। কিবোর্ডে অক্ষর চাপলে input device সংকেত পাঠায়; operating system সেটি নেয়; CPU নির্দেশনা চালায়; প্রয়োজন হলে RAM-এ data বদলায়; তারপর graphics system স্ক্রিনে ফল দেখায়। কাজ দ্রুত হওয়ায় ধাপগুলো চোখে পড়ে না, কিন্তু প্রতিটির আলাদা দায়িত্ব আছে।

CPU মানুষের উদ্দেশ্য বোঝে না; machine instruction, memory-র data এবং control flow অনুসরণ করে। Hardware হলো স্পর্শযোগ্য অংশ, আর software হলো যন্ত্রাংশকে কাজ করানোর program ও data। এই পার্থক্য জানলে operating system, programming, networking ও debugging-এর বিষয়গুলো পরস্পরের সঙ্গে যুক্ত করা সহজ হয়।

## বাস্তব জীবনের উপমা

রেস্টুরেন্টে অর্ডারের কথা ভাবো: ক্রেতা input দেয়, অর্ডার রান্নাঘরে পৌঁছায়, রান্নার ধাপ চলে, আর খাবার output হিসেবে আসে। কম্পিউটারেও input, processing ও output আলাদা দায়িত্ব ভাগ করে।

## মূল বিষয়

- Input: keyboard, mouse বা sensor থেকে data আসে।
- Processing: CPU নির্দেশনা চালায়; ALU গণিত ও logic-এর কাজ করে।
- RAM চলমান কাজের অস্থায়ী data রাখে; SSD/HDD ফাইল দীর্ঘমেয়াদে রাখে।
- Output: screen, speaker, printer বা network-এ ফল পৌঁছায়।

## Code example

```python
name = input("তোমার নাম: ")
message = f"স্বাগতম, {name}!"
print(message)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- CPU-কে পুরো কম্পিউটার মনে করা; এটি বড় ব্যবস্থার একটি অংশ।
- RAM ও storage-কে এক জিনিস ভাবা।
- প্রতিটি কাজ শুধু CPU করে ধরে নেওয়া; OS ও I/O device-ও যুক্ত থাকে।

## অনুশীলন ও সমাধান

### সমস্যা 1
একটি ডিজিটাল ঘড়ির input, processing ও output আলাদা করো।

**সমাধান:** Input: সময়ের সংকেত; processing: সময় গণনা ও format; output: screen-এ ঘণ্টা-মিনিট দেখানো।

### সমস্যা 2
ফাইল save করা আর screen-এ লেখা দেখানোর মধ্যে কোনটির জন্য storage দরকার?

**সমাধান:** ফাইল দীর্ঘমেয়াদে রাখতে storage দরকার; সাময়িক display-এর জন্য RAM ও graphics ব্যবস্থা কাজ করে।

### সমস্যা 3
CPU, RAM ও SSD-এর দায়িত্ব এক বাক্যে লেখো।

**সমাধান:** CPU instruction চালায়, RAM চলমান কাজের data রাখে, SSD file স্থায়ীভাবে সংরক্ষণ করে।

## আরও পড়ো

- [https://www.khanacademy.org/computing/computer-science](https://www.khanacademy.org/computing/computer-science)
- [https://computer.howstuffworks.com/pc.htm](https://computer.howstuffworks.com/pc.htm)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
