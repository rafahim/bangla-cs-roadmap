# Testing, CI ও CD

## এই পাঠ শেষে

- Testing, CI ও CD সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Testing নির্দিষ্ট condition-এ software প্রত্যাশিত result দেয় কি না যাচাই করে। Unit test ছোট function/module, integration test component-এর সংযোগ, আর end-to-end test user flow পরীক্ষা করে। Happy path-এর পাশাপাশি boundary, invalid input ও failure case অন্তর্ভুক্ত করো। আচরণ যাচাই করা test refactor সহজ রাখে; implementation detail-এ অতিরিক্ত বাঁধা test brittle হয়।

Continuous Integration (CI) change-এর পর automated build/test চালিয়ে integration bug দ্রুত ধরে। Continuous Delivery software-কে release-ready রাখে; Continuous Deployment সফল gate-এর পর production deploy স্বয়ংক্রিয় করতে পারে। Pipeline-এ lint, test, security check ও build থাকতে পারে। Secret log-এ ছাপিও না; deploy-এর আগে rollback ও database migration পরিকল্পনা করো।

## বাস্তব জীবনের উপমা

বই ছাপার আগে proofread, page check ও সম্পূর্ণ বই পরীক্ষা করার মতো—unit, integration ও end-to-end test আলাদা স্তরের যাচাই।

## মূল বিষয়

- Unit, integration ও end-to-end test-এর scope আলাদা।
- CI change-এর পর automated check চালায়।
- CD release/deployment repeatable করে; rollback পরিকল্পনা প্রয়োজন।

## Code example

```python
def calculate_discount(total, percent):
    if total < 0 or not 0 <= percent <= 100:
        raise ValueError("invalid amount or percent")
    return total * (1 - percent / 100)
def test_calculate_discount():
    assert calculate_discount(100, 10) == 90
    assert calculate_discount(0, 50) == 0
test_calculate_discount()
print("tests passed")
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Code চলেছে মানেই output ঠিক ধরে নেওয়া।
- Flaky test উপেক্ষা করা।
- CI secret repository বা log-এ প্রকাশ করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
একটি boundary test লেখো।

**সমাধান:** `assert calculate_discount(100, 0) == 100`।

### সমস্যা 2
CI-এর একটি উদ্দেশ্য কী?

**সমাধান:** Change-এর পর automated test/build চালিয়ে integration problem দ্রুত ধরা।

### সমস্যা 3
Delivery ও Deployment-এর প্রচলিত পার্থক্য কী?

**সমাধান:** Delivery release-ready state রাখে; Deployment সফল check-এর পর production release স্বয়ংক্রিয় করতে পারে।

## আরও পড়ো

- [https://docs.pytest.org/en/stable/](https://docs.pytest.org/en/stable/)
- [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
- [https://martinfowler.com/articles/continuousIntegration.html](https://martinfowler.com/articles/continuousIntegration.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
