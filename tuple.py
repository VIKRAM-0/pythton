#module for coping values
import copy
import sys #module for konwing about he program with the computer
import timeit #module for calculating execution time
mytuple = ("vk",1,"jk","vk",2,3,1)
mylist=["vk",1,"jk","vk",2,3,1]
print(type(mytuple))

#coping tuple
cpy=copy.deepcopy(mytuple)
print(cpy)

#counting the occurence of an element
count1=mytuple.count(1)
print("the count of 1 is",count1)

#index method
index1 = mytuple.index("jk")
print("the index of jk is\n",index1)

#unpacking a tuple
tuple1 = ("jack",15,"good")
name,age,remarks = tuple1
print(name)
print(age)
print(remarks)

#unpacking multiple elements with *
tuple2 = (1,2,3,4,5,6)
l1 , *l2 ,l3 = tuple2
print(l1)
print(l2)
print(l3)

#comparision with list
print(sys.getsizeof(mytuple),"bytes","--tuple")
print(sys.getsizeof(mylist),"bytes","--list")
#both contian the same elements 
#execution time for creating tuple and list
print(timeit.timeit(stmt="(1,2,3,4)",number=100),"--tuple creation")
print(timeit.timeit(stmt="[1,2,3,4]",number=100),"--list creation")
