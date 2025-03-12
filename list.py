# Create an empty list
my_list = []

# Add elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert an element 15 at the second position
my_list.insert(1, 15)

# Extend the list with additional elements
my_list.extend([50, 60, 70])

# Remove the last element from the list
my_list.remove(70)

# Sort the list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print(index_of_30)

# Print the updated list
print(my_list)
