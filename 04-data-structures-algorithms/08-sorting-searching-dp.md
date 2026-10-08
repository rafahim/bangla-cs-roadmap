# Sorting, Searching ও Dynamic Programming

## এই পাঠ শেষে

- Sorting, Searching ও Dynamic Programming সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Sorting data-কে ক্রমে সাজায়; searching target খোঁজে। Linear search unsorted list-এ একে একে পরীক্ষা করে `O(n)` সময় নেয়। Binary search sorted list-কে বারবার অর্ধেক করে `O(log n)` সময় নেয়; data sorted থাকা আবশ্যক। Merge sort সাধারণত `O(n log n)` সময় ও extra memory নেয়; quicksort গড়ে দ্রুত, তবে bad pivot-এ worst case `O(n²)` হতে পারে। Stability, in-place behavior ও input size-ও বিবেচনা করো।

Dynamic programming (DP) তখন কাজে লাগে যখন subproblem overlap করে এবং বড় সমস্যার উত্তরে ছোট সমস্যার result লাগে। Memoization recursive result cache করে; tabulation ছোট state থেকে table ভরে। Fibonacci-এর naive recursion একই কাজ বারবার করে; DP প্রতিটি value একবার হিসাব করতে পারে। DP শুরু করার আগে state, transition এবং base case নির্ধারণ করো।

## বাস্তব জীবনের উপমা

সাজানো অভিধানে মাঝখান থেকে শব্দ খুঁজে অর্ধেক দিক বাদ দেওয়া যায়। DP হলো একই অঙ্কের উত্তর খাতায় রেখে পরে আবার ব্যবহার করা।

## মূল বিষয়

- Linear search unsorted data-তেও চলে।
- Binary search-এর জন্য sorted data দরকার।
- DP overlapping subproblem ও optimal substructure কাজে লাগায়।

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
def fib(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    dp = [0, 1]
    for _ in range(2, n + 1):
        dp.append(dp[-1] + dp[-2])
    return dp[n]
print(binary_search([2, 5, 8, 12, 16], 12))
print(fib(10))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Unsorted list-এ binary search ব্যবহার করা।
- Boundary update ভুল করে endless loop তৈরি করা।
- DP state ও base case না ভেবে table তৈরি করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
`[1, 4, 7, 9]`-এ ৭-এর index কী?

**সমাধান:** Zero-based index ২।

### সমস্যা 2
Linear search worst-case time complexity?

**সমাধান:** `O(n)`।

### সমস্যা 3
DP Fibonacci naive recursion-এর চেয়ে দ্রুত কেন?

**সমাধান:** আগে হিসাব করা value reuse করে duplicate computation এড়ায়; tabulation `O(n)` সময় নেয়।

## আরও পড়ো

- [https://visualgo.net/en/sorting](https://visualgo.net/en/sorting)
- [https://cp-algorithms.com/](https://cp-algorithms.com/)
- [https://www.geeksforgeeks.org/dynamic-programming/](https://www.geeksforgeeks.org/dynamic-programming/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
