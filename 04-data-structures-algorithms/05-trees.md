# Trees: hierarchy ও traversal

## এই পাঠ শেষে

- Trees: hierarchy ও traversal সম্পর্কে মূল ধারণা নিজের ভাষায় ব্যাখ্যা করতে পারা
- একটি ব্যবহারিক উদাহরণে ধারণাটি প্রয়োগ করতে পারা
- সাধারণ ভুল শনাক্ত করে input বা পরিস্থিতি বদলে পরীক্ষা করা

## ধারণা ও ব্যাখ্যা

Tree এমন hierarchical structure যেখানে node parent-child সম্পর্কে যুক্ত। Root শীর্ষ node, leaf child-হীন node, subtree কোনো node ও তার descendants। Binary tree-তে প্রতি node-এর সর্বোচ্চ দুই child থাকে। Binary search tree-তে সাধারণ convention অনুযায়ী বাম দিকে ছোট, ডানে বড় মান রাখা হয়; duplicate value-এর নীতি implementation অনুযায়ী আলাদা হতে পারে।

Traversal-এর ক্রম আলাদা: preorder-এ node আগে, inorder-এ left-node-right, postorder-এ children-এর পরে node। Balanced BST-তে search/insert `O(log n)` হতে পারে; tree একদিকে বাঁকা হলে `O(n)` হয়। Folder, menu ও organization chart-এর মতো parent-child data-তে tree উপযোগী।

## বাস্তব জীবনের উপমা

Folder-এর ভেতরে subfolder-এর hierarchy ভাবো। Root থেকে শাখা বের হয়, আর leaf শেষ প্রান্তের item।

## মূল বিষয়

- Root, parent, child, leaf, height ও depth।
- Traversal নির্দিষ্ট ক্রমে node পরিদর্শন করে।
- BST-এর speed balance-এর ওপর নির্ভর করে।

## Code example

```python
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right)

root = Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
print(inorder(root))
```

উদাহরণটি নিজে চালাও। ফল প্রত্যাশার মতো না হলে input, environment ও error message যাচাই করো; code line ধরে execution অনুসরণ করো।

## সাধারণ ভুল

- BST সবসময় balanced ধরে নেওয়া।
- Recursive traversal-এ base case বাদ দেওয়া।
- Tree-র structure না বুঝে child pointer update করা।

## অনুশীলন ও সমাধান

### সমস্যা 1
Root ৪, left ২, right ৬ হলে inorder output কী?

**সমাধান:** `[2, 4, 6]`।

### সমস্যা 2
Child-হীন node-কে কী বলে?

**সমাধান:** Leaf node।

### সমস্যা 3
Skewed BST-তে worst-case search কী?

**সমাধান:** `O(n)`।

## আরও পড়ো

- [https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BST.html](https://opendsa-server.cs.vt.edu/ODSA/Books/Everything/html/BST.html)
- [https://visualgo.net/en/bst](https://visualgo.net/en/bst)

---

[এই অধ্যায়ের পাঠক্রমে ফিরে যাও](README.md)
