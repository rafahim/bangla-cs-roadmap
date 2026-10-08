# AI ও Machine Learning-এর ভিত্তি

## এই পাঠ শেষে

- AI ও Machine Learning-এর ভিত্তি সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Artificial Intelligence হলো perception, reasoning, planning বা language-এর মতো কাজে কম্পিউটারকে সক্ষম করার বিস্তৃত ক্ষেত্র। Machine Learning AI-এর একটি অংশ; প্রতিটি rule হাতে না লিখে data থেকে pattern শেখানো হয়। Model শেখা pattern দিয়ে prediction বা decision করে। Training data parameter শেখায়, validation data model নির্বাচন করে, আর held-out test data final performance অনুমানে আলাদা রাখা উচিত।

Data খারাপ হলে বড় model-ও ভুল বা biased হতে পারে। Feature input তথ্য, label supervised learning-এর expected answer। Machine learning সব সমস্যার উত্তর নয়—rule-based logic বা সাধারণ statistics অধিক উপযুক্ত হতে পারে। Data leakage ও distribution shift result-কে অযথা আশাবাদী করতে পারে।

## বাস্তব জীবনের উপমা

শিক্ষক উদাহরণ দিয়ে pattern শেখান; শিক্ষার্থী নতুন সমস্যায় প্রয়োগ করে। শেখা উদাহরণের বাইরে গেলে ভুলও হতে পারে, তাই নতুন প্রশ্নে পরীক্ষা জরুরি।

## মূল বিষয়

- AI বিস্তৃত ক্ষেত্র; ML data থেকে pattern শেখে।
- Feature input তথ্য; label প্রত্যাশিত target।
- Train, validation ও test set-এর আলাদা উদ্দেশ্য।

## Code example

```python
from statistics import mean
hours = [1, 2, 3, 4, 5]
scores = [42, 48, 57, 65, 71]
print(round(mean(hours), 1), round(mean(scores), 1))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Correlation-কে causation ধরে নেওয়া।
- Model selection-এর সময় test set বারবার ব্যবহার করা।
- AI সবসময় neutral বা correct বিশ্বাস করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
ML-এ label কী?

**সমাধান:** Supervised example-এর expected target/answer।

### সমস্যা 2
Test data training-এ ব্যবহার না করার কারণ কী?

**সমাধান:** Unseen data-তে generalization স্বাধীনভাবে মূল্যায়ন করতে।

### সমস্যা 3
সব সমস্যায় ML দরকার কি?

**সমাধান:** না; rule বা simple algorithm যথেষ্ট হলে সেটিই সহজ ও ব্যাখ্যাযোগ্য।

## আরও পড়ো

- [https://developers.google.com/machine-learning/crash-course](https://developers.google.com/machine-learning/crash-course)
- [https://scikit-learn.org/stable/user_guide.html](https://scikit-learn.org/stable/user_guide.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
