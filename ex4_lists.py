__author__ = 'sakkas'


list=["Hale","Jale","Lale"]
print(list)
list.append("Ahmet")
print(list)
list.insert(1,"Mehmet")
print(list)


#extending the list
list2=["Ali","Veli"]
#list=list+list2# same job with extend
list.extend(list2)
print(list)


#removing an element
list.remove("Ahmet")# if there is more than 1 Ahmet, it will remove the first one.
print(list)


print(list.pop())#returns the removed element
print(list.pop(3))#removes the third element and returns it
print(list)
print(list.index("Mehmet"))#Returns the Mehmet's index


#sorting
list.sort()# if there are different types then it won't work
print(list)



list.append("Ali")
#counts the element
print(list.count("Ali"))


#list[-5] gives first element=list[0]
print(list[-2])



#sublist
#list[first:last] last is not included.
print(list[1:3])
print(list[2:])#till end