"""
MULTI VALUE CONTAINER 
   sequences
   tuple
   list
   set
   string

    dictioinary
    
    PROPERTIES:
    1 Indexing
    2 Negative indexing
    3 Slicing
    4 Concatenation
    5 Multiplicity
    6 Membership Testing
    """
    
my_data = [10, 20, 30]

numbers = [
     [10, 20, 30],
      [10, 20, 30, 40, 50, 60, 70],
       [46, 78, 55, 32]
]

print(len(my_data))
print(my_data[1])
print(len(numbers))
print(numbers[1][2])
large_data = [
[
     [10, 20, 30],
      [10, 20, 30, 40, 50, 60, 70],
       [46, 78, 55, 32]
],
[
     [10, 20, 30],
      [10, 20, 30, 40, 50, 60, 70],
       [46, 78, 55, 32]
]
]

print(large_data[1][2][1])
print(my_data[-1])
print(large_data[-2][-2][-4])
#Slicing
data = list(range(10,101, 10))
print("DATA:",data)
print("DATA:[:5]",data[:5])
print("DATA:[4:]",data[4:])
print("DATA:[2:6]",data[2:6])
print("DATA [:-5]",data[:-5])
print("DATA:[-5:-2]",data[-5:-2])


#concatenation
data1 = (10, 20, 30)
data2 = (40, 50, 60)

data3 = data1 + data2
print("DATA3:", data3)

#Multiplicity
data4 = data1 * 3
print("DATA 4 :", data4)

#Membership testing
print(10 is data1)
print(100 is data1)
print(1000 not in data1)
"""
student = {
    "Name":"Ramanjot",
    "rollno" : "1256",
    "age" : "45",
    "class" : "CSE"
}
student2 = {
    "Name":"damanjot",
    "rollno" : "1286",
    "age" : "47",
    "class" : "CSE"
}
student3 = student + student2
print("STUDENT3:",student3)
"""
"""
    dictioinary
    
    PROPERTIES:
    1 Indexing 
    2 Negative indexing
    3 Slicing
    4 Concatenation
    5 Multiplicity
    6 Membership Testing
    """
#Assignment -> Explore all the properties on string:)
qoute1 = "Search the candle rather than cursing in darkness | "
#Indexing 
print("qoute1 :)",len(qoute1))
#Negative indexing
print("qoute1 :",qoute1[-1])
#Slicing
print("qoute1:[4:]",qoute1[4:])
print("qoute1:[4:19]",qoute1[4:19])
#Concatenation
qoute2 = "Explore all the properties on string | "
qoute3 = "MULTI VALUE CONTAINER "
qoute4 = qoute1 + qoute2 + qoute3
print("QOUTE3:",qoute4)
#Multiplicity
qoute5 = qoute1 * 2 + qoute3
print("QOUTE3:",qoute5)
#Membership Testing
print("Hlo" is qoute2)
print("MULTI VALUE CONTAINER " is qoute3)
print("MULTI VALUE CONTAINER " not in qoute1)