# Linux Shell, Path ও Permissions

## এই পাঠ শেষে

- Linux Shell, Path ও Permissions সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Linux shell-এ command, argument ও pipe দিয়ে ছোট tool একত্র করা যায়। `grep` text খোঁজে, `sort` সাজায়, `wc` গণনা করে; pipe `|` এক command-এর output পরের command-এ পাঠায়। Unix file permission-এ owner, group ও others-এর read/write/execute অধিকার থাকে। `chmod` permission বদলায়; `sudo` elevated privilege-এ command চালাতে পারে, তাই অপ্রয়োজনে ব্যবহার করা উচিত নয়।

Environment variable process-কে configuration দেয়; `PATH` executable খোঁজার directory জানায়। Script-এ absolute path ধরে নিলে অন্য machine-এ নাও চলতে পারে। Shell-এ spaces, wildcard ও quoting গুরুত্বপূর্ণ। User input দিয়ে shell command string তৈরি করা ঝুঁকিপূর্ণ; argument list ও নিরাপদ API ব্যবহার করো।

## বাস্তব জীবনের উপমা

Toolbox-এর ছোট tool জুড়ে কাজ করার মতো; একটি tool output দেয়, pipe তা পরের tool-এ পাঠায়।

## মূল বিষয়

- Pipe output-কে পরের command-এর input করে।
- Permission least privilege অনুসারে সীমিত রাখো।
- Environment variable configuration ও executable search-এ ব্যবহৃত হয়।

## Code example

```bash
printf 'delta\nalpha\nbeta\n' > names.txt
sort names.txt | grep 'a'
wc -l names.txt
chmod u+x names.txt
printf '%s\n' "$PATH"
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- সব ক্ষেত্রে `sudo` ব্যবহার করা।
- Permission 777 করে সমস্যা ঢেকে রাখা।
- Space-যুক্ত filename quote না করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
`sort names.txt | grep 'a'` কী করে?

**সমাধান:** Line sort করে, তারপর `a` থাকা line filter করে।

### সমস্যা 2
`chmod u+x file` কী করে?

**সমাধান:** Owner-এর execute permission যোগ করে।

### সমস্যা 3
`PATH` কেন দরকার?

**সমাধান:** Shell executable command কোন directory-তে খুঁজবে তা জানায়।

## আরও পড়ো

- [https://ubuntu.com/tutorials/command-line-for-beginners](https://ubuntu.com/tutorials/command-line-for-beginners)
- [https://www.gnu.org/software/bash/manual/bash.html](https://www.gnu.org/software/bash/manual/bash.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
