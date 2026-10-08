# দলগত কাজ, Code Review ও Git Workflow

## এই পাঠ শেষে

- দলগত কাজ, Code Review ও Git Workflow সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Team software development-এ ছোট change, পরিষ্কার commit, issue link ও review history বোঝা সহজ করে। Feature branch-এ focused কাজ করে pull request করলে reviewer উদ্দেশ্য, test result ও risk দেখতে পারেন। Review ব্যক্তিকে নয়, code-এর behavior ও maintainability-কে কেন্দ্র করে হওয়া উচিত। মতভেদ হলে requirement, reproducible example ও trade-off দিয়ে আলোচনা করো।

Issue-তে expected/actual behavior, reproduction step ও environment লিখলে debugging সহজ হয়। Merge-এর আগে conflict, tests ও secret exposure যাচাই করো। ছোট pull request দ্রুত review করা যায়; unrelated formatting change একসঙ্গে মেশালে মূল পরিবর্তন বোঝা কঠিন হয়।

## বাস্তব জীবনের উপমা

একসঙ্গে বই সম্পাদনার মতো: আলাদা অংশে কাজ, reviewer-দের feedback, এরপর পরিবর্তন একত্রে প্রকাশ।

## মূল বিষয়

- Issue bug-কে reproducible context দেয়।
- Pull request code review ও merge-এর প্রস্তাব।
- Small focused change review burden কমায়।

## Code example

```bash
git switch -c feature/add-search
git status
git add src/search.js
git commit -m "Add search filtering"
git push -u origin feature/add-search
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- এক branch-এ unrelated feature মেশানো।
- Review feedback-কে ব্যক্তিগত আক্রমণ মনে করা।
- Deploy configuration পরীক্ষা না করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Bug report-এ কী থাকবে?

**সমাধান:** Expected/actual result, reproduction steps, environment এবং sanitized error/log।

### সমস্যা 2
Small pull request review করা সহজ কেন?

**সমাধান:** কম context switching-এ reviewer scope ও risk বুঝতে পারেন।

### সমস্যা 3
Commit message নির্দিষ্ট হওয়া কেন ভালো?

**সমাধান:** History থেকে কী behavior বদলেছে দ্রুত বোঝা যায়।

## আরও পড়ো

- [https://docs.github.com/en/pull-requests/collaborating-with-pull-requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
- [https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
