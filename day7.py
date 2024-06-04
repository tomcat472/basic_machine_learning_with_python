# def show_menu():
#     options=("Display the database","add an item","delete an item","change an item","quit")
    
#     for i in range(0,len(options)):
#         print(f"{str(i)} : {options[i]}")

# def show_database(db):
#     print()
#     for i in range(0,len(db)):
#         print(f"{str(i)} : {db[i]}")

# def add_item(db):
#     item=input("Enter item to add: ")
#     db.append(item)

# def change_item(db):
#     item_number=input('Enter number of item to change: ')
#     item=input("Enter new item: ")
    
#     db[int(item_number)]=item

# def delete_item(db):
#     item_number=input('Enter number of item to delete: ')
#     db.pop(int(item_number))

# def main():
#     db=["apple","orange","mango"]
    
#     # show_menu()
#     # show_database(db)
#     # add_item(db)
#     # change_item(db)
#     # delete_item(db)
#     # show_database(db)
#     do_loop=True
    
#     while do_loop:
#         show_menu()
#         print()
#         option=int(input("select option > "))
        
#         if option == 0:
#             show_database(db)
#             print("*************************************")
#         elif option ==1:
#             add_item(db)
#         elif option==2:
#             delete_item(db)
#         elif option==3:
#             change_item(db)
#         elif option==4:
#             do_loop=False
#         else:
#             print("unrecognised option")

# main()
# _____________________________________________________________________________
## set

# num={1,2,3,4,5}
# print(num)

# number_list={2,2,2,24,3,2,3,2,3,22,9}
# print(set(number_list))

# for number in number_list:
#     print(number)
    
# print(3 in number_list)
# print(100 in number_list)

##note
#list: ordered and mutable, "in" is slow
#tuple : ordered and immutable, "in" is slow
#set: not ordered and mutable, "in"  is fast
# ______________________________________________________________________________
# def main():
#     number1={1,2,3}
#     print(number1)
    
#     number1.add(7)
#     number1.add(10)
#     print(number1)
#     print()
    
#     number2={100,200,300}
#     number1.update(number2)
#     print(number1)
#     print()
    
#     number1.update(["he","she"])
#     print(number1)
    
# main()
# _______________________________________________________________________________
# def main():
#     num={x for x in range(15)}
#     print(num)

#     num.remove(7)
#     print(num)

#     num.discard(11)
#     print(num)

#     for x in num:
#         print(x)

# main()
# _______________________________________________________________________________
# def main():
#     num1={1,3,5,7,9,11}
#     num2={x for x in range(1)}
    
#     print(num1)
#     print(num2)
    
#     print(num1.union(num2))
#     print(num1.intersection(num2))
    
#     print("difference")
#     print(num1.difference(num2))
#     print(num1-num2)
#     print(num2.difference(num1))
    
#     print(num2.symmetric_difference(num1))
# main()
# _______________________________________________________________________________
def main():
    num1={1,2,3,4,5,6,7}
    num2={8,0,3,10,3,6,1}
    
    num1.difference_update(num2)
    print(num1)
    
    print(num1.issuperset(num2))
    
    print({1,2,3}.issuperset({1,2}))
main()