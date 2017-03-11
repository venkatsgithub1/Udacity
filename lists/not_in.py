list1=[1,2,3,4]

varToBeFound=2

#below line prints True because value 2 is present in  list1
print (varToBeFound in list1)

varToBeFound=55

#below line prints False since 55 is not present in list1
print (varToBeFound in list1)

#below line prints True since 55 is not present in the list1
#observation: in keyword is used with not before, which means
#search for not being found in list1 is being done.
print (varToBeFound not in list1)
