"""
# 1).Write a Python program to combine values in python list of dictionaries. 
                Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 
                                                                                            300}, o {'item': 'item1', 'amount': 750}] 
                            Expected Output:
                                            Counter ({'item1': 1150, 'item2': 300}) 

"""

from collections import Counter

item_list = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
result = Counter()
for dict in item_list:
    result[dict['item']] += dict['amount']
print(result) 

# Second example using loop and conditional statements :

a = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]    
cp = {}
val = 0
for dict in a:
    if dict['item'] not in cp:
        cp[dict['item']] = dict['amount']
    else:
        cp[dict['item']] += dict['amount'] 
print(cp) 