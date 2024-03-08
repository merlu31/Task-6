#You have been given Python List[10,501,22,37,100,999,87,351] your task is to create two List 
#one which have all the Even Numbers and another List which will have all the ODD numbers in it?
# declare and assign list1
list1 = [10,501,22,37,100,999,87,351]
# declare listOdd - to store odd numbers
# declare listEven - to store even numbers
listOdd = []
listEven = []
# check and append odd numbers in listOdd
# and even numbers in listEven
for num in list1:
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)
# print lists
print("list1:    ", list1)
print("listEven: ", listEven)
print("listOdd:  ", listOdd)