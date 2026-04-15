def add_item(item, lst =[]):
    lst.append(item)
    return lst

add_item(1)
add_item(2)
result = add_item(3,[])

print(len(result) + len(add_item(4)))
print(add_item(5))