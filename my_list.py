# 1. Create an empty list
my_list = []
print("After creating empty list:", my_list)

# 2. Append elements 10, 20, 30, 40
my_list.append(10)
print("After appending 10:", my_list)
my_list.append(20)
print("After appending 20:", my_list)
my_list.append(30)
print("After appending 30:", my_list)
my_list.append(40)
print("After appending 40:", my_list)

# 3. Insert the value 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# 4. Extend the list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# 5. Remove the last element from the list
my_list.pop()
print("After removing the last element:", my_list)

# 6. Sort the list in ascending order
my_list.sort()
print("After sorting the list:", my_list)

# 7. Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
