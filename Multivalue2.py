                                              #EXPLORE LIST iIN PYTHON
"""
num = list(range(10, 101, 10))
print("numbers:", num)
print(type(num))
num.append(20)
num.append(10)
num.append(20)
print("numbers now:", num)
print(sum(num))
print(len(num))
print(max(num))
print(min(num))
reverse_num = reversed(num)
reverse_num = list(reversed(num))
print(reverse_num)
print(num.index(20))
print(num.count(30))
data = [100, 10, 29, 90, 85, 57]
print(data)
data.sort()
print("Data now:", data)
names = ["John", "Jack", "Ram", "Shivam", "Mandeep", "Abhishek"]
names.sort()
print(names)
print(min(names))
print(max(names))
names.remove("John")
print(names)
data = [100, 10, 29, 90, 85, 57]
data.remove(10)
print(data)
#DELETE or INSERT commands
data = [100, 10, 29, 90, 85, 57]
data.pop()
data.pop()
print(data)
data.insert(0,10)
print(data)
data.insert(5, 10)
print(data)
"""
                                                #EXPLORE SET IN PYTHON
"""
john_followers = {"Ram", "Sham", "Mandeep"}
print(john_followers)
numbers = list(range(10, 101, 10))
print(numbers)
numbers = set(numbers)
print("NO0W DATA:", numbers)
numbers.add(110)
numbers.add(510)
numbers.add(710)
print("NOW DATA:", numbers)
numbers.pop()
numbers.pop()
numbers.pop()
print(numbers)
numbers.remove(110)
numbers.discard(80)
print(numbers)

john_followers = {"Raman", "Daman", "Sanam", "mandeep"}
Jack_followers = {"Raman", "kanav", "Sanam", "shivam"}
joe_followers = {"Raman", "Sanam"}

mutual_followers = john_followers.intersection(Jack_followers).intersection(joe_followers)
print(mutual_followers)
print(joe_followers.issubset(john_followers))
print(john_followers.issuperset(joe_followers))

A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}
C = A - B
print(C)
D = A & B
print(D)
E = A | B
print(E)
F = A ^ B
print(F)
A.clear()
print(A)
G = A.symmetric_difference(B)
print("G is:", G)
"""
                                         #EXPLORE DICTIONAARY IN PYTHON
my_data = {1:"Raman", 2:"Sanam", 3:"Mandeep"}
print(my_data)
print(min(my_data))
print(max(my_data))
print(sum(my_data))
print(my_data[2])
print(my_data.pop(3))
print(my_data)
my_data[3] = "Teji"
print(my_data)
my_data[3] = "mandeep"
print(my_data)
del my_data[3]
print(my_data)
columns = ['from', 'to']
flights = {}.fromkeys(columns, "delhi")
print(flights)
columns = ['ludhiana', 'patiala','jalandhar','bathinda']
tickets = {}.fromkeys(columns,101)
print(tickets)
tickets["amritsar"] = 102
print(tickets)
items = list(tickets.items())
print(items)





