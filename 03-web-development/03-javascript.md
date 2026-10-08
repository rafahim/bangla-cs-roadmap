# JavaScript: ওয়েবে আচরণ যোগ করা

## এই পাঠ শেষে

- JavaScript: ওয়েবে আচরণ যোগ করা সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

JavaScript browser-এ button click, form validation, DOM পরিবর্তন, asynchronous request ও state management করে। `const` binding পুনরায় assign করা যায় না, `let` যায়; তবে `const` object-এর property বদলাতে পারে। `===` সাধারণত type conversion ছাড়া তুলনা করে, তাই unintended coercion এড়াতে এটি স্পষ্ট পছন্দ।

Browser JavaScript event-driven: click, input বা submit হলে handler চলে। DOM API দিয়ে element পড়া ও বদলানো যায়। `fetch()` Promise দেয়; HTTP error status-এ Promise সবসময় reject হয় না, তাই `response.ok` যাচাই জরুরি। User content DOM-এ বসানোর সময় `textContent` সাধারণত `innerHTML`-এর চেয়ে নিরাপদ, কারণ raw HTML হিসেবে parse করে না।

## বাস্তব জীবনের উপমা

Remote control-এর মতো: HTML control ও screen-এর কাঠামো, CSS চেহারা, আর JavaScript button চাপলে কী হবে তা নির্ধারণ করে।

## মূল বিষয়

- `const`/`let` block scope তৈরি করে।
- DOM HTML document-এর object representation।
- Event handler user action-এ সাড়া দেয়।
- Promise ও `async/await` asynchronous code সহজ করে।

## Code example

```html
<!doctype html>
<html lang="bn"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Click demo</title></head>
<body><button id="countButton" type="button">চাপ দাও</button><p id="count">০</p>
<script>
const button = document.querySelector("#countButton");
const output = document.querySelector("#count");
let count = 0;
button.addEventListener("click", () => { count += 1; output.textContent = String(count); });
</script></body></html>
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- সব জায়গায় `var` ব্যবহার করা।
- Fetch response-এর status যাচাই না করা।
- Untrusted input সরাসরি `innerHTML`-এ বসানো।

## অনুশীলন ও সমাধান

### সমস্যা 1
Click-এ count বাড়াতে কোন event লাগবে?

**সমাধান:** `click` event এবং `addEventListener()`।

### সমস্যা 2
`const` object-এর property বদলানো যায়?

**সমাধান:** হ্যাঁ, binding reassign না করে property বদলানো যায়।

### সমস্যা 3
Fetch-এর পরে `response.ok` কেন যাচাই করবে?

**সমাধান:** ৪০৪/৫০০ status-ও Promise resolve করতে পারে; status আলাদা যাচাই দরকার।

## আরও পড়ো

- [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
- [https://javascript.info/](https://javascript.info/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
