
# definition
nums = {1, 2, 3, 4, 5, 6}
nums2 = set((1, 2, 3, 4,))

print(nums)
print(nums2)
print(type(nums))
print(len(nums2))


# No duplicate allowed
nums = {1, 2, 2, 4}
print(nums)


# True is a dupe of 1, and False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# check if a value is in set
print(2 in nums)
# you can't refer to an element using an index or a key

# adding a new value
nums.add(8)
print(nums)


# add elements from one set to another
morenums = {9, 16, 5}
nums.update(morenums)

print(nums)

# the .update() can be used with lists, tuples and dictionaries too


# merge 2 sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}
new_set = one.union(two)

print(new_set)


# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
