# 1 tapsyrma
# Create an empty tuple
tpl = ()

# 2 tapsyrma
# Create a tuple containing names of your sisters and your brothers
sister = ('guljupar', 'aqmeruert','marfuza')
brother = ('sagymjan', 'qydyrali')
 
# 3tapsyrma
#Join brothers and sisters tuples and assign it to siblings
siblings = (brother + sister)

# 4 tapsyrma
#How many siblings do you have?
nume_siblings = len(siblings)

# 5 tapsyrma
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = ('Father', 'Mother') + siblings

# 6 tapsyrma
# Unpack siblings and parents from family_members
parents = family_members[:2]
siblings = family_members[2:]

# 7 tapsyrma
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'lettuce', 'broccoli')
animal_products = ('milk', 'eggs', 'cheese')
food_stuff_tp = fruits+vegetables + animal_products

# 8 tapsyrma
# Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt= list(food_stuff_tp)

# 9 tapsyrma
#slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp [len(food_stuff_tp)//2]
middle_items = food_stuff_lt [len(food_stuff_lt)//2-1:len(food_stuff_lt)//2+1]

# 10 tapsyrma
#Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]


# 11 tapsyrma
# Delete the food_staff_tp tuple completely
del food_stuff_tp

# 12 tapsyrma
# Check if an item exists in tuple
juis = ('apple', 'alma', 'banan', 'shery')
is_estonia_nordic = 'apple' in juis
is_iceland_nordic = 'klubnika' in juis
