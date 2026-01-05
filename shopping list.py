shopping_list=["milk","eggs","cake","chicken","fruits","spam"]

for items in shopping_list:
  if items =="milk":
    continue 
  print("buy"+" "+items)

shopping_list=["milk","eggs","cake","chicken","fruits","spam"]

items_to_find="eggs"
found_at= None
for index in range(len(shopping_list)):
    if shopping_list[index]== items_to_find:
     found_at=index
print('items will be found at{0}'.format(found_at))
 
shopping_list=["milk","eggs","cake","chicken","fruits","spam"]
items_to_find="cake"
found_at=None 

for index in range(len(shopping_list)):
  if shopping_list[index]==items_to_find:
    found_at=index
print('item will be found at {}'.format(found_at))





shopping_list=["milk","eggs","cake","chicken","fruits","spam"]
items_to_find="chicken"
found_at="None"

for index in range(len(shopping_list)):
  if shopping_list[index]==items_to_find:
    found_at=index
print('it will be found at {0}'.format(found_at))
