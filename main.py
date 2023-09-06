person={
    "name":"maryam",
    "age" : 18,
    "hobbies":["swimming","writing","watching films"]
}
print(person["name"])
print(person["age"])
person["age"]=15
print(person["age"])
person["country"]= "japan"
print(person)
print(len(person))
person["hobbies"].append("coding")
print(person["hobbies"])

def check_hobbies(person):
    if len(person["hobbies"])>=3:
        print("you are amazing!")
    else:
        print("think harder")
check_hobbies(person)    
 
