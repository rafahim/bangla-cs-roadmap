# HTTPS, TLS ও নিরাপদ সংযোগ

## এই পাঠ শেষে

- HTTPS, TLS ও নিরাপদ সংযোগ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

HTTPS হলো TLS-এর মধ্যে HTTP চালানো। TLS transit-এ data encrypt করে এবং certificate দিয়ে server identity যাচাইয়ে সহায়তা করে। Browser certificate chain, expiry ও hostname পরীক্ষা করে; security warning উপেক্ষা করলে impostor server-এর ঝুঁকি থাকে। HTTPS transit security বাড়ায়, কিন্তু server-এ stored data, user identity বা application bug নিজে থেকে নিরাপদ করে না।

Web security-তে authentication, authorization, input validation, secure cookie, CSRF/XSS protection, dependency update ও secret management-ও দরকার। Password plain text-এ রাখা উচিত নয়; password-specific hashing ব্যবহার করো। Certificate expiry, mixed content ও exposed secret ঝুঁকি তৈরি করে। Security হলো নিয়মিত review ও patching-এর প্রক্রিয়া।

## বাস্তব জীবনের উপমা

সিল করা খাম ও প্রেরকের পরিচয় যাচাইয়ের মতো। HTTPS মাঝপথে data পড়া/বদলানো কঠিন করে এবং certificate server-এর identity যাচাই করে।

## মূল বিষয়

- TLS encryption ও integrity দেয়।
- Authentication পরিচয় যাচাই; authorization permission নির্ধারণ।
- HTTPS application vulnerability স্বয়ংক্রিয়ভাবে ঠিক করে না।

## Code example

```bash
curl -I https://example.com
openssl s_client -connect example.com:443 -servername example.com </dev/null
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Padlock দেখেই পুরো application নিরাপদ ভাবা।
- TLS warning উপেক্ষা করে password দেওয়া।
- API secret source code-এ রাখা।

## অনুশীলন ও সমাধান

### সমস্যা 1
HTTPS data-কে কীভাবে সুরক্ষা দেয়?

**সমাধান:** TLS-এর মাধ্যমে connection-এ data encrypt ও integrity-protected করে।

### সমস্যা 2
Authentication ও authorization কীভাবে আলাদা?

**সমাধান:** প্রথমটি পরিচয় যাচাই, দ্বিতীয়টি অনুমতি নির্ধারণ।

### সমস্যা 3
HTTPS থাকলেও XSS কেন হতে পারে?

**সমাধান:** HTTPS transit রক্ষা করে; unsafe input render করার application bug আলাদা।

## আরও পড়ো

- [https://developer.mozilla.org/en-US/docs/Web/Security](https://developer.mozilla.org/en-US/docs/Web/Security)
- [https://www.rfc-editor.org/rfc/rfc8446.html](https://www.rfc-editor.org/rfc/rfc8446.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
