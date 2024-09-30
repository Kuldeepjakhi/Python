#!/usr/bin/python3

old_list = ['10','20','30','40']

new_list = old_list
print(old_list)
print(new_list)

# Now add new item in new_list and check if old_list get changed

new_list.append('50')
print(new_list)
print(old_list)

# The value of old_list will also changed because both the list is pointing to same reference ID.
# So List is Mutable.


"""
OutPut
['10', '20', '30', '40']
['10', '20', '30', '40']
['10', '20', '30', '40', '50']
['10', '20', '30', '40', '50']
"""