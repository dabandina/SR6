from array import*
array1 = array("i", [1,2,3,4,5,6])
smallest_number = min(array1)
print("The smallest number is: ", smallest_number)
delta = 3
count = 0
count = sum(map(lambda item: item ==smallest_number+delta, array1))
print("количество элементов удовлетворяющих условию: ", count)