from pathlib import Path
import json, zipfile
ROOT = Path(__file__).resolve().parent
LESSONS = json.loads((ROOT / 'lessons.json').read_text(encoding='utf-8'))
SECTIONS = {
'00-getting-started': ('শুরু করার আগে','প্রোগ্রামিং, সমস্যা ভাঙা এবং Git দিয়ে কাজের ইতিহাস রাখার ভিত্তি তৈরি করো।','আধুনিক browser, Python 3, Git ও text editor ব্যবহার করো। উদাহরণ নিজে চালালে debugging-এর অভ্যাস তৈরি হবে।'),
'01-computer-basics': ('কম্পিউটার বেসিকস','কম্পিউটার, binary data, CPU/RAM/storage, OS, file ও process-এর ভিত্তি তৈরি করো।','Hardware, operating system ও command line-এর পার্থক্য বুঝে পরে runtime ও memory ধারণার সঙ্গে যুক্ত করো।'),
'02-programming-fundamentals': ('Programming Fundamentals','Variable, type, operator, control flow, function ও recursion দিয়ে ছোট সমাধান বানাও।','Python 3-এ উদাহরণ চালাও। Error message পড়া, boundary input পরীক্ষা এবং algorithm ব্যাখ্যা করা অনুশীলন করো।'),
'03-web-development': ('Web Development','HTML, CSS, JavaScript, string/object, HTTP ও REST API দিয়ে browser-server flow বোঝো।','HTML উদাহরণ browser-এ খোলো। JavaScript browser console বা Node.js-এ চালাও; API উদাহরণে internet লাগতে পারে।'),
'04-data-structures-algorithms': ('Data Structures & Algorithms','Complexity, data structures, sorting/searching ও dynamic programming-এর কৌশল শেখো।','প্রতিটি structure-এর operation cost, boundary case ও কখন ব্যবহার করা উপযুক্ত—তা ব্যাখ্যা করো।'),
'05-databases': ('Databases','Relational modeling, SQL query, JOIN, normalization, index ও transaction বোঝো।','SQL উদাহরণ PostgreSQL-ধাঁচের; কিছু syntax অন্য database-এ আলাদা হতে পারে। Destructive query-এর আগে test database ব্যবহার করো।'),
'06-networking': ('Networking','TCP/IP, DNS, HTTPS ও network troubleshooting-এর স্তরগুলো বোঝো।','Network command-এ connectivity লাগতে পারে। Security test কেবল নিজের বা অনুমোদিত system-এ চালাও।'),
'07-operating-systems': ('Operating Systems','Process/thread, memory, filesystem, shell ও permission-এর বাস্তব প্রয়োগ দেখো।','কিছু উদাহরণ Unix-ধাঁচের shell-এর জন্য। System file বদলানোর আগে command target যাচাই করো।'),
'08-software-engineering': ('Software Engineering','OOP, functional style, design pattern, testing ও CI/CD workflow শেখো।','বাস্তব project-এ test, reviewable commit ও repeatable setup যোগ করে ধারণাগুলো প্রয়োগ করো।'),
'09-ai-ml': ('AI ও Machine Learning','ML foundation, supervised/unsupervised learning, evaluation ও responsible AI জানো।','scikit-learn উদাহরণের জন্য `python -m pip install scikit-learn` লাগতে পারে। Privacy, fairness ও context বিবেচনা করো।'),
'10-career': ('Career & Practice','Portfolio, teamwork, code review, CV ও technical interview প্রস্তুতি নাও।','README, tests, demo ও limitation লিখলে অন্য কেউ তোমার কাজ যাচাই করতে পারবে।')}
ROOT_FILES = {
'README.md': '''# বাংলা CS Roadmap
> বাংলায় Computer Science শেখার সম্পূর্ণ গাইড
Maintained by [RA Fahim](https://rafahim.com) · [github.com/rafahim](https://github.com/rafahim)

## 🔍 SEO
**Description / keywords:** bangla cs roadmap, bengali programming guide, bangla coding tutorial

বাংলাভাষী শিক্ষার্থীদের জন্য Computer Science, programming, web development, data structures, database, networking, operating systems, software engineering এবং AI/ML শেখার ধাপে ধাপে পাঠ্যক্রম। প্রতিটি পাঠে রয়েছে ব্যাখ্যা, বাস্তব উদাহরণ, code sample, সাধারণ ভুল, সমাধানসহ অনুশীলন ও আরও পড়ার উৎস।

## কীভাবে ব্যবহার করবে
1. `ROADMAP.md` থেকে শেখার ক্রম ও আনুমানিক সময় দেখো।
2. প্রতিটি section-এর `README.md` পড়ে lesson ক্রমানুসারে শেষ করো।
3. Code নিজে চালাও, input বদলাও এবং অন্তত একটি নতুন test যোগ করো।
4. অনুশীলন আগে নিজে সমাধান করো, তারপর দেওয়া সমাধানের সঙ্গে মিলাও।
5. নিজের কাজ আলাদা repository-তে রাখো এবং প্রকল্পে README ও tests যোগ করো।

## বিষয়বস্তু
| অধ্যায় | বিষয় | পাঠ |
|---|---|---:|
| 00 | [Getting Started](00-getting-started/README.md) | 3 |
| 01 | [Computer Basics](01-computer-basics/README.md) | 4 |
| 02 | [Programming Fundamentals](02-programming-fundamentals/README.md) | 6 |
| 03 | [Web Development](03-web-development/README.md) | 5 |
| 04 | [Data Structures & Algorithms](04-data-structures-algorithms/README.md) | 8 |
| 05 | [Databases](05-databases/README.md) | 3 |
| 06 | [Networking](06-networking/README.md) | 3 |
| 07 | [Operating Systems](07-operating-systems/README.md) | 3 |
| 08 | [Software Engineering](08-software-engineering/README.md) | 3 |
| 09 | [AI & Machine Learning](09-ai-ml/README.md) | 3 |
| 10 | [Career](10-career/README.md) | 3 |

মোট **৪৪টি পাঠ**। এটি self-study curriculum; পূর্বশর্ত, অনুশীলন ও প্রকল্পের গভীরতার ওপর মোট সময় বদলাবে।

## Repository নীতি
- ব্যাখ্যা ও উদাহরণ বাংলায় মৌলিকভাবে লেখা; মূল technical term পাশে রাখা হয়েছে।
- উদাহরণ ছোট ও পুনরায় চালানোর উপযোগী; external service-নির্ভর উদাহরণে network/package লাগতে পারে।
- Security, accessibility, testing ও responsible data use-কে software কাজের অংশ হিসেবে দেখা হয়েছে।
- Code block-এ explanatory comment রাখা হয়নি; ব্যাখ্যা আলাদা prose-এ আছে।

## Contribution
ভুল ধরলে Bug Report template ব্যবহার করো। নতুন পাঠের প্রস্তাবে শেখার লক্ষ্য, বাংলা ব্যাখ্যা, runnable example এবং অন্তত তিনটি সমাধানসহ অনুশীলন উল্লেখ করো। `CONTRIBUTING.md` ও `CODE_OF_CONDUCT.md` পড়ো।

## Maintainer
**RA Fahim** — Web Developer & Creator · Full-stack · 1 year  
Dhaka, Bangladesh · [rafahim.com](https://rafahim.com) · [GitHub](https://github.com/rafahim) · [Email](mailto:dev@rafahim.com) · [Twitter/X](https://twitter.com/rafahimn) · [LinkedIn](https://linkedin.com/in/rafahimn)

## License
পাঠ্য কনটেন্ট **CC BY-SA 4.0** এবং code examples **MIT** লাইসেন্সের অধীনে। বিস্তারিত `LICENSE` ফাইলে।
''',
'ROADMAP.md': '''# শেখার Roadmap

এই সময়সূচি সপ্তাহে আনুমানিক ৬–১০ ঘণ্টা অনুশীলন ধরে তৈরি। নতুন শিক্ষার্থী কম সময় দিতে পারলে পথ দীর্ঘায়িত করতে পারবে। প্রতিটি অধ্যায় শেষে একটি ছোট deliverable তৈরি করো।

```mermaid
flowchart TD
    A[00 Getting Started - 1 সপ্তাহ] --> B[01 Computer Basics - 2 সপ্তাহ]
    B --> C[02 Programming Fundamentals - 4 সপ্তাহ]
    C --> D[03 Web Development - 4 সপ্তাহ]
    C --> E[04 Data Structures & Algorithms - 4 সপ্তাহ]
    D --> F[05 Databases - 2 সপ্তাহ]
    B --> G[06 Networking - 2 সপ্তাহ]
    B --> H[07 Operating Systems - 2 সপ্তাহ]
    E --> I[08 Software Engineering - 3 সপ্তাহ]
    F --> I
    G --> I
    H --> I
    I --> J[09 AI & Machine Learning - 2 সপ্তাহ]
    I --> K[10 Career - 2 সপ্তাহ]
    J --> K
```

## অধ্যায়ভিত্তিক পরিকল্পনা
| অধ্যায় | সময় | কাজের প্রমাণ |
|---|---:|---|
| 00 Getting Started | 1 সপ্তাহ | Git repository, algorithm note ও README |
| 01 Computer Basics | 2 সপ্তাহ | CPU/RAM/storage তুলনা এবং CLI practice |
| 02 Programming Fundamentals | 4 সপ্তাহ | validation-সহ CLI calculator বা expense summary |
| 03 Web Development | 4 সপ্তাহ | responsive semantic page ও public API data |
| 04 Data Structures & Algorithms | 4 সপ্তাহ | search/sort complexity note ও DP solution |
| 05 Databases | 2 সপ্তাহ | related tables, JOIN query, transaction demo |
| 06 Networking | 2 সপ্তাহ | DNS/TLS troubleshooting note ও HTTP request |
| 07 Operating Systems | 2 সপ্তাহ | shell workflow, permission ও process note |
| 08 Software Engineering | 3 সপ্তাহ | unit tests, CI workflow ও design decision note |
| 09 AI & Machine Learning | 2 সপ্তাহ | held-out test set-সহ model evaluation report |
| 10 Career | 2 সপ্তাহ | portfolio, project README ও CV draft |

## অধ্যায় শেষ করার মানদণ্ড
- মূল ধারণাটি বই না দেখে নিজের ভাষায় ব্যাখ্যা করতে পারো।
- practice solution-এর যুক্তি বোঝাও এবং অন্তত একটি variation নিজে সমাধান করো।
- Code হলে normal, boundary ও invalid input পরীক্ষা করো।
- Command বা external service ব্যবহার করলে risk, dependency ও limitation নোট করো।

সময় estimate planning aid, পরীক্ষা বা চাকরির নিশ্চয়তা নয়। শেখার গতি অনুযায়ী পরিবর্তন করো।
''',
'GLOSSARY.md': '''# বাংলা ↔ English Glossary

| বাংলা শব্দ/ব্যাখ্যা | English term | সহজ অর্থ |
|---|---|---|
| অ্যালগরিদম | Algorithm | সমস্যা সমাধানের ধাপ |
| হার্ডওয়্যার | Hardware | কম্পিউটারের স্পর্শযোগ্য অংশ |
| সফটওয়্যার | Software | program ও নির্দেশনার ব্যবস্থা |
| প্রসেসর | CPU / Processor | নির্দেশনা চালায় |
| অস্থায়ী মেমোরি | RAM | চলমান কাজের দ্রুত memory |
| স্থায়ী সংরক্ষণ | Storage | SSD/HDD-তে ফাইল রাখা |
| বিট | Bit | binary-র ০ বা ১ |
| বাইট | Byte | সাধারণত ৮ bit |
| অক্ষর এনকোডিং | Character Encoding | text-কে byte-এ প্রকাশের নিয়ম |
| অপারেটিং সিস্টেম | Operating System | hardware ও app পরিচালনা করে |
| কমান্ড লাইন | CLI | লিখিত command-এর interface |
| চলমান প্রোগ্রাম | Process | চালু program ও তার resource |
| থ্রেড | Thread | process-এর execution stream |
| ভেরিয়েবল | Variable | নাম দিয়ে মান ব্যবহার |
| ডেটার ধরন | Data Type | মানের ধরন ও operation নির্ধারণ |
| শর্ত | Condition | সত্য-মিথ্যার ওপর সিদ্ধান্ত |
| পুনরাবৃত্তি | Loop / Iteration | ধাপ বারবার চালানো |
| ফাংশন | Function | পুনর্ব্যবহারযোগ্য কাজের একক |
| পুনরাবৃত্ত ফাংশন | Recursion | function-এর নিজেকে call করা |
| পরামিতি | Parameter | function definition-এর input name |
| আর্গুমেন্ট | Argument | function call-এ পাঠানো মান |
| ফেরত মান | Return Value | function caller-কে দেয় যে ফল |
| তালিকা | Array / List | ordered item collection |
| সংযুক্ত তালিকা | Linked List | link-যুক্ত node-এর তালিকা |
| স্ট্যাক | Stack | LIFO structure |
| সারি | Queue | FIFO structure |
| গাছ | Tree | parent-child hierarchy |
| গ্রাফ | Graph | node ও edge-এর সম্পর্ক |
| হ্যাশ টেবিল | Hash Table | key-value lookup structure |
| সময় জটিলতা | Time Complexity | input বাড়লে কাজের প্রবণতা |
| স্থান জটিলতা | Space Complexity | algorithm-এর memory চাহিদা |
| সাজানো | Sorting | নির্দিষ্ট ক্রমে data রাখা |
| অনুসন্ধান | Searching | data-তে target খোঁজা |
| ডায়নামিক প্রোগ্রামিং | Dynamic Programming | subproblem-এর ফল reuse করা |
| মার্কআপ ভাষা | HTML | web content-এর কাঠামো |
| স্টাইল শিট | CSS | page presentation নির্ধারণ |
| জাভাস্ক্রিপ্ট | JavaScript | web interaction ও behavior |
| ডকুমেন্ট অবজেক্ট মডেল | DOM | HTML-এর programmatic representation |
| প্রোটোকল | Protocol | যোগাযোগের নিয়ম |
| অনুরোধ | Request | client থেকে server-এ বার্তা |
| প্রতিক্রিয়া | Response | server থেকে client-এ ফল |
| REST API | REST API | resource-ভিত্তিক HTTP interface |
| ডোমেইন নেম সিস্টেম | DNS | domain-এর network record lookup |
| ট্রান্সমিশন কন্ট্রোল প্রোটোকল | TCP | ordered reliable byte stream |
| ইন্টারনেট প্রোটোকল | IP | packet addressing ও routing |
| এনক্রিপশন | Encryption | key-নির্ভর গোপন রূপান্তর |
| TLS সার্টিফিকেট | TLS Certificate | server identity যাচাইয়ে ব্যবহৃত |
| রিলেশনাল ডেটাবেস | Relational Database | table-এ সম্পর্কযুক্ত data |
| প্রাইমারি কী | Primary Key | row-এর স্বতন্ত্র পরিচয় |
| ফরেন কী | Foreign Key | অন্য table-এর key reference |
| যোগসূত্র | JOIN | related table-এর row মেলানো |
| সূচি | Index | query-তে row খোঁজার সহায়ক কাঠামো |
| লেনদেন | Transaction | logical database কাজের unit |
| পরীক্ষা | Testing | আচরণ যাচাই |
| নিরবচ্ছিন্ন সংযোজন | Continuous Integration / CI | change-এর পর automated checks |
| নিরবচ্ছিন্ন বিতরণ | Continuous Delivery | release-ready pipeline |
| অবজেক্ট-ওরিয়েন্টেড | OOP | object/class-ভিত্তিক design |
| এনক্যাপসুলেশন | Encapsulation | internal state ও interface আলাদা |
| নকশা-প্যাটার্ন | Design Pattern | পুনরাবৃত্ত design problem-এর কৌশল |
| মেশিন লার্নিং | Machine Learning | data থেকে pattern শেখা |
| শ্রেণিবিন্যাস | Classification | category predict করা |
| রিগ্রেশন | Regression | numeric target predict করা |
| ক্লাস্টারিং | Clustering | unlabeled data-কে group করা |
| অতিরিক্ত মানিয়ে যাওয়া | Overfitting | training-এ ভালো, নতুন data-তে খারাপ |
| নির্ভুলতা | Precision | positive prediction-এ সত্য positive-এর হার |
| পুনরুদ্ধার হার | Recall | প্রকৃত positive-এর মধ্যে শনাক্ত positive-এর হার |
| সংস্করণ নিয়ন্ত্রণ | Version Control | পরিবর্তনের ইতিহাস রাখা |
| শাখা | Branch | আলাদা development line |
| কমিট | Commit | history-তে নির্দিষ্ট snapshot |
| Pull Request | Pull Request | change review/merge-এর প্রস্তাব |
| স্থাপন | Deployment | environment-এ software release |
| রিপোজিটরি | Repository | project files ও history |
''',
'CONTRIBUTING.md': '''# Contributing Guide

এই project-এ নির্ভুল, সহজপাঠ্য ও ব্যবহারযোগ্য বাংলা Computer Science পাঠ যোগ করতে অবদান স্বাগত। নতুন change ছোট ও উদ্দেশ্য-স্পষ্ট রাখো।

## Lesson checklist
- ব্যাখ্যা নিজের ভাষায় লেখো; ধার করা ধারণার জন্য source link দাও।
- শেখার লক্ষ্য, ব্যাখ্যা, বাস্তব analogy, runnable code, common mistakes, ৩–৫টি solved practice problem ও further reading রাখো।
- Code example-এ comment রেখো না; ব্যাখ্যা code block-এর বাইরে দাও। একান্ত দরকার হলে একটি ছোট comment ব্যবহার করা যায়।
- External package প্রয়োজন হলে dependency ও run instruction লিখো।
- প্রথম ব্যবহারে technical term-এর সঙ্গে বাংলা ব্যাখ্যা দাও।
- কোনো secret, private data বা অনুমতিহীন copyrighted material যোগ কোরো না।

## Workflow
1. Fork করে ছোট feature branch তৈরি করো।
2. Change-এর scope স্পষ্ট রাখো এবং Markdown links/code fences পরীক্ষা করো।
3. Code example নিজে চালাও অথবা limitation উল্লেখ করো।
4. Pull request template পূরণ করে summary, tests ও context দাও।

সহজ ও সম্মানজনক বাংলা ব্যবহার করো; disagreement-এ ব্যক্তিকে নয়, যুক্তি ও evidence-কে কেন্দ্র করো।
''',
'CODE_OF_CONDUCT.md': '''# Code of Conduct

## অঙ্গীকার
এখানে সবার জন্য সম্মানজনক, সহায়ক ও শিক্ষামূলক পরিবেশ বজায় রাখা হবে—অভিজ্ঞতা, ভাষা, লিঙ্গ, ধর্ম, জাতীয়তা, অক্ষমতা বা পরিচয় নির্বিশেষে।

## প্রত্যাশিত আচরণ
- ভদ্র ও গঠনমূলক ভাষায় কথা বলা এবং নতুন শিক্ষার্থীর প্রশ্নকে গুরুত্ব দেওয়া।
- সমালোচনা code, idea বা behavior-কে কেন্দ্র করে করা; ব্যক্তিগত আক্রমণ নয়।
- অন্যের অবদান, privacy ও license সম্মান করা।
- হয়রানি, হুমকি, targeted insult, doxxing বা unwanted contact থেকে বিরত থাকা।

## প্রয়োগ
সমস্যা জানাতে `dev@rafahim.com`-এ যোগাযোগ করা যায়। প্রয়োজনীয় context দাও, অপ্রয়োজনীয় ব্যক্তিগত তথ্য নয়। Maintainer পরিস্থিতি পর্যালোচনা করে সতর্কতা, content removal, temporary restriction বা অংশগ্রহণ বন্ধ করার ব্যবস্থা নিতে পারেন। রিপোর্টের গোপনীয়তা যথাসম্ভব রক্ষা করা হবে।
''',
'LICENSE': '''# Dual License

Copyright (c) 2026 RA Fahim and contributors.

## Written content
Explanatory prose, lesson text, roadmap, glossary, and other written educational content are licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. You may share and adapt it, including commercially, if you provide attribution, link the license, indicate changes, and share adaptations under the same license. Do not imply endorsement by the maintainers.

Full license: https://creativecommons.org/licenses/by-sa/4.0/legalcode

## Code examples
Code snippets are licensed under the **MIT License**:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
''',
'.gitignore': '''__pycache__/
*.py[cod]
.env
.env.*
!.env.example
.venv/
venv/
.DS_Store
Thumbs.db
.idea/
.vscode/
*.log
''',
'humans.txt': '''/* TEAM */
Maintainer: RA Fahim
Role: Web Developer & Creator
Focus: Full-stack development and educational content
Experience: 1 year
Location: Dhaka, Bangladesh
Website: https://rafahim.com
GitHub: https://github.com/rafahim
Email: dev@rafahim.com
Twitter/X: https://twitter.com/rafahimn
LinkedIn: https://linkedin.com/in/rafahimn

/* THANKS */
Thanks to learners, reviewers, and open documentation communities helping make computing education accessible in Bengali.
''',
'.well-known/security.txt': '''Contact: mailto:dev@rafahim.com
Expires: 2027-10-09T23:59:59.000Z
Preferred-Languages: bn, en
Canonical: https://rafahim.com/.well-known/security.txt
Policy: https://rafahim.com/security
''',
'.github/ISSUE_TEMPLATE/bug_report.md': '''---
name: Bug report
about: পাঠ বা code example-এর ভুল জানাও
title: "[BUG] "
labels: bug
assignees: ''
---

## কোন ফাইলে সমস্যা?
ফাইলের path ও heading লেখো।

## কী সমস্যা হয়েছে?
ভুল ব্যাখ্যা, broken link, typo বা code error বর্ণনা করো।

## প্রত্যাশিত ফল
সঠিক আচরণ বা ব্যাখ্যা কী হওয়া উচিত?

## পুনরুৎপাদনের ধাপ
1. কোন section/উদাহরণ খুলেছ লিখো।
2. Code হলে command, language/version ও input দাও।
3. Error বা output দাও।

## প্রমাণ
ব্যক্তিগত তথ্য/secret বাদ দিয়ে error, screenshot বা reference যোগ করো।
''',
'.github/ISSUE_TEMPLATE/new_lesson.md': '''---
name: New lesson proposal
about: নতুন পূর্ণাঙ্গ বাংলা পাঠ প্রস্তাব করো
title: "[LESSON] "
labels: content, enhancement
assignees: ''
---

## প্রস্তাবিত বিষয়
নতুন পাঠের শিরোনাম ও section লিখো।

## কেন দরকার?
কোন learning gap বা objective পূরণ করবে?

## শেখার লক্ষ্য
পাঠ শেষে কী ব্যাখ্যা, তৈরি বা পরীক্ষা করা যাবে?

## পরিকল্পিত উদাহরণ
Runnable example ও environment লিখো।

## অনুশীলন
কমপক্ষে ৩টি প্রশ্ন ও solution plan দাও।

## উৎস
বিশ্বস্ত documentation/specification-এর link দাও। কপি করা লেখা জমা দিও না।
''',
'.github/PULL_REQUEST_TEMPLATE.md': '''## পরিবর্তনের সারাংশ
কী বদলেছে এবং কেন?

## ধরন
- [ ] Typo/ভাষা সংশোধন
- [ ] Lesson content
- [ ] Code example
- [ ] Roadmap/glossary/documentation
- [ ] Bug fix

## যাচাই
- [ ] Markdown heading ও links পরীক্ষা করেছি
- [ ] Code example চালিয়েছি অথবা limitation উল্লেখ করেছি
- [ ] Lesson-এ ৩–৫টি solved practice problem রয়েছে
- [ ] Code sample-এ explanatory comment নেই
- [ ] Secret বা ব্যক্তিগত তথ্য নেই
- [ ] Contribution guide অনুসরণ করেছি

## অতিরিক্ত তথ্য
Reviewer-এর প্রয়োজনীয় context, test result বা screenshot দাও।
'''
}

