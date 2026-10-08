# Supervised ও Unsupervised Learning

## এই পাঠ শেষে

- Supervised ও Unsupervised Learning সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Supervised learning-এ input-এর সঙ্গে label থাকে। Regression numerical value predict করে, যেমন বিক্রির পরিমাণ; classification category predict করে, যেমন spam/non-spam। Complexity বাড়ালে training performance ভালো হলেও unseen data-তে খারাপ হতে পারে—এটি overfitting। Validation set ও baseline ব্যবহার করে model নির্বাচন করো।

Unsupervised learning label ছাড়া data-র structure খোঁজে। Clustering similar example group করে, dimensionality reduction representation ছোট করে। Cluster মানেই বাস্তব শ্রেণি নয়; domain context দিয়ে ব্যাখ্যা দরকার। Feature scale, missing value, leakage ও class imbalance result প্রভাবিত করে।

## বাস্তব জীবনের উপমা

উত্তরসহ অনুশীলনপত্র supervised learning-এর মতো; উত্তর ছাড়া অনেক খাতায় pattern খোঁজা unsupervised learning-এর কাছাকাছি।

## মূল বিষয়

- Classification category/label predict করে।
- Regression numeric target predict করে।
- Clustering label ছাড়াই similarity-ভিত্তিক group খোঁজে।

## Code example

```python
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- Test result দেখে বারবার hyperparameter tune করা।
- Accuracy একাই imbalance বোঝায় ধরে নেওয়া।
- Clustering-কে নিশ্চিত বাস্তব category ধরা।

## অনুশীলন ও সমাধান

### সমস্যা 1
ইমেইল spam কি না বলা কোন task?

**সমাধান:** Classification।

### সমস্যা 2
আগামী মাসের বিক্রি অনুমান কোন task?

**সমাধান:** Regression।

### সমস্যা 3
Label নেই এমন customer-দের আচরণ অনুযায়ী group করা কোন approach?

**সমাধান:** Unsupervised clustering।

## আরও পড়ো

- [https://scikit-learn.org/stable/supervised_learning.html](https://scikit-learn.org/stable/supervised_learning.html)
- [https://scikit-learn.org/stable/unsupervised_learning.html](https://scikit-learn.org/stable/unsupervised_learning.html)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
