# HTML: ওয়েব পৃষ্ঠার কাঠামো

## এই পাঠ শেষে

- HTML: ওয়েব পৃষ্ঠার কাঠামো সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

HTML semantic structure তৈরি করে। Heading, paragraph, navigation, link, image, list, form ও table-এর জন্য অর্থবহ element আছে। `<h1>` কেবল বড় অক্ষরের জন্য নয়; এটি প্রধান heading বোঝায়। `<a>` navigation-এর জন্য, `<button>` action-এর জন্য, আর `<label>` form control চিহ্নিত করে। Semantic HTML accessibility, keyboard navigation, search ও maintenance-এ সাহায্য করে।

Element সাধারণত opening tag, content ও closing tag নিয়ে গঠিত; `<img>` ও `<input>`-এর মতো void element-এর closing tag থাকে না। Attribute অতিরিক্ত তথ্য দেয়। HTML structure, CSS presentation এবং JavaScript behavior আলাদা রাখলে site রক্ষণাবেক্ষণ সহজ হয়। User-generated content দেখানোর সময় input-কে markup ভেবে নেওয়া বা unsafe HTML হিসেবে render করা যাবে না।

## বাস্তব জীবনের উপমা

বইয়ের অধ্যায় ও শিরোনাম: রং বা font না দেখেও কাঠামো বোঝা যায়। HTML বলে কোনটি title, paragraph, image বা link।

## মূল বিষয়

- Semantic element অর্থ প্রকাশ করে।
- Attribute element-এর বৈশিষ্ট্য নির্ধারণ করে।
- Image-এ meaningful `alt` text দরকার; decorative image-এ empty alt হতে পারে।

## Code example

```html
<!doctype html>
<html lang="bn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>আমার প্রথম পৃষ্ঠা</title>
</head>
<body>
  <header><h1>বাংলা CS Roadmap</h1></header>
  <main><p>এটি semantic HTML উদাহরণ।</p><a href="https://developer.mozilla.org/">MDN পড়ো</a></main>
</body>
</html>
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- শুধু বড় font দেখাতে heading tag বেছে নেওয়া।
- Image-এ alt বাদ দেওয়া।
- Form control-এর সঙ্গে label যুক্ত না করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
প্রধান heading-এর element কী?

**সমাধান:** `<h1>`।

### সমস্যা 2
Link ও button-এর পার্থক্য কী?

**সমাধান:** Link resource/location-এ নেয়; button সাধারণত action চালায়।

### সমস্যা 3
`lang="bn"` কেন সহায়ক?

**সমাধান:** Browser ও assistive technology-কে document-এর ভাষা জানায়।

## আরও পড়ো

- [https://developer.mozilla.org/en-US/docs/Learn/HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [https://html.spec.whatwg.org/](https://html.spec.whatwg.org/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
