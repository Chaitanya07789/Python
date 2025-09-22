dict = {
    "name":"Chaitanya",
    "city":"Pune",
    "job":"none",
    "mobile_no":7757877681,
    "age":24
}

for index,key in  enumerate(dict): # used for iterating index and key at a same time 
    print(f" {index} : {key}")


for key,value in dict.items(): # used for iterating key-value pair
    print(f"{key} : {value}")

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

# adding value in dict
dict["email"] ="chaitanyalondhe730@gmail.com"
dict.update({"job":"developer", "gender":"male"})


for key,value in dict.items(): # used for iterating key-value pair
    print(f"{key} : {value}")

print(dict.get("name")) # returns the value of key if present ,otherwise none .can give default value in case value is not present like dict.get("name",0)

