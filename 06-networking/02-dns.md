# DNS: ডোমেইন নাম থেকে IP

## এই পাঠ শেষে

- DNS: ডোমেইন নাম থেকে IP সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Domain Name System মানুষের মনে রাখার মতো নামকে IP address ও অন্যান্য resource record-এর সঙ্গে যুক্ত করে। Browser domain খুললে resolver DNS lookup করে; cache-এ উত্তর থাকলে authoritative server-এ আবার যেতে হয় না। A record IPv4, AAAA IPv6, CNAME alias, MX mail server এবং TXT text information রাখতে পারে।

DNS hierarchy-তে root, top-level domain ও authoritative name server ভূমিকা রাখে। TTL বলে cache কতক্ষণ record রাখবে। DNS update সব user-এর কাছে একই মুহূর্তে দেখা যায় না, কারণ cache-এ পুরোনো উত্তর থাকতে পারে। DNS resolution সফল হলেও web server বন্ধ থাকতে পারে; তাই name resolution ও service reachability আলাদা করে যাচাই করো।

## বাস্তব জীবনের উপমা

ফোনের contact list-এ নাম দিয়ে নম্বর পাওয়া যায়। DNS domain name-এর সঙ্গে network information খুঁজে দেয়।

## মূল বিষয়

- Resolver client-এর হয়ে DNS query করে।
- A/AAAA address, MX mail server, CNAME alias দেয়।
- TTL cache duration নির্দেশ করে।

## Code example

```bash
nslookup example.com
dig example.com A
dig example.com MX
getent hosts example.com
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- DNS response-কে website সব ঠিক আছে বলে ধরে নেওয়া।
- TTL থাকা সত্ত্বেও DNS change সঙ্গে সঙ্গে সবখানে হবে ধরে নেওয়া।
- CNAME ও address record গুলিয়ে ফেলা।

## অনুশীলন ও সমাধান

### সমস্যা 1
কোন record IPv6 address দেয়?

**সমাধান:** AAAA record।

### সমস্যা 2
DNS cache-এর সুবিধা কী?

**সমাধান:** Repeated upstream query ও latency কমায়।

### সমস্যা 3
DNS ঠিক, কিন্তু page load না হলে আর কী পরীক্ষা করবে?

**সমাধান:** IP reachability, port, TLS certificate, HTTP server ও application error।

## আরও পড়ো

- [https://www.cloudflare.com/learning/dns/what-is-dns/](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [https://www.rfc-editor.org/rfc/rfc1035.html](https://www.rfc-editor.org/rfc/rfc1035.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
