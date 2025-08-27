#1.Create an empty list called my_list.
my_list=[]
#2.Append the numbers 10, 20, 30, and 40 to my_list.
my_list.append(10)
my_list.append (20)
my_list.append(30)
my_list.append(40)
print(my_list)
#3.Insert the number 15 at index 1 in my_list.
my_list.insert(1, 15)
print(my_list)
#4.Extend my_list by adding the numbers 50, 60, and 70.
my_list.extend([50,60,70])
print(my_list)
#5.Remove the last element from my_list.
del my_list[-1]
print(my_list)
#6.Sort my_list in ascending order.
my_list.sort()
print(my_list)
#7.Find and print the index of the value 30 in my_list.
idx_30 = my_list.index(30)
print("Index of 30:", idx_30) 



