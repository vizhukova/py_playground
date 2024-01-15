list_1 = [1, 2, 3, 4, 5, 6, 7]
print("Expected ([1, 2, 3, 4, 5, 6, 7]): " + str(list_1))
print("Expected (1): " + str(list_1[0]))
print("Expected (3): " + str(list_1[-1]))
print("Expected (2): " + str(list_1[-2]))

print("Expected all elements after 1: " + str(list_1[1:]))
print("Expected all elements after 1: " + str(list_1[1:]))
print("Expected all elements [3, 4, 5], not including last one desired element: " + str(list_1[2:5]))

extended_list_1s = [1,2,4]
extended_list_1s.extend(['str1', 'str2', 'str3'])
print("Exptend list_1 with other format data: " + str(extended_list_1s))
extended_list_1s.append(4.55)
print("Appended new item to the list_1" + str(extended_list_1s))
index = input("Enter _index_ where should be inserted the new item: ")
new_item = input("Enter the new item: ")
extended_list_1s.insert(int(index), new_item)
print('The result: ' + str(extended_list_1s))
extended_list_1s.remove(new_item)
print("Joke, you have not power to change here anything, the list_1 is still: " + str(extended_list_1s))
extended_list_1s.clear()
print("We are done with you, here is your list_1: " + str(extended_list_1s))

print("Wooooow, stop cry...")

arr = [1, 2, 1, 1, 5, 6, 7] 
item_index = arr.index(1)
print("Will show only first enterance of item: " + str(item_index))
item_count = arr.count(1)
print("But here is the amount of that items: " + str(item_count))

# print("Expectint error out of range: " + str(list_1[-7]))
# print("Expectint error out of range: " + str(list_1[7]))
print("created quick list from 0 to 4: ", list(range(5)))
print("created quick list from 2 to 4: ", list(range(2, 5)))