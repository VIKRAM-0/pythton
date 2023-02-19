import copy #module used for copying without the same reference
mydict = {"name":"vk", "age":18, "gender":"male"}
mydict1 = copy.deepcopy(mydict) #copying the dictionary using the copy module
print(mydict)
#keys are used to access the dictionary not the index

#adding new key:value pair
mydict["email"] = "xyz.com"
print(mydict)

#deleting key value pair
del mydict["gender"]
print(mydict)
#or
mydict.pop("age")
print(mydict)
#to remove the last element
mydict.popitem()
print(mydict)

#keys method
iem = mydict.keys()
me = mydict.values()
iep = mydict.items()
print("the key is",iem,"the value is",me)
print("the items in dictionary\r",iep)

#updating the dictionary
mydict.update(mydict1)
print()
print("afetr update",mydict)

#using tuple as a key
tuple1 = (2,5)
dict_tuple = {tuple1:7}
print("dictionary with tuple\n",dict_tuple)
#list can't be used as a key since its is a mutable data type 