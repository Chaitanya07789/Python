# how many times each element occured in list
list = [1,1,2,3,2,6,8,9,5,6,7,2,3,1,2]
print(f"length of list : {len(list)}")

dict = {}

for i in list:
    dict[i] = dict.get(i,0) +1

print(dict)        

