# CV, Interview ও শেখার পরিকল্পনা

## এই পাঠ শেষে

- CV, Interview ও শেখার পরিকল্পনা সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Technical CV-তে প্রাসঙ্গিক skill ও প্রমাণকে অগ্রাধিকার দাও। শুধু tool name নয়, কী বানিয়েছ, তোমার দায়িত্ব, trade-off এবং ফল কী—তা সংক্ষেপে লেখো। Experience কম হলে project, internship, open-source contribution ও coursework দেখানো যায়। যা জানো না তা বাড়িয়ে না বলে শেখার সীমা সৎভাবে ব্যাখ্যা করো।

Interview-এ problem পরিষ্কার করো, constraint জিজ্ঞেস করো, baseline solution দাও, তারপর complexity ব্যাখ্যা করো। Edge case পরীক্ষা, readable naming ও dry run-এ reasoning দেখাও। Behavioral প্রশ্নে situation, responsibility, action ও result কাঠামো ব্যবহার করা যায়। Interview শেষে দুর্বল topic লিখে পরের practice plan বানাও; শুধু puzzle মুখস্থ নয়, explanation ও debugging-ও অনুশীলন করো।

## বাস্তব জীবনের উপমা

CV হলো দাবির তালিকা, আর project code ও demo হলো সেই দাবির প্রমাণ।

## মূল বিষয়

- CV role অনুযায়ী customize করো।
- Interview-এ clarify, plan, implement, test, complexity দেখাও।
- Skill gap measurable practice task-এ ভাগ করো।

## Code example

```python
def binary_search(values, target):
    low, high = 0, len(values) - 1
    while low <= high:
        middle = (low + high) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1

values = [2, 5, 8, 12, 16]
print(binary_search(values, 12))
print(binary_search(values, 7))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- CV-তে প্রমাণহীন skill rating বা অতিরঞ্জিত experience লেখা।
- Problem বোঝার আগেই code শুরু করা।
- এক interview-কে সামগ্রিক skill-এর চূড়ান্ত মাপ ভাবা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Project bullet-কে শক্তিশালী করার নিয়ম লেখো।

**সমাধান:** Action + technology/context + ফল/impact লিখো।

### সমস্যা 2
Coding problem সমাধানের পর কী করবে?

**সমাধান:** Dry run, boundary/invalid test এবং time/space complexity ব্যাখ্যা করবে।

### সমস্যা 3
প্রতিদিন ৩০ মিনিট practice কীভাবে ভাগ করবে?

**সমাধান:** ১০ মিনিট concept, ১৫ মিনিট problem solving, ৫ মিনিট ভুল ও learning note।

## আরও পড়ো

- [https://www.techinterviewhandbook.org/](https://www.techinterviewhandbook.org/)
- [https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
