# Sort
a=[1,99,24,56,2,5]
print(a)
a.sort()
print(a)

# sorting by 2nd element
import operator
my_list = [ ('John', 40), ('Dana', 35), ('Betty', 10), ('Robby', 8), ('John', 20) ]
my_list.sort(key = operator.itemgetter(1))
print(my_list)
#The output is
#[('Robby', 8), ('Betty', 10), ('John', 20), ('Dana', 35), ('John', 40)]

b=[1,3,56,100,45,23,40]
# b.reverse() # reverses the list
# b.append(101) # adds 101 at the end of the list 
# b.insert(4,109) # inserts 109 at index 4
# b.pop(3) # removes element at index 3
# b.remove(100) # removes 100 from the list
# b.extend(a) # adds list a to the end of b in an unordered way.
print(b)

l1=[1,1,1,2,2,2,3,3,3]
del l1[1]
l1.remove(2)
print(l1)
l1.pop(2)
# for del - specify index no. ; for remove - specify element