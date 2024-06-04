# def main():
#     cubic_set={x**3 for x in range(10)}
#     print(cubic_set)
    
#     square_set={x**2 for x in range(28)}
#     print(square_set)
    
#     print(cubic_set.intersection(square_set))
#     print(cubic_set - square_set)
# main()
# ____________________________________________________________
# def main():
#     fruits={
#         "apple":"red",
#         "orange":"orange",
#         "grape":"green",
#         True:10
#     }
#     print(fruits["apple"])
#     print(fruits["orange"])
#     print(fruits["grape"])
#     print(fruits[True])
    
#     print()
#     fruits["strawberry"]="red"
#     fruits.update({"banana":"yellow","pineapple":"yellow"})
#     print(fruits)
# main()
# _______________________________________________________________________
# def main():
#     fruits={
#         "apple":"red",
#         "orange":"orange",
#         "grape":"green",
#     }
    
#     for fruit in fruits:
#         print(fruit + ": " + fruits[fruit])
#     print()
    
#     for fruit in fruits.keys():
#         print(fruit+": "+fruits[fruit])
#     print()
        
#     print("apple" in fruits)
#     print()
    
#     for fruit,color in fruits.items():
#         print(fruit+", "+color)
        
#     for fruit in fruits.values():
#         print(fruit)

# main()
# ___________________________________________________________________
# def main():
#     fruits={
#         "apple":"red",
#         "orange":"orange",
#         "grape":"green",
#     }
#     keys=fruits.keys()
#     values=fruits.values()
#     items=fruits.items()
    
#     print(keys)
#     print(values)
#     print(items)
    
#     keys_list=list(keys)
#     print(keys_list)
    
#     fruits["lime"]="green"
#     print(keys)
#     print(keys_list)
# main()
# ___________________________________________________________________
# def main():
#     fruits={
#         "apple":"red",
#         "orange":"orange",
#         "grape":"green",
#     }

#     del fruits["orange"]
#     print(fruits)
    
#     color=fruits.pop("apple")
#     print(color)
    
#     print(fruits)
# main()
# ___________________________________________________________________
# def main():
#     fruits={
#         "apple":"red",
#         "orange":"orange",
#         "grape":"green",
#     }

#     color=fruits.get("mango")
#     print(color)
#     print(type(color))
    
#     color=fruits.get("mango","red")
#     print(color)
    
#     color=fruits.get("banana","red")
#     print(color)
# main()
# ___________________________________________________________________
# def main():
#     fruits={
#         "apple":"red",
#         "orange":"orange",
#         "grape":"green",
#     }
#     fruits2={key:value for key,value in fruits.items()}
#     print(fruits2)
# main()
# ___________________________________________________________________
# def create_lookup(people,ages):
#     lookup=dict()
    
#     for i in range(0,len(people)):
#         name=people[i]
#         age=ages[i]
#         lookup[name]=age
#     return lookup

# def main():
#     people=["mg mg","ko ko","ma ma","aung aung","zaw zaw"]
#     age=[12,13,15,16,18]
#     lookup=create_lookup(people,age)
#     print(lookup)

# main()
# ___________________________________________________________________
# def create_lookup(people,ages):
#     lookup=dict()
    
#     for i in range(0,len(people)):
#         name=people[i]
#         age=ages[i]
#         lookup[name]=age
#     return lookup
# def user_lookup(lookup):
#     while True:
#         user_input=input("Enter a name, or 'quit' > ")
        
#         if user_input=="quit":
#             break
#         elif not user_input in lookup:
#             print("Unknown user")
#             continue
        
#         age=lookup[user_input]
#         print(user_input+" is "+ str(age)+" years old")

# def main():
#     people=["mg mg","ko ko","ma ma","aung aung","zaw zaw"]
#     age=[12,13,15,16,18]
    
#     lookup=create_lookup(people,age)
    
#     user_lookup(lookup)

# main()
# ___________________________________________________________________

# NAME="ZAW SHINE"
# name="zaw shine"
# print(name.casefold() == NAME.casefold())

# names={"zaw zaw":22}
# age=names.get("Kyaw Kyaw")
# print(age)

# if age is None:
#     print("Name not found")

# ___________________________________________________________________
# fruits=["apple","orange","banana"]
# animals=['dog','cat','mouse']

# for i,items in enumerate(fruits):
#     print(i,items)
# print()

# for fruit,animal in zip(fruits,animals):
#     print(fruit,animal)
# ___________________________________________________________________

def create_lookup(people,ages):
    lookup=dict()
    
    for name,age in zip(people,ages):
        lookup[name.casefold()]=age
    return lookup
    
def user_lookup(lookup):
    while True:
        user_input=input("Enter a name, or 'quit' > ")
        
        if user_input=="quit":
            break
        elif not user_input.casefold() in lookup:
            print("Unknown user")
            continue
        
        age=lookup[user_input.casefold()]
        print(user_input+" is "+ str(age)+" years old")

def main():
    people=["mg mg","ko ko","ma ma","aung aung","zaw zaw"]
    age=[12,13,15,16,18]
    
    lookup=create_lookup(people,age)
    
    user_lookup(lookup)

main()