# Object-Oriented Programming (OOP)

## এই পাঠ শেষে

- Object-Oriented Programming (OOP) সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

OOP-তে state ও behavior object/class দিয়ে সংগঠিত হয়। Class হলো instance তৈরির blueprint; object তার নির্দিষ্ট instance। Encapsulation internal state ও public interface আলাদা করে। Inheritance behavior সম্প্রসারণ করতে পারে, কিন্তু গভীর hierarchy জটিল; polymorphism একই interface-এর ভিন্ন implementation ব্যবহারের সুযোগ দেয়।

OOP একমাত্র সমাধান নয়। State ও behavior ঘনিষ্ঠভাবে সম্পর্কিত হলে class সুবিধাজনক; ছোট transformation-এর জন্য function সহজ হতে পারে। Constructor initial state তৈরি করে। Method-এর precondition, side effect ও invariant বোঝা দরকার। Composition—এক object-এর ভেতরে অন্য object ব্যবহার—অনেক সময় inheritance-এর চেয়ে flexible।

## বাস্তব জীবনের উপমা

Mobile phone-এর public button ব্যবহার করা যায়, ভেতরের সার্কিটের সব detail জানতে হয় না। Encapsulation implementation detail আড়াল করে।

## মূল বিষয়

- Class থেকে instance তৈরি হয়।
- Encapsulation state ও interface আলাদা রাখে।
- Inheritance ও composition-এর trade-off আছে।
- Polymorphism একই contract-এ ভিন্ন implementation চালায়।

## Code example

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self.owner = owner
        self._balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount
    @property
    def balance(self):
        return self._balance
account = BankAccount("Samia", 100)
account.deposit(50)
print(account.balance)
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- প্রতিটি ছোট কাজের জন্য class বানানো।
- Internal state-এ যেকোনো জায়গা থেকে পরিবর্তন অনুমোদন করা।
- শুধু code reuse-এর জন্য অপ্রাসঙ্গিক inheritance করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Class ও object-এর পার্থক্য কী?

**সমাধান:** Class blueprint; object ওই class-এর instance।

### সমস্যা 2
Deposit-এর আগে amount validate কেন?

**সমাধান:** Invalid amount state invariant নষ্ট করতে পারে।

### সমস্যা 3
Composition-এর উদাহরণ দাও।

**সমাধান:** Car-এর ভেতরে Engine object রাখা; engine behavior inherit না করে object-টি ব্যবহার করা।

## আরও পড়ো

- [https://docs.python.org/3/tutorial/classes.html](https://docs.python.org/3/tutorial/classes.html)
- [https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
