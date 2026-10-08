# HTTP ও REST API

## এই পাঠ শেষে

- HTTP ও REST API সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

HTTP client ও server-এর request-response protocol। Request-এ method, path, headers ও প্রয়োজনে body থাকে; response-এ status code, headers ও body থাকে। `GET` সাধারণত resource পড়ে, `POST` resource বা action তৈরি করতে পারে, `PUT` representation বদলায়, `PATCH` আংশিক update করে, আর `DELETE` মুছে ফেলে। API contract-এ নির্দিষ্ট আচরণ স্পষ্ট থাকা জরুরি।

REST resource-ভিত্তিক API design style; URL-এ action verb ঢোকানোর বদলে resource ও HTTP method দিয়ে কাজ প্রকাশ করা যায়। Authentication, validation, pagination, rate limiting ও structured errors গুরুত্বপূর্ণ। `200`, `201`, `400`, `401`, `403`, `404`, `429` ও `500` বিভিন্ন outcome বোঝায়। Private API key frontend code-এ রাখলে তা গোপন থাকে না।

## বাস্তব জীবনের উপমা

লাইব্রেরির কাউন্টারে form দেওয়ার মতো: client request করে, server নিয়ম দেখে তথ্য ফেরায় বা বদলায়; status জানায় কী হলো।

## মূল বিষয়

- Request ও response HTTP যোগাযোগের দুই দিক।
- REST resource ও HTTP method দিয়ে operation প্রকাশ করতে পারে।
- Status code client-কে পরবর্তী পদক্ষেপ ঠিক করতে সাহায্য করে।

## Code example

```javascript
async function loadUser() {
  const response = await fetch("https://jsonplaceholder.typicode.com/users/1");
  if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
  const user = await response.json();
  return { id: user.id, name: user.name };
}
loadUser().then(user => console.log(user)).catch(error => console.error(error.message));
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- সব response-কে সফল ধরে JSON পড়া।
- Sensitive value URL query string-এ রাখা।
- Frontend bundle-এ private API secret রাখা।

## অনুশীলন ও সমাধান

### সমস্যা 1
নতুন resource সফলভাবে তৈরি হলে সাধারণ status কী?

**সমাধান:** সাধারণত `201 Created`।

### সমস্যা 2
`401` ও `403`-এর পার্থক্য কী?

**সমাধান:** `401` authentication প্রয়োজন/ব্যর্থ বোঝাতে পারে; `403` অনুমতি নেই বোঝায়।

### সমস্যা 3
API pagination কেন দরকার?

**সমাধান:** বড় result-কে ছোট page-এ ভাগ করলে latency ও memory চাপ কমে।

## আরও পড়ো

- [https://developer.mozilla.org/en-US/docs/Web/HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
- [https://www.rfc-editor.org/rfc/rfc9110.html](https://www.rfc-editor.org/rfc/rfc9110.html)
- [https://restfulapi.net/](https://restfulapi.net/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
