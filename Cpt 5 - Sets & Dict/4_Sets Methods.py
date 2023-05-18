a=set()
print(type(a))

a.add(1)
a.add(1) # Adding a value repeatedly does not changes a set
a.add(2)
a.add(5)
a.add((4, 5, 6))
# a.add({4:5}) # Cannot add list or dictionary to sets
print(a)

# Removal of an Item 
a.remove(5) # Removes 5 fromt set a
# a.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(a)

## Length of the Set
print(len(a)) # Prints the length of this set

a={1,2,3,456,566}
a.pop() # Removes an arbitary element from the set
print(a)

# a.clear() #  Removes the set a
# print(a)


# (Clg) to print only the unique elements of a list 
l1=[1,1,1,2,2,2,3,3,3]
set(l1)
print(set(l1))

sam_set={"Yellow","Red","Green"}
sam_list=["Black","Orange"]
sam_set.update(sam_list) # wont add the elements which are already present in the set.
# or
# sam_set.add(sam_list[0])
# sam_set.add(sam_list[1])
print(sam_set)

set1={10,20,30,40,50}
set2={30,40,50,60,70}
set3=set1.intersection(set2) # only the values common in both the lists
print(set3)
# or
# print(set1 & set2)

set1={10,20,30,40,50}
set1.difference_update({10,20,30}) # removes 10,20,30 from the set
print(set1)

set1={10,20,30}
set2={30,40,50}
print(set1.isdisjoint(set2)) #isdisjoint() method returns True if two sets are disjoint sets. If not, then False.

odd={1,3,5,7,9,11}
prime={2,3,5,7,11}
print(odd | prime) # | = union of sets
print(odd & prime) # & = intersection of sets
print(odd - prime) # - = set difference
print(odd ^ prime) # ^ = exclusive (elements which are present in exactly one of the sets)