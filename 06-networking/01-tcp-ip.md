# TCP/IP ও নেটওয়ার্ক যোগাযোগ

## এই পাঠ শেষে

- TCP/IP ও নেটওয়ার্ক যোগাযোগ সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Network-এ device নিয়ম মেনে data বিনিময় করে। TCP/IP suite-এ IP address ও routing-এ কাজ করে; TCP ordered reliable byte stream দেয়; UDP কম overhead-এ datagram পাঠায় কিন্তু delivery guarantee দেয় না। Packet loss, delay, congestion ও reset হতে পারে, তাই application-এ timeout এবং error handling দরকার।

IP address host/interface-কে address করে, port একই host-এর service আলাদা করে। TCP connection establish করতে handshake হয়। TCP reliable হলেই data encrypted নয়; TLS encryption ও server identity validation-এ সাহায্য করে। Troubleshooting-এ DNS, IP reachability, port, TLS ও application response আলাদা করে পরীক্ষা করো।

## বাস্তব জীবনের উপমা

ডাকব্যবস্থার মতো: IP গন্তব্য address করে, আর TCP delivery-র ক্রম ও missing data সামলাতে চেষ্টা করে।

## মূল বিষয়

- IP addressing ও routing করে।
- TCP ordered reliable stream, UDP datagram দেয়।
- Port একই host-এর service আলাদা করে।

## Code example

```python
import socket
address = ("example.com", 80)
with socket.create_connection(address, timeout=5) as connection:
    connection.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n")
    response = connection.recv(200)
    print(response.decode("latin-1", errors="replace"))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- TCP/IP-কে একটিমাত্র protocol ভাবা।
- Port-কে IP address-এর বিকল্প মনে করা।
- TCP নিজেই encryption দেয় ধরে নেওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
TCP ও UDP-এর মূল পার্থক্য কী?

**সমাধান:** TCP ordered reliable stream দেয়; UDP datagram পাঠায় কিন্তু নিজে delivery/order guarantee দেয় না।

### সমস্যা 2
এক server-এ port কেন দরকার?

**সমাধান:** এক host-এ web, SSH ইত্যাদি service-এর traffic আলাদা করতে।

### সমস্যা 3
TCP connection কি গোপনীয়তা নিশ্চিত করে?

**সমাধান:** না; data transit encrypt করতে TLS-এর মতো protocol লাগে।

## আরও পড়ো

- [https://www.rfc-editor.org/rfc/rfc9293.html](https://www.rfc-editor.org/rfc/rfc9293.html)
- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
