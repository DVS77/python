list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]
print("input: ",list1)
for i in list1:
    if i > 0:
        print("output:", i)
        

print("input: ",list2)
list3 = list(filter(lambda x: x>0, list2))
print("output:", list3)
