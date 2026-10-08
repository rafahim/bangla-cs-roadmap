# Relational Database ও SQL

## এই পাঠ শেষে

- Relational Database ও SQL সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Relational database data-কে table, row ও column-এ সাজায়। Students বা courses-এর মতো প্রতিটি table একটি বিষয় রাখে। Primary key প্রতিটি row-কে অনন্যভাবে চিহ্নিত করে; data type ও constraint ভুল data ঠেকায়। SQL দিয়ে schema তৈরি, data insert/update/delete ও query করা যায়।

`SELECT` column বেছে নেয়, `FROM` table, `WHERE` filter, `ORDER BY` sort এবং `LIMIT` result সীমিত করে। User input সরাসরি query string-এ জুড়লে SQL injection হতে পারে; parameterized query ব্যবহার করো। ভালো schema-তে key, nullability, data format ও domain rule স্পষ্ট থাকে।

## বাস্তব জীবনের উপমা

Spreadsheet-এর মতো table হলেও database constraint ও relation নির্দিষ্ট করে। Student ID পরিচয়পত্রের মতো, যা একই নামের দুই শিক্ষার্থীকে আলাদা করতে পারে।

## মূল বিষয়

- Table row ও column দিয়ে data রাখে।
- Primary key প্রতিটি row-কে uniquely চিহ্নিত করে।
- Parameterized query user input-কে SQL structure থেকে আলাদা রাখে।

## Code example

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 0)
);
INSERT INTO students (id, name, age) VALUES (1, 'Samia', 20);
SELECT id, name FROM students WHERE age >= 18 ORDER BY name;
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- User input query string-এ concatenate করা।
- শুধু নাম দিয়ে row চিহ্নিত করা।
- Column meaning ও constraints না ভেবে schema বানানো।

## অনুশীলন ও সমাধান

### সমস্যা 1
Primary key-এর কাজ কী?

**সমাধান:** প্রতিটি row-কে নির্ভরযোগ্যভাবে স্বতন্ত্র চিহ্নিত করে।

### সমস্যা 2
১৮ বা তার বেশি বয়সের student দেখাতে কোন clause?

**সমাধান:** `WHERE age >= 18`।

### সমস্যা 3
SQL injection ঠেকাতে কী ব্যবহার করবে?

**সমাধান:** Prepared/parameterized query এবং সীমিত database permission।

## আরও পড়ো

- [https://www.postgresql.org/docs/current/tutorial.html](https://www.postgresql.org/docs/current/tutorial.html)
- [https://sqlbolt.com/](https://sqlbolt.com/)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
