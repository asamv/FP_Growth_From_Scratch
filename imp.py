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
import pandas as pd
from fp_tree import FP_Tree

df = pd.read_excel("transactions.xlsx")
print(df)

transactions = df["Items"].tolist()
transactions = list(t.split(',') for t in transactions) [:10]  # Limiter à 10 transactions pour l'exemple
print(transactions)
""""
transactions = [
["banane", "ananas", "pomme"],
["ananas", "banane"],
["ananas", "cacaou", "pomme"],
["banane", "cacaou"],
["ananas", "banane", "pomme", "kiwi"],
["banane", "pomme", "kiwi"],
["ananas", "kiwi", "frais"],
["banane", "cacaou", "kiwi"],
["ananas", "banane", "cacaou", "kiwi","pasteque"],
["banane", "pomme", "frais"],
["ananas", "pomme", "kiwi","frais"],
["banane", "ananas", "kiwi","frais","pasteque"],
]
"""

fp_tree = FP_Tree() 

fp_tree.add_transactions(transactions)
fp_tree.display()
fp_tree.visualize()
