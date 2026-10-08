# Recursion: নিজেকে ডাকা

## এই পাঠ শেষে

- Recursion: নিজেকে ডাকা সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Recursion-এ function একই সমস্যার ছোট সংস্করণ সমাধান করতে নিজেকেই call করে। প্রতিটি recursive function-এর base case থাকতে হবে, যেখানে আর recursion হয় না; recursive case-এ input-কে base case-এর দিকে ছোট করতে হয়। Factorial-এর নিয়ম `n! = n × (n-1)!`, এবং `0! = 1`। Base case ভুল হলে function থামবে না অথবা ভুল ফল দেবে।

প্রতিটি recursive call call stack-এ একটি frame তৈরি করতে পারে। খুব গভীর recursion stack limit ছাড়াতে পারে, এবং naive Fibonacci-এর মতো code একই subproblem বারবার গণনা করতে পারে। Tree traversal ও divide-and-conquer-এ recursion স্বাভাবিক; loop কখনও কম memory ব্যবহার করে। Code বেছে নাও readability, input depth এবং performance দেখে।

## বাস্তব জীবনের উপমা

এক বাক্স খুলে ভেতরে আরেকটি ছোট বাক্স, তারপর আরেকটি—শেষে base case-এ খালি বাক্স পাওয়া যায়।

## মূল বিষয়

- Base case recursion থামায়।
- Recursive step input-কে ছোট বা সহজ করে।
- Call stack অসমাপ্ত call-এর state ধরে।

## Code example

```python
def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Base case বাদ দেওয়া।
- Recursive call-এ input না কমানো।
- Repeated computation বা recursion depth উপেক্ষা করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
`factorial(4)`-এর ফল কী?

**সমাধান:** ৪×৩×২×১ = ২৪।

### সমস্যা 2
Naive Fibonacci recursion ধীর কেন?

**সমাধান:** একই subproblem বারবার হিসাব করে; memoization বা iteration তা কমায়।

### সমস্যা 3
Recursive function review-এর দুটি প্রশ্ন কী?

**সমাধান:** Base case আছে কি এবং প্রতিটি call termination-এর দিকে যাচ্ছে কি?।

## আরও পড়ো

- [https://docs.python.org/3/reference/compound_stmts.html#function-definitions](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)
- [https://en.wikipedia.org/wiki/Recursion_(computer_science)](https://en.wikipedia.org/wiki/Recursion_(computer_science))

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
