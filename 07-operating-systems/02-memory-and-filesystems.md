# Memory Management ও File Systems

## এই পাঠ শেষে

- Memory Management ও File Systems সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Program-এর logical address virtual address space-এ থাকে; OS ও hardware page table দিয়ে virtual address physical memory-তে map করে। Virtual memory isolation ও protection দেয়। Page fault হলে OS-কে memory access-এর জন্য handling করতে হয়; RAM কমে page বারবার storage-এ সরলে thrashing এবং performance drop হতে পারে।

Filesystem file metadata, directory ও storage block সংগঠিত করে। Permission কে read/write/execute করবে তা সীমিত করে। File write হয়েছে দেখালেই সব পরিস্থিতিতে durable হয়েছে ধরে নেওয়া যায় না; cache ও filesystem semantics প্রভাব ফেলে। Backup-এর পাশাপাশি restore test দরকার, কারণ corrupt বা incomplete backup recovery-তে কাজে নাও লাগতে পারে।

## বাস্তব জীবনের উপমা

RAM হলো ডেস্ক আর storage আলমারি। ডেস্কে জায়গা শেষ হলে বারবার আলমারি থেকে কাগজ আনতে হলে কাজ ধীর হয়।

## মূল বিষয়

- Virtual memory address translation ও isolation-এ সাহায্য করে।
- Page fault memory access-এ OS/hardware handling প্রয়োজন বোঝায়।
- Filesystem data ও metadata সাজায়; permission access নিয়ন্ত্রণ করে।

## Code example

```python
from pathlib import Path
path = Path("report.txt")
path.write_text("ফাইল সিস্টেমের অনুশীলন", encoding="utf-8")
print(path.stat().st_size)
print(path.read_text(encoding="utf-8"))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Virtual memory-কে শুধু swap disk মনে করা।
- Backup আছে মানেই restore ঠিক হবে ভাবা।
- সব OS-এ permission behavior এক ধরে নেওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
RAM-এর তুলনায় storage access ধীর হলে কী হয়?

**সমাধান:** Page storage থেকে বারবার আনতে হলে wait বাড়ে ও performance কমে।

### সমস্যা 2
Backup restore test কেন জরুরি?

**সমাধান:** Backup incomplete বা corrupt হলে recovery ব্যর্থ হতে পারে।

### সমস্যা 3
File permission-এর উদ্দেশ্য কী?

**সমাধান:** কোন user/process file পড়তে, লিখতে বা execute করতে পারবে তা নির্ধারণ।

## আরও পড়ো

- [https://www.kernel.org/doc/html/latest/admin-guide/mm/](https://www.kernel.org/doc/html/latest/admin-guide/mm/)
- [https://www.redhat.com/sysadmin/linux-file-permissions-explained](https://www.redhat.com/sysadmin/linux-file-permissions-explained)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
