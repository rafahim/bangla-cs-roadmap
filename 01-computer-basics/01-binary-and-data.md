# বাইনারি, বিট ও ডেটা

## এই পাঠ শেষে

- বাইনারি, বিট ও ডেটা সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Digital circuit সাধারণত দুটি স্থিতিশীল অবস্থাকে ০ ও ১ দিয়ে প্রকাশ করে। একটি binary digit bit; আট bit মিলে byte। সংখ্যা, লেখা, ছবি, অডিও ও ভিডিও—সবই bit sequence এবং সেই sequence ব্যাখ্যার নিয়ম দিয়ে উপস্থাপিত হয়। একই bit pattern এক প্রসঙ্গে সংখ্যা, অন্য প্রসঙ্গে রঙের মান হতে পারে।

দশমিক পদ্ধতিতে position-এর মান ১০-এর ঘাত, binary-তে ২-এর ঘাত। `1011₂` হলো ৮+০+২+১ = ১১। Text-এর ক্ষেত্রে Unicode character-কে code point দেয়, আর UTF-8-এর মতো encoding সেটিকে byte-এ প্রকাশ করে। ভুল encoding দিয়ে byte পড়লে বাংলা লেখা ভাঙা দেখা যায়; তাই text ও raw bytes-এর পার্থক্য বোঝা দরকার।

## বাস্তব জীবনের উপমা

শুধু বাড়ির নম্বর দেখলে ঠিকানা সম্পূর্ণ হয় না; কোন রাস্তার নম্বর তা জানতে হয়। Bit-এর অর্থ বুঝতেও encoding বা data format জানতে হয়।

## মূল বিষয়

- Bit হলো binary digit; byte সাধারণত ৮ bit।
- Binary positional notation-এ প্রতিটি ঘর ২-এর ঘাত।
- Unicode character identity বর্ণনা করে; UTF-8 byte encoding করে।

## Code example

```python
value = 0b1011
print(value)
print(format(value, "08b"))
text = "বাংলা"
encoded = text.encode("utf-8")
print(encoded)
print(encoded.decode("utf-8"))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Bit ও byte-কে একই একক ভাবা।
- সব বাংলা অক্ষর এক byte ধরে নেওয়া।
- Fixed-width data-তে leading zero-কে অপ্রয়োজনীয় ভাবা।

## অনুশীলন ও সমাধান

### সমস্যা 1
`1101₂` দশমিক কত?

**সমাধান:** ৮+৪+০+১ = ১৩।

### সমস্যা 2
৪ byte-এ কত bit?

**সমাধান:** ৪×৮ = ৩২ bit।

### সমস্যা 3
ভুল encoding-এ বাংলা ফাইল খুললে কী হতে পারে?

**সমাধান:** Byte ভুল নিয়মে character-এ রূপান্তরিত হয়ে ভাঙা লেখা দেখা যেতে পারে।

## আরও পড়ো

- [https://unicode.org/standard/standard.html](https://unicode.org/standard/standard.html)
- [https://docs.python.org/3/library/stdtypes.html#bytes-and-bytearray](https://docs.python.org/3/library/stdtypes.html#bytes-and-bytearray)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
