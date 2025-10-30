
from fp_tree import FP_Tree

import json

with open("data.json", "r") as file:
    transactions = json.load(file)


fp_tree = FP_Tree() 

fp_tree.add_transactions(transactions)
fp_tree.display()
fp_tree.visualize()