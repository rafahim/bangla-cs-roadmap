# CSS: লেআউট, রং ও responsive design

## এই পাঠ শেষে

- CSS: লেআউট, রং ও responsive design সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

CSS HTML element-এর রং, spacing, typography, অবস্থান ও responsive আচরণ নির্ধারণ করে। Selector বলে কোন element-এ style লাগবে; declaration-এ property ও value থাকে। Cascade, specificity ও source order একাধিক rule-এর মধ্যে কোনটি কার্যকর হবে তা প্রভাবিত করে। CSS custom property design token এক জায়গায় রাখতে সাহায্য করে, ফলে brand color ও spacing বদলানো সহজ হয়।

Responsive design হলো বিভিন্ন viewport-এ content-কে ব্যবহারযোগ্য রাখা। Flexible grid, relative unit, Flexbox, Grid ও media query দিয়ে layout মানিয়ে নেওয়া যায়। Fixed pixel width ছোট screen-এ overflow তৈরি করতে পারে। Keyboard focus, readable type ও color contrast-ও design-এর অংশ—শুধু আকর্ষণীয় রং দিলেই user experience ভালো হয় না।

## বাস্তব জীবনের উপমা

ঘর সাজানোর মতো: HTML দেয়াল ও দরজা, CSS দেয়ালের রং, আসবাবের দূরত্ব ও layout নির্ধারণ করে।

## মূল বিষয়

- Selector element নির্বাচন করে; specificity conflict মেটাতে প্রভাব ফেলে।
- Flexbox এক-দিকের layout, Grid দুই-মাত্রার layout-এ উপযোগী।
- Media query viewport বা user preference অনুযায়ী style বদলায়।

## Code example

```html
<!doctype html>
<html lang="bn">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
:root { --space: 1rem; --brand: #1e3a8a; }
body { font-family: system-ui, sans-serif; margin: 0; padding: var(--space); }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: var(--space); }
.card { border: 1px solid #cbd5e1; border-radius: 12px; padding: var(--space); }
h1 { color: var(--brand); }
</style>
</head>
<body><h1>শেখার বিষয়</h1><div class="cards"><article class="card">HTML</article><article class="card">CSS</article></div></body>
</html>
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- সব layout-এ fixed width ব্যবহার করা।
- অনেক `!important` দিয়ে specificity সমস্যা ঢেকে রাখা।
- Keyboard focus ও contrast উপেক্ষা করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Card-এর ভেতরে spacing বাড়াতে কোন property?

**সমাধান:** `padding`।

### সমস্যা 2
ছোট screen-এ card নিচে নামাতে কী কৌশল?

**সমাধান:** Grid-এর `auto-fit`/`minmax` বা media query ব্যবহার করা যায়।

### সমস্যা 3
`:root`-এ custom property রাখার সুবিধা কী?

**সমাধান:** একই design token বহু জায়গায় পুনর্ব্যবহার ও পরিবর্তন করা যায়।

## আরও পড়ো

- [https://developer.mozilla.org/en-US/docs/Learn/CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
- [https://web.dev/learn/css/](https://web.dev/learn/css/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
