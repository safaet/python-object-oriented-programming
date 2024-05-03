a = [7, 3, 6, 8, 2, 3, 7, 2, 6, 3, 6]
b = a
c = b
b = c
 
def remove_elem(data, target):
    elem = data[:]
    for item in elem:
        if item == target:
            elem.remove(target)
    return elem
 
def get_product(data):
    total = 1
    for i in range(len(data)):
        total *= data[i]
    return total
 
 
print(a) 
print(remove_elem(c, 3))
print(a)
print(get_product(b))
print(a)