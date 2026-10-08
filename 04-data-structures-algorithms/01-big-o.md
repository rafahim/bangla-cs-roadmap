# Big-O: অ্যালগরিদমের বৃদ্ধি বিশ্লেষণ

## এই পাঠ শেষে

- Big-O: অ্যালগরিদমের বৃদ্ধি বিশ্লেষণ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Big-O input size বাড়লে algorithm-এর কাজ কীভাবে বাড়ে তার asymptotic বর্ণনা। এটি নির্দিষ্ট machine-এ seconds মাপার বিকল্প নয়; বড় input-এ কোন algorithm scale করবে তা তুলনা করতে সাহায্য করে। `O(1)` constant, `O(log n)` logarithmic, `O(n)` linear, `O(n log n)` অনেক efficient sorting-এর প্রচলিত order এবং `O(n²)` pairwise কাজের পরিচিত উদাহরণ। Constant factor ও lower-order term সাধারণত বাদ দেওয়া হয়।

Time complexity-এর পাশাপাশি space complexity দেখো—অতিরিক্ত memory কত বাড়ে। এক loop প্রায়ই `O(n)`, সব pair তুলনা করা nested loop প্রায়ই `O(n²)`, কিন্তু loop-এর bound বিশ্লেষণ ছাড়া complexity বলা যায় না। Best, average ও worst case আলাদা হতে পারে। Readability, memory, real input distribution ও benchmark-ও decision-এ গুরুত্বপূর্ণ।

## বাস্তব জীবনের উপমা

এক তালিকায় একজন একজন করে নাম খোঁজা linear search; প্রতিবার তালিকা অর্ধেক করা logarithmic search। তালিকা বড় হলে growth-এর পার্থক্য দ্রুত বেড়ে যায়।

## মূল বিষয়

- Complexity input size `n`-এর function হিসেবে দেখা হয়।
- Nested iteration কাজকে গুণিতকভাবে বাড়াতে পারে।
- Asymptotic analysis-এর পাশাপাশি বাস্তব performance test-ও দরকার।

## Code example

```python
def contains_pair_sum(values, target):
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target:
                return True
    return False

print(contains_pair_sum([2, 7, 11, 15], 9))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Big-O-কে সরাসরি milliseconds মনে করা।
- Space complexity বাদ দেওয়া।
- সব nested loop পরীক্ষা ছাড়াই `O(n²)` বলা।

## অনুশীলন ও সমাধান

### সমস্যা 1
List একবার traverse করলে complexity কী?

**সমাধান:** `O(n)`।

### সমস্যা 2
Balanced BST-তে lookup সাধারণত কত?

**সমাধান:** `O(log n)`; unbalanced worst case `O(n)`।

### সমস্যা 3
Input ১০০ গুণ হলে `O(n²)` কেন চিন্তার?

**সমাধান:** Quadratic work প্রায় ১০,০০০ গুণ হতে পারে।

## আরও পড়ো

- [https://www.bigocheatsheet.com/](https://www.bigocheatsheet.com/)
- [https://opendsa-server.cs.vt.edu/](https://opendsa-server.cs.vt.edu/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
