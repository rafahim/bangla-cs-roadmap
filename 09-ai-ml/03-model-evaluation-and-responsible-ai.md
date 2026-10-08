# Model Evaluation ও Responsible AI

## এই পাঠ শেষে

- Model Evaluation ও Responsible AI সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Model evaluation metric-কে বাস্তব সিদ্ধান্তের সঙ্গে যুক্ত করতে হয়। Accuracy মোট সঠিক prediction-এর অনুপাত; precision positive prediction-এর মধ্যে সত্য positive-এর হার; recall প্রকৃত positive-এর কত অংশ শনাক্ত হয়েছে তা জানায়। False positive ও false negative-এর cost এক নয়, তাই fraud, medical triage ও spam-এ metric নির্বাচন আলাদা হতে পারে। Confusion matrix error type দেখায়।

Responsible AI-তে privacy, consent, fairness, explainability, safety ও accountability বিবেচনা করা হয়। Dataset-এ কোনো group কম represented হলে performance gap হতে পারে। Sensitive data minimization, access control, retention policy ও audit trail জরুরি। Production input distribution বদলালে model drift হয়; তাই monitoring, feedback এবং rollback/update plan দরকার।

## বাস্তব জীবনের উপমা

পরীক্ষার মোট নম্বরের পাশাপাশি কোন ধরনের প্রশ্নে ভুল হয়েছে তা দেখার মতো। এক metric দিয়ে model বিচার করলে গুরুত্বপূর্ণ ঝুঁকি আড়াল হতে পারে।

## মূল বিষয়

- Precision ও recall আলাদা প্রশ্নের উত্তর দেয়।
- Fairness শুধু এক metric দিয়ে পুরো বোঝা যায় না।
- Deployment-এর পর monitoring ও governance দরকার।

## Code example

```python
from sklearn.metrics import classification_report, confusion_matrix
y_true = [1, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 0, 1, 1]
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, zero_division=0))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- শুধু accuracy দেখে false negative উপেক্ষা করা।
- Personal data ব্যবহারের legal/ethical basis উপেক্ষা করা।
- Model deploy করে monitoring বন্ধ করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Precision কম হলে কী ইঙ্গিত হতে পারে?

**সমাধান:** Positive prediction-এর মধ্যে false positive বেশি হতে পারে।

### সমস্যা 2
Recall বাড়াতে কী trade-off হতে পারে?

**সমাধান:** Positive বেশি ধরতে false positive বাড়তে পারে।

### সমস্যা 3
Model drift কী?

**সমাধান:** Production data বা input-target relation বদলে performance কমে যাওয়া।

## আরও পড়ো

- [https://scikit-learn.org/stable/modules/model_evaluation.html](https://scikit-learn.org/stable/modules/model_evaluation.html)
- [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
