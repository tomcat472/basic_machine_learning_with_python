# def main():
#     num=[[1,2,3],[4,5,6],[7,8,9]]
    
#     sublist=num[0]
#     print(sublist)
    
#     print(sublist[2])
#     print(num[2][0])
# main()
# _______________________________________________________________# def main():
# def main():
#     num=[[1,2,3],[4,5,6],[7,8,9]]

    # for x in num:
    #     for y in x:
    #         print(y,end="")
    #     print()
    
#     for i in range(0,len(num)):
#         for j in range(0,len(num[i])):
#             print(num[i][j],end="")
#         print()
# main()
# _______________________________________________________________# def main():
# student={
#     "naing":["running","reading"],
#     "aung":["coding","walking"]
# }
# print(student["naing"][0])

# for name,hobbies in student.items():
#     print(name)
#     print()
#     for hobby in hobbies:
#         print(hobby)
#     print()
# _______________________________________________________________# def main():
# def find_book(library, book):
#     for books in library.values():
#         if book in books:
#             return True
#     return False


# def add_book(library, category, title):
#     if not category in library:
#         library[category] = set()
        
#     library[category].add(title)

# def main():
#     library = {
#         "computer": {"coding", "microsoft"},
#         "comics": {"ironman", "batman"}
#     }
#     add_book(library, "computer", "pandas")
    
#     for category in library:
#         books = library[category]
#         print(category + ": ", end="")
        
#         print(", ".join(books))
        
#     print(find_book(library, "batman"))  
 
# main()
# ________________________________________________________________________
# value=0

# def do_something():
#     global value
#     print(value)
#     value=100
#     print(value)
    
# def main():
#     do_something()
#     print(value)
# main()