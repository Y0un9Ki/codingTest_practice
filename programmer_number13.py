list=[3,2,3,3,4,3]
list_=[3,2,1,3,3,4,1,2,3,1]
# print(min(list))
n=0
a=len(list_)
list1=[]
while n<len(list):
    list1.append(min(list))
    # print(min(list))
    list.remove(min(list))
# list1.append(min(list))
    # n+=1 이것때문에 틀림 잘생각해보기

print(list1)
a=[1,2,3,4,5]
print(min(a))