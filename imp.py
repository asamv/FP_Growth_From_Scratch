"""from fp_tree import FP_Tree

fp = FP_Tree()
transactions = [
        ["a", "b", "c"],
        ["a", "b"],
        ["a", "c", "d"],
        ["b", "c"]
    ]

for t in transactions:
    fp.add_transaction(t)

fp.display()
fp.display_header_table()"""
# imp.py

from fp_tree import FP_Tree

transactions = [
["banana", "ananas", "pomme"],
["a", "banana"],
["a", "c", "d"],
["banana", "c"],
["a", "banana", "d", "e"],
["banana", "d", "e"],
["a", "e", "f"],
["b", "c", "e"],
["a", "banana", "c", "e","kakaweyyyaaa"]
]

fp_tree = FP_Tree() 

fp_tree.add_transactions(transactions)
fp_tree.display()
fp_tree.visualize()