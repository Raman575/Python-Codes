# Strings are IMMUTABLE :)
names = "John, Jack, Jim, Ram"
print(names)  

print(id(names)) 

upper_case_names = names.upper()
print(upper_case_names) 

lower_case_names = names.lower()
print(lower_case_names)


s1 = names.capitalize()
print("s1",s1)


s2 = names.title()
print(s2)  


s3 = names.swapcase()
print(s3)  

s4 = names.replace("John", "Jane")
print(s4)  
"""
password = input("Enter your password:")
print("Password", password.strip())
"""
data='0000000547'
print(data.strip('0'))
num = 3.545400101
num = float(str(num).strip('0'))
print("number is:", num)
number = "547"
print(number.zfill(50))
qoute = "Search the candle rathar than cursing in darkness"
print(qoute.find('sing'))
print(qoute.find('the'))
print(qoute.index('the'))
print(qoute.rindex('the'))

idx1 = qoute.index('candle')
idx2 = idx1 +len('candle')-1
print(idx1)
print(idx2)
for ch in qoute:
    print(ch,end=" ")
message = "No Internet Connectivity"
print(message)
print(message.center(120))
print(message.ljust(120))
print(message.rjust(120))

names = "John, Jack, Jim, Ram"
print(len(names))
print(names[1])
print(names[len(names)-1])

split_names = names.split(", ")
print(split_names, type(split_names))
s1 = names.replace("Jim", "Mike")
print(names)
print(s1)

idx = names.find("hlo")
print(idx)

idx = names.find("John")
print(idx)
idx = names.find("t")
print(idx)
