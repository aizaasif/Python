# Grocery billing system

dict={}
# 1st item
items1_name=input("Enter the name of 1st item: ")
items1_price=int(input("Enter the price of 1st item: "))
dict.update({items1_name:items1_price})
# 2nd item
items2_name=input("Enter the name of 2nd item: ")
items2_price=int(input("Enter the price of 2nd item: "))
dict.update({items2_name:items2_price})
# 3rd item
items3_name=input("Enter the name of 3rd item: ")
items3_price=int(input("Enter the price of 3rd item: "))
dict.update({items3_name:items3_price})

# item names in a single line seprated by commas
print("The names of available items are : ",tuple(dict))

# Ask the user to input an item name to check its availability
useritem=input("Enter any item name : ")
if useritem in dict:
    print("Item Found and the prize of item is : ",dict[useritem])
else:
    print("Item not Found")

# Create a tuple of all item prices and print the total bill (sum of all prices).
prices=tuple(dict.values())
print("Tuple of all item prices is : ",prices)
total=sum(prices)
print("The sum of all prices are : ",total)

# Find and display the most expensive and the cheapest item price 
expensive_item=max(prices)
print("The most expensive item price is : ",expensive_item)
cheapest_item=min(prices)
print("The most cheapest item price is : ",cheapest_item)

# Converting list of items in a set
print(dict)
item_set=set(dict.items())
print("The list of all items in the form of a set are : ",item_set)

print("The first 3 chs of 1st itemname",items1_name[0:3])
print("The first 3 chs of 2nd itemname",items2_name[0:3])
print("The first 3 chs of 3rd itemname",items3_name[0:3])

if max(prices)>500:
    print("Premimum Item availble in the store")
else:
    print("No premimum item available")