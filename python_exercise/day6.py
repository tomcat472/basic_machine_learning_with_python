## lists
# def main():
#     fruits=["apple","orange","grape"]
#     print(len(fruits))
    
#     print(fruits[2])
#     print(fruits[0:2])
    
#     test1=tuple()
#     test2=list()
    
#     animals=("fox","lion")
#     print(animals)
#     animals=list(animals)
#     print(animals)
    
#     for animal in animals:
#         print(animal)
    
# main()
# _______________________________________________________________
## joining lists
# def main():
#     animals1=("dog","cat","mouse")
#     animals2=("lion","tiger","elephant")
    
#     fruits1=["apple","orange"]
#     fruits2=["melon","pineapple","peach"]
    
#     value=5
#     value+=3
#     print(value)
    
#     print(id(animals1))
#     animals1+=animals2
#     print(animals1)
#     print(id(animals1))
    
#     fruits1+=fruits2
#     print(fruits1)
# main()
# ________________________________________________________________
## modifying list
# def main():
#     fruits=['apple','orange','grape','lime','kiwi']
#     print(fruits)
    
#     fruits.append("peach")
#     fruits.append("watermelon")
#     print(fruits)
    
#     fruits[0]="during"
#     print(fruits)
#     print()
#     # fruits[1:3]="lychee"
#     fruits[1:3]=["lychee"]
#     print(fruits)

#     fruits[16:]=["lemon","corn"]
#     print(fruits)
# main()
# ____________________________________________________________________________
## extended slicing
# def main():
#     numbers=[0,1,2,3,4,5,6,7,8,9,10]
    
#     print(numbers[3:7:2])
    
#     numbers[3:7:2]=["Hi","Hello"]
#     print(numbers)
    
#     print(numbers[::])
    
#     greeting="Hello there"
#     print(greeting[::2]) #start,stop,step
    
#     print("How are you?"[3::3])

# main()
# _________________________________________________________________
## extending and inserting into list
# def main():
#     animals=["dog","donkey","duck"]
#     animals.insert(0,"mouse")
#     print(animals)
#     print()
    
#     more_animals=["snake","lion"]
#     animals.extend(more_animals)
#     print(animals)

# main()
# __________________________________________________________________________
## removing list items
# def main():
#     num=[11,12,13,14,15,16,17,18]
    
#     num[2:4]=[]
#     print(num)
#     print()
    
#     num.remove(17)
#     print(num)
    
#     item=num.pop(0)
#     print(num)
    
#     del num[2]    
#     print(num)
#     print()
    
#     num.clear()
#     print(num)
# main()
# ____________________________________________________________________
## list comprehension flexibly creating lists
# def main():
#     animals=["dog","cat","snake"]
#     animals2=[animal.upper() for animal in animals]
#     print(animals2)

#     lengths=[len(animal) for animal in animals]
#     print(lengths)

#     num=[3,4,2,3,5]
#     square=[n**2 for n in num]
#     print(square)
# main()
# __________________________________________________________________
## list comprehension condition
# def main():
#     num1=[x for x in range(0,10)]
#     print(num1)
    
#     num2=[x for x in num1 if x>5]
#     print(num2)
    
#     # mod operator
#     print(13%5)
#     print(18%2==0)
    
#     num3=[x for x in num1 if x%2==0]
#     print(num3)
# main()
# _____________________________________________________________________
# list comprehension ifelse
def main():
    numbers=[x for x in range(0,20) if x%2==1]
    print(numbers)
    
    more_numbers=[2*x if x>10 else 0 for x in numbers]
    print(more_numbers)
main()