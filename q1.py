IDS_SUBMISSION = 316296771

#functions that exists in strings but not in lists:
name = "xyzw"

# (1)
str.isalpha(name)
# (2)
name.isalpha()

# (1)
str.islower(name)
# (2)
name.islower()

# (1)
str.title(name)
# (2)
name.title()


#functions that exists in lists but not in strings:
list1 = ['x','y','z','w']

# (1)
list.copy(list1)
# (2)
list1.copy()

# (1)
list.sort(list1)
# (2)
list1.sort()

# (1)
list1 = ['x','y','z','w']
list.append(list1, 'a')
# (2)
list1 = ['x','y','z','w']
list1.append('a')
