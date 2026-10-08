# ফাইল, প্রসেস ও পেরিফেরাল

## এই পাঠ শেষে

- ফাইল, প্রসেস ও পেরিফেরাল সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Filesystem file ও directory-তে data সংগঠিত করে। Name ও extension সহায়ক হলেও extension সবসময় প্রকৃত file format প্রমাণ করে না। Metadata-তে size, timestamp ও permissions থাকতে পারে। Relative path বর্তমান directory-র তুলনায় অবস্থান জানায়; absolute path পূর্ণ অবস্থান দেয়। একই নামে file ভিন্ন directory-তে থাকতে পারে।

Process হলো চলমান program-এর instance; এর নিজস্ব address space ও resource থাকে। Thread process-এর ভেতরের execution stream, আর একই process-এর thread memory ভাগ করতে পারে। Printer, webcam, keyboard ও USB drive-এর মতো peripheral OS driver-এর সাহায্যে কাজ করে। App crash করলে process থামতে পারে, আর OS সাধারণত তার resource reclaim করে।

## বাস্তব জীবনের উপমা

লাইব্রেরির তাক directory, বই file আর বই পড়তে থাকা পাঠক process। বই খুঁজতে shelf location দরকার; এক reader একই সময়ে একাধিক helper task-ও চালাতে পারে।

## মূল বিষয়

- Directory file সংগঠিত করে।
- Process চলমান program ও resource-এর পরিবেশ।
- Thread একই process-এর ভেতরে execution চালায়।
- Driver OS-কে hardware-এর সঙ্গে কথা বলতে সাহায্য করে।

## Code example

```python
from pathlib import Path
folder = Path("sample-data")
folder.mkdir(exist_ok=True)
file_path = folder / "notes.txt"
file_path.write_text("প্রথম নোট", encoding="utf-8")
print(file_path.read_text(encoding="utf-8"))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- শুধু extension দেখে file content নিশ্চিত ধরে নেওয়া।
- Process ও thread-কে একই ধারণা ভাবা।
- একই shared file-এ concurrent write হলে conflict হতে পারে তা উপেক্ষা করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Relative path ও absolute path-এর পার্থক্য কী?

**সমাধান:** Relative path বর্তমান directory-র ভিত্তিতে; absolute path সম্পূর্ণ path।

### সমস্যা 2
App-এর একাধিক thread কেন থাকতে পারে?

**সমাধান:** UI responsive রাখা এবং network/data processing-এর মতো কাজ overlap করাতে।

### সমস্যা 3
USB keyboard app-এ input পাঠায় কীভাবে?

**সমাধান:** Device signal OS ও driver-এর মাধ্যমে event হিসেবে application-এ পৌঁছায়।

## আরও পড়ো

- [https://docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)
- [https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads](https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
