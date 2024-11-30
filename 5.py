# from array import *
# value=array('i',[1,2,3,4,5,6,7,8,9])
# print(value)
# value.pop()
# print(value)
# value.fromfile(4)
# print(value.fromfile)
# print(value.frombytes(10))
# y=value.extend(0)
# print(y)
# y=value.clear('i')
# value.clear()
# print(value)
# for i in range(4):
#     print(value[i])
# for i in range(len(value)):
#     print(value[i])    

country= ["+91 ", "+1 ", "+44 ", "+93 ", "+92 "]
# countryname=[]
x = input("Enter your mobile number:-> ")
if any(x.startswith(code) and len(x) == len(code) + 10 for code in country):
    print("Correct number")
else:
    print("Incorrect number")
