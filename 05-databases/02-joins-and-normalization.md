# JOIN ও Database Normalization

## এই পাঠ শেষে

- JOIN ও Database Normalization সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Student ও course-এর তথ্য আলাদা table-এ থাকলে JOIN matching key-এর ভিত্তিতে সেগুলো মিলিয়ে দেখায়। `INNER JOIN` matching row দেয়; `LEFT JOIN` বাম table-এর সব row রাখে, ডান দিকে match না থাকলে NULL দেখায়। Join condition ভুল হলে duplicate বা অপ্রত্যাশিত row তৈরি হতে পারে, তাই key ও relationship বোঝা জরুরি।

Normalization duplicate data ও update anomaly কমায়। একই course name প্রতিটি enrollment row-তে রাখলে name বদলাতে বহু row update করতে হবে। Course আলাদা table-এ রেখে relationship foreign key দিয়ে প্রকাশ করলে তথ্য এক জায়গায় maintain করা যায়। অতিরিক্ত normalization ও read performance-এর trade-off থাকতে পারে, কিন্তু data integrity দিয়ে শুরু করো।

## বাস্তব জীবনের উপমা

স্কুলের student register ও course register আলাদা; ID দিয়ে প্রয়োজনের সময় দুই register মেলানো হয়, নাম বারবার লিখতে হয় না।

## মূল বিষয়

- JOIN related table-এর row মেলায়।
- Foreign key অন্য table-এর key reference করে।
- Normalization duplicate data ও update anomaly কমায়।

## Code example

```sql
CREATE TABLE courses (id INTEGER PRIMARY KEY, title TEXT NOT NULL);
CREATE TABLE enrollments (student_id INTEGER, course_id INTEGER REFERENCES courses(id));
INSERT INTO courses VALUES (1, 'HTML'), (2, 'SQL');
INSERT INTO enrollments VALUES (10, 1), (11, 2);
SELECT e.student_id, c.title
FROM enrollments AS e
JOIN courses AS c ON c.id = e.course_id;
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- JOIN condition বাদ দিয়ে accidental cartesian product তৈরি করা।
- এক table-এ course name বারবার রাখা।
- LEFT JOIN-এ NULL আসতে পারে তা উপেক্ষা করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
INNER JOIN কী ফেরায়?

**সমাধান:** Join condition-এ matching row-গুলো।

### সমস্যা 2
Enroll না করা student-সহ সব student দেখাতে কী join লাগতে পারে?

**সমাধান:** Students table থেকে enrollments-এ `LEFT JOIN`।

### সমস্যা 3
Course title এক জায়গায় রাখার সুবিধা কী?

**সমাধান:** Name বদলালে এক row update হয়, duplicate ও inconsistency কমে।

## আরও পড়ো

- [https://www.postgresql.org/docs/current/queries-table-expressions.html](https://www.postgresql.org/docs/current/queries-table-expressions.html)
- [https://sqlbolt.com/lesson/select_queries_with_joins](https://sqlbolt.com/lesson/select_queries_with_joins)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
