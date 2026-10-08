# Indexes ও Transactions

## এই পাঠ শেষে

- Indexes ও Transactions সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Index table-এ row খুঁজতে সাহায্য করে, বইয়ের সূচির মতো। Index না থাকলে database-কে অনেক row scan করতে হতে পারে। তবে index storage নেয় এবং insert/update/delete-এ update করতে হয়; সব column-এ index বানানো বুদ্ধিমানের কাজ নয়। Query plan, query pattern ও data distribution দেখে index নির্বাচন করো।

Transaction একাধিক operation-কে এক logical unit হিসেবে চালায়। ACID হলো Atomicity, Consistency, Isolation ও Durability। ব্যাংক transfer-এ এক account থেকে টাকা কমে অন্য account-এ যোগ না হলে data ভুল; transaction আংশিক update commit হওয়া আটকাতে পারে। Concurrent access-এ isolation level ও lock performance এবং correctness-এর trade-off তৈরি করতে পারে।

## বাস্তব জীবনের উপমা

বইয়ের সূচি দ্রুত বিষয় খুঁজে দেয়, কিন্তু সূচি তৈরি ও update করার খরচ আছে। Transaction এমন transfer, যেখানে পুরো কাজ সফল হবে নয়তো rollback হবে।

## মূল বিষয়

- Index নির্দিষ্ট query দ্রুত করতে পারে।
- Transaction একাধিক change-কে atomic unit করে।
- ACID reliable database operation বোঝার ভিত্তি।

## Code example

```sql
CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL CHECK (balance >= 0));
INSERT INTO accounts VALUES (1, 1000), (2, 200);
BEGIN;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;
SELECT id, balance FROM accounts ORDER BY id;
CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE INDEX idx_students_name ON students(name);
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- অপ্রয়োজনীয় index দিয়ে write cost বাড়ানো।
- ভুল WHERE clause-এ অনেক row update করা।
- Transaction commit/rollback-এর আগে connection ছেড়ে দেওয়া।

## অনুশীলন ও সমাধান

### সমস্যা 1
Index-এর সুবিধা ও খরচ লেখো।

**সমাধান:** Query দ্রুত হতে পারে; storage লাগে ও write-এর সময় index update হয়।

### সমস্যা 2
Transfer-এর দ্বিতীয় update ব্যর্থ হলে কী করতে হবে?

**সমাধান:** Transaction rollback করতে হবে যাতে আংশিক transfer স্থায়ী না হয়।

### সমস্যা 3
Slow query-তে প্রথমে কী দেখবে?

**সমাধান:** Query plan, WHERE filter, JOIN, index ও data distribution।

## আরও পড়ো

- [https://www.postgresql.org/docs/current/indexes.html](https://www.postgresql.org/docs/current/indexes.html)
- [https://www.postgresql.org/docs/current/tutorial-transactions.html](https://www.postgresql.org/docs/current/tutorial-transactions.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