def lesson_markdown(x):
    goals = [f"{x['title']} সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা", 'একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা', 'সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা']
    lines = [f"# {x['title']}", '', '## এই পাঠ শেষে', '']
    lines += [f'- {g}' for g in goals]
    lines += ['', '## ধারণা ও ব্যাখ্যা', '', x['explanation'], '', '## বাস্তব জীবনের উপমা', '', x['analogy'], '', '## মূল বিষয়', '']
    lines += [f'- {c}' for c in x['concepts']]
    lines += ['', '## Code example', '', f"```{x['language']}", x['code'], '```', '', 'উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।', '', '## সাধারণ ভুল', '']
    lines += [f'- {m}' for m in x['mistakes']]
    lines += ['', '## অনুশীলন ও সমাধান', '']
    for i, pair in enumerate(x['exercises'], 1):
        lines += [f'### সমস্যা {i}', pair[0], '', '**সমাধান:** ' + pair[1], '']
    lines += ['## আরও পড়ো', '']
    lines += [f'- [{u}]({u})' for u in x['reading']]
    lines += ['', '---', '', '[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)', '']
    return '\n'.join(lines)

def write_all():
    for rel, body in ROOT_FILES.items():
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body.rstrip() + '\n', encoding='utf-8')
    for section, (heading, description, notes) in SECTIONS.items():
        subset = [x for x in LESSONS if x['section'] == section]
        lines = [f'# {heading}', '', description, '', notes, '', '## পাঠক্রম', '']
        lines += [f"- [{x['title']}]({x['slug']}.md)" for x in subset]
        lines += ['', '## শেখার পদ্ধতি', 'প্রতিটি পাঠে আগে ব্যাখ্যা পড়ো, এরপর code চালাও, common mistakes মিলিয়ে দেখো এবং solutions না দেখে অনুশীলনের চেষ্টা করো। কোনো শব্দ অস্পষ্ট হলে `GLOSSARY.md` দেখো।', '']
        p = ROOT / section / 'README.md'
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text('\n'.join(lines), encoding='utf-8')
    for x in LESSONS:
        p = ROOT / x['section'] / (x['slug'] + '.md')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(lesson_markdown(x), encoding='utf-8')
    (ROOT / 'setup.sh').chmod(0o755)

def zip_repo():
    out = ROOT.parent / 'bangla-cs-roadmap.zip'
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted(ROOT.rglob('*')):
            if p.is_file() and '.git' not in p.parts and p.name != 'ALL_FILES.txt':
                z.write(p, Path(ROOT.name) / p.relative_to(ROOT))
    return out

if __name__ == '__main__':
    write_all()
    out = zip_repo()
    print(f'Lessons: {len(LESSONS)}')
    print(f'Files listed in manifest: {len(ROOT_FILES) + 1 + len(SECTIONS) + len(LESSONS)}')
    print(f'ZIP: {out}')
