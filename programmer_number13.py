list=[3,2,1,3,3,4,1,2,3,1]
list_=[3,2,1,3,3,4,1,2,3,1]
# print(min(list))
n=0
a=len(list_)
list1=[]
while n<len(list):
    list1.append(min(list))
    # print(min(list))
    # list.remove(min(list))
    n+=1
# list1.append(min(list))

print(list1)
