# Processes, Threads ও Concurrency

## এই পাঠ শেষে

- Processes, Threads ও Concurrency সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Process হলো চলমান program, যার সাধারণত নিজস্ব virtual address space থাকে। Thread একই process-এর resource ভাগ করে execution চালায়। আলাদা process isolation দেয়, তবে process-গুলোর মধ্যে IPC লাগে; shared-memory thread দ্রুত হতে পারে, কিন্তু race condition-এর ঝুঁকি থাকে।

Concurrency-তে কাজের অগ্রগতি overlap হয়; parallelism-এ কাজ একই সময়ে hardware-এ চলে। Single core-এ scheduler context switch করে concurrency দিতে পারে; multi-core-এ কাজ parallel হতে পারে। Lock, queue, atomic operation ও immutable data race কমাতে সাহায্য করে। ভুল lock ordering deadlock তৈরি করতে পারে।

## বাস্তব জীবনের উপমা

রেস্টুরেন্টের আলাদা অর্ডার process, আর একই রান্নাঘরের কর্মীরা thread-এর মতো; shared ingredient-এ সমন্বয় না থাকলে conflict হয়।

## মূল বিষয়

- Process isolation দেয়; thread process memory ভাগ করে।
- Concurrency ও parallelism এক নয়।
- Race condition shared state-এর unsynchronized access থেকে আসতে পারে।

## Code example

```python
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
def fetch_status(url):
    with urlopen(url, timeout=5) as response:
        return url, response.status
with ThreadPoolExecutor(max_workers=2) as pool:
    for result in pool.map(fetch_status, ["https://example.com", "https://www.iana.org"]):
        print(result)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Shared variable বহু thread বদলালেও নিরাপদ ধরে নেওয়া।
- Concurrency সব CPU-bound code দ্রুত করবে ভাবা।
- Deadlock-এর সম্ভাবনা উপেক্ষা করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Process ও thread-এর একটি পার্থক্য লেখো।

**সমাধান:** Process সাধারণত আলাদা address space পায়; একই process-এর thread memory ভাগ করে।

### সমস্যা 2
Race condition-এর উদাহরণ কী?

**সমাধান:** দুই thread একই counter পড়া-লেখা করলে increment হারিয়ে যেতে পারে।

### সমস্যা 3
Network I/O-তে thread উপকারী কেন?

**সমাধান:** এক request অপেক্ষা করলে অন্য কাজ এগোতে পারে; ফল workload ও runtime-এর ওপর নির্ভর করে।

## আরও পড়ো

- [https://docs.python.org/3/library/concurrent.futures.html](https://docs.python.org/3/library/concurrent.futures.html)
- [https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads](https://learn.microsoft.com/en-us/windows/win32/procthread/processes-and-threads)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
