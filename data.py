#Create empty list
my_list = []

#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert
my_list.insert(1, 15)

#Extend
my_list.extend([50, 60, 70])

#Check my_list 
print(my_list[1:7])

#remove last element
my_list.pop()

#sort my_list in ascending
my_list.sort()

#find and print index of value 30
index_of_30 = my_list.index(30)

#print the modified
print("Modified list:", my_list)
print("Index of 30:", index_of_30)