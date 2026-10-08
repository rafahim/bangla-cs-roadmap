# Git ও GitHub-এর ভিত্তি

## এই পাঠ শেষে

- Git ও GitHub-এর ভিত্তি সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Git হলো version control system; এটি file-এর পরিবর্তন, author ও project-এর আগের অবস্থার ইতিহাস রাখে। গুরুত্বপূর্ণ অবস্থার snapshot-কে commit বলে। ভুল হলে পুরোনো সংস্করণ দেখা যায়, আলাদা branch-এ কাজ করা যায় এবং পরে merge করা যায়। Git স্থানীয় কম্পিউটারেই কাজ করে; online account দরকার হয় না।

GitHub হলো Git repository রাখা ও সহযোগিতার platform। `push` পরিবর্তন remote-এ পাঠায়; `fetch` বা `pull` অন্যদের update আনে। README project ব্যাখ্যা করে, issue কাজ বা bug নথিবদ্ধ করে, pull request change review করার সুযোগ দেয়। Password, API key বা ব্যক্তিগত তথ্য repository-তে commit করা উচিত নয়।

## বাস্তব জীবনের উপমা

Document version history-র মতো: commit bookmark, branch আলাদা খসড়া আর merge খসড়াগুলো এক করা।

## মূল বিষয়

- Repository হলো history-সহ file collection।
- Commit একটি নির্দিষ্ট snapshot।
- Branch আলাদা line of development।
- Remote অন্য computer বা hosting platform-এ থাকা repository।

## Code example

```bash
git init
git add README.md
git commit -m "Add project introduction"
git branch -M main
git remote add origin https://github.com/rafahim/example-repo.git
git push -u origin main
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- পরিবর্তন না বুঝে সব file stage করা; আগে `git status` দেখো।
- Commit message-এ শুধু `update` লেখা।
- Secret commit করা; প্রকাশ পেলে key revoke/rotate করো।

## অনুশীলন ও সমাধান

### সমস্যা 1
ফাইল বদলানোর আগে কোন command চালাবে?

**সমাধান:** `git status` working tree, staged files ও branch দেখায়।

### সমস্যা 2
`git add` আর `git commit`-এর পার্থক্য কী?

**সমাধান:** `git add` change stage করে; `git commit` staged snapshot history-তে যোগ করে।

### সমস্যা 3
পুরোনো commit-এর বিস্তারিত কীভাবে দেখবে?

**সমাধান:** `git log --oneline` দিয়ে history দেখো, তারপর `git show <commit>` চালাও।

## আরও পড়ো

- [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
- [https://docs.github.com/en/get-started/using-git/about-git](https://docs.github.com/en/get-started/using-git/about-git)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
